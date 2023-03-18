from __future__ import annotations

import io


class InvalidBond(RuntimeError):
    pass


class EmptyMolecule(RuntimeError):
    pass


class LockedMolecule(RuntimeError):
    pass


class UnlockedMolecule(RuntimeError):
    pass


class Atom:
    """Represents a specific atom in a specific molecule."""

    _PROPERTIES = {
        # Symbol: (valence, atomic weight)
        'H': (1, 1.0),
        'B': (3, 10.8),
        'C': (4, 12.0),
        'N': (3, 14.0),
        'O': (2, 16.0),
        'F': (1, 19.0),
        'Mg': (2, 24.3),
        'P': (3, 31.0),
        'S': (2, 32.1),
        'Cl': (1, 35.5),
        'Br': (1, 80.0),
    }

    def __init__(self, symbol: str, id_: int, branch_id: int = None):
        """Create an atom inside a molecule.

        :param symbol: Symbol of this atom’s chemical element.
        :param id_: This atom’s ID within its molecule.
        :param branch_id: ID of the molecule branch this atom belongs to.
        :raise ValueError: If the symbol is undefined.
        """
        if symbol not in self._PROPERTIES:
            raise ValueError(f'invalid atomic symbol "{symbol}"')
        self._element = symbol
        self.id = id_  # May be changed by Molecule.unlock()
        self.branch_id = branch_id  # May be changed by Molecule.unlock()
        self._bonds: list[Atom] = []

    @property
    def element(self) -> str:
        """This atom’s element symbol."""
        return self._element

    @element.setter
    def element(self, element: str):  # Called by Molecule.mutate()
        """Set this atom’s element symbol.

        :param element: This atom’s new element.
        :raise InvalidBond: If the new element’s valence is less than the atom’s current bonds number.
        """
        if self._PROPERTIES[element][0] < len(self._bonds):
            raise InvalidBond()
        self._element = element

    @property
    def valence(self) -> int:
        """This atom’s valence."""
        return self._PROPERTIES[self.element][0]

    @property
    def weight(self) -> float:
        """This atom’s atomic weight."""
        return self._PROPERTIES[self.element][1]

    @property
    def bonds(self) -> list[Atom]:
        """List of all atoms this one is bound to."""
        return self._bonds.copy()

    def bind(self, atom: Atom):
        """Add a bond between this atom and the given one.
        Reverse binding is also done on the argument atom.

        :param atom: The atom to bind with this one.
        :raise InvalidBond: If this atom or the given one cannot be bound further.
        :return: This object.
        """
        if atom is self or len(self._bonds) == self.valence or len(atom._bonds) == atom.valence:
            raise InvalidBond()
        self._bonds.append(atom)
        atom._bonds.append(self)
        return self

    def unbind(self, atom: Atom):
        """Remove the bond between this atom and the given one.
        Reverse binding is also undone in the argument atom.

        :param atom: The atom to unbind from this one.
        :return: This object.
        """
        if atom in self._bonds:
            self._bonds.remove(atom)
        if self in atom._bonds:
            atom._bonds.remove(self)

    def unbind_all(self):
        """Remove all bonds this atom has."""
        for bond in self._bonds.copy():  # Copy as list’s length mutates within loop
            self.unbind(bond)

    def __hash__(self):
        return self.id

    def __eq__(self, other):
        return self.id == other.id

    def __repr__(self):
        args = f'{self.element}.{self.id}'
        if self._bonds:
            bonds = [f'{atom.element}{atom.id}' if atom.element != 'H' else atom.element
                     for atom in sorted(self._bonds, key=self._atoms_sorting_key)]
            args += ': ' + ','.join(bonds)
        return f'Atom({args})'

    @staticmethod
    def _atoms_sorting_key(atom: Atom) -> tuple[str, int]:
        """Sorting key for bounded to atoms in __repr__()."""
        e, id_ = atom.element, atom.id
        if e == 'C':  # Carbons first
            return ' ', id_
        if e == 'O':  # Oxygens second
            return '!', id_
        if e == 'H':  # Hydrogens last
            return '~', id_
        return e, id_


class Molecule:
    """Represents a single molecule."""

    def __init__(self, name: str = ''):
        """Create an empty molecule.

        :param name: This molecule’s name. Optional.
        """
        self._name = name
        self._formula = ''
        self._weight = 0.0
        self._atoms: list[Atom] = []
        self._locked = False
        self._branches: list[list[Atom]] = []

    @property
    def name(self) -> str:
        """This molecule’s name."""
        return self._name

    @property
    def formula(self) -> str:
        """This molecule’s raw formula.

        :raise UnlockedMolecule: If this molecule is not yet locked.
        """
        self._ensure_locked()
        return self._formula

    @property
    def molecular_weight(self) -> float:
        """This molecule’s total weight.

        :raise UnlockedMolecule: If this molecule is not yet locked.
        """
        self._ensure_locked()
        return self._weight

    @property
    def atoms(self) -> list[Atom]:
        """The list of this molecule’s atoms."""
        return self._atoms.copy()

    def brancher(self, *carbons: int) -> Molecule:
        """Add branches to this molecule.
        Each integer corresponds to the number of carbon atoms on each branch.

        :param carbons: List of number of carbons on each branch.
        :return: This object.
        :raise LockedMolecule: If this molecule is locked.
        """
        self._ensure_unlocked()
        roots = []
        for n in carbons:
            branch_id = len(self._branches) + 1
            # Create branch’s root
            root_carbon = self._create_atom('C', branch_id)
            roots.append(root_carbon)
            self._branches.append([root_carbon])
            # Create remaining atoms in the current branch
            for _ in range(n - 1):
                carbon = self._create_atom('C', branch_id)
                root_carbon.bind(carbon)
                self._branches[-1].append(carbon)
                root_carbon = carbon
        return self

    def bounder(self, *bonds: tuple[int, int, int, int]) -> Molecule:
        """Create bonds between two atoms.

        :param bonds: List of 4-tuples indicating the index and branch of each carbon to bind.
        :return: This object.
        :raise LockedMolecule: If this molecule is locked.
        """
        self._ensure_unlocked()
        for carbon1_i, branch1_id, carbon2_i, branch2_id in bonds:
            self._branches[branch1_id - 1][carbon1_i - 1].bind(self._branches[branch2_id - 1][carbon2_i - 1])
        return self

    def mutate(self, *mutations: tuple[int, int, int]) -> Molecule:
        """Mutate a carbon into another element.

        :param mutations: List of 3-tuples indicating the index and branch of the carbon as well
            as the symbol of the element to replace it by.
        :return: This object.
        :raise LockedMolecule: If this molecule is locked.
        """
        self._ensure_unlocked()
        for carbon_i, branch_id, new_element in mutations:
            self._branches[branch_id - 1][carbon_i - 1].element = new_element
        return self

    def add(self, *elements: tuple[int, int, str]) -> Molecule:
        """Add atoms to specific carbons.

        :param elements: List of 3-tuples indicating the index and branch of the carbon to bind the atom to.
        :return: This object.
        :raise LockedMolecule: If this molecule is locked.
        """
        self._ensure_unlocked()
        for carbon_i, branch_id, element in elements:
            try:
                self._branches[branch_id - 1][carbon_i - 1].bind(self._create_atom(element))
            except InvalidBond:
                self._pop_atom()  # Delete the new atom that could not be bound
                raise  # Stop at first error, re-raise same error
        return self

    def add_chaining(self, carbon_id: int, branch_id: int, *elements: str) -> Molecule:
        """Add a chain of atoms the the specified carbon.

        :param carbon_id: ID of the carbon.
        :param branch_id: ID of the carbon’s branch.
        :param elements: Chain of atoms to bind to the carbon.
        :return: This object.
        :raise LockedMolecule: If this molecule is locked.
        """
        self._ensure_unlocked()
        root = self._branches[branch_id - 1][carbon_id - 1]
        error = None
        atoms_nb = 0
        for element in elements:
            atom = self._create_atom(element)
            atoms_nb += 1
            try:
                root.bind(atom)
            except InvalidBond as e:
                error = e
                break  # Stop at first error
            root = atom
        if error:  # If any error, remove all newly created atoms
            for _ in range(atoms_nb):
                self._pop_atom()
            raise error  # Re-raise error
        return self

    def closer(self) -> Molecule:
        """Lock this molecule.
        Add all necessary hydrogen atoms and compute the raw formula and total weight.

        :return: This object.
        :raise LockedMolecule: If this molecule is already locked.
        """
        self._ensure_unlocked()
        # Add all missing hydrogen atoms
        for atom in self._atoms:
            missing_bonds = atom.valence - len(atom.bonds)
            for _ in range(missing_bonds):
                atom.bind(self._create_atom('H'))
        # Compute raw formula
        s = io.StringIO()
        count = 0
        prev = None
        for atom in sorted(self._atoms, key=self._atoms_sorting_key):
            if not prev or prev.element != atom.element:
                if prev:
                    if count > 1:
                        s.write(f'{prev.element}{count}')
                    else:
                        s.write(prev.element)
                count = 1
                prev = atom
            else:
                count += 1
        if count > 1:
            s.write(f'{prev.element}{count}')
        else:
            s.write(prev.element)
        self._formula = s.getvalue()
        # Compute total weight
        self._weight = 0
        for atom in self._atoms:
            self._weight += atom.weight
        # Lock this molecule to prevent further modifications
        self._locked = True
        return self

    def unlock(self) -> Molecule:
        """Unlock this molecule.
        Remove all hydrogen atoms and empty branches.
        All remaining atoms and branches will be re-numbered.

        :return: This object.
        :raise UnlockedMolecule: If this molecule is unlocked.
        """
        self._ensure_locked()
        # Remove all hydrogen atoms
        for i in range(len(self._atoms) - 1, -1, -1):
            atom = self._atoms[i]
            if atom.element == 'H':
                atom.unbind_all()
                del self._atoms[i]
                for branch in self._branches:
                    if atom in branch:
                        branch.remove(atom)
        # Remove empty branches and re-number remaining ones
        i = 0
        while i < len(self._branches):
            if not self._branches[i]:
                del self._branches[i]
            else:
                i += 1
                for atom in self._branches[i - 1]:
                    atom.branch_id = i
        if not self._branches:
            raise EmptyMolecule()
        # Re-number remaining atoms
        for i, atom in enumerate(self._atoms):
            atom.id = i + 1
        # Lock this molecule to allow modifications
        self._locked = False
        return self

    def _create_atom(self, symbol: str, branch_id: int = None) -> Atom:
        """Create an atom and add it to the list."""
        atom = Atom(symbol, len(self._atoms) + 1, branch_id)
        self._atoms.append(atom)
        return atom

    def _pop_atom(self):
        """Pop the last atom from the list as well as branches."""
        atom = self._atoms[-1]
        atom.unbind_all()
        for branch in self._branches:
            if atom in branch:
                branch.remove(atom)
        del self._atoms[-1]

    @staticmethod
    def _atoms_sorting_key(atom: Atom) -> str:
        """Sorting key for closer() method."""
        e = atom.element
        if e == 'C':  # Carbons first
            return ' '
        if e == 'H':  # Hydrogens second
            return '!'
        if e == 'O':
            return '"'  # Oxygens third
        return e

    def _ensure_unlocked(self):
        """Raise a LockedMolecule error if this molecule is locked.
        Do nothing otherwise.
        """
        if self._locked:
            raise LockedMolecule()

    def _ensure_locked(self):
        """Raise a UnlockedMolecule error if this molecule is unlocked.
        Do nothing otherwise.
        """
        if not self._locked:
            raise UnlockedMolecule()

from __future__ import annotations

import re


class VersionManager:
    def __init__(self, version: str = ''):
        if not version:
            self._major = 0
            self._minor = 0
            self._patch = 1
        else:
            if not (m := re.fullmatch(r'(\d+)(?:\.(\d+)(?:\.(\d+)(?:\.[^.]+)*)?)?', version)):
                raise ValueError('Error occured while parsing version!')
            self._major = int(m.group(1))
            if m.group(2) is not None:
                self._minor = int(m.group(2))
            else:
                self._minor = 0
            if m.group(3) is not None:
                self._patch = int(m.group(3))
            else:
                self._patch = 0
        self._operations = []

    def major(self) -> VersionManager:
        self._operations.append(self.as_tuple())
        self._major += 1
        self._minor = 0
        self._patch = 0
        return self

    def minor(self) -> VersionManager:
        self._operations.append(self.as_tuple())
        self._minor += 1
        self._patch = 0
        return self

    def patch(self) -> VersionManager:
        self._operations.append(self.as_tuple())
        self._patch += 1
        return self

    def rollback(self) -> VersionManager:
        if not self._operations:
            raise RuntimeError('Cannot rollback!')
        self._major, self._minor, self._patch = self._operations.pop()
        return self

    def release(self) -> str:
        return f'{self._major}.{self._minor}.{self._patch}'

    def as_tuple(self) -> tuple[int, int, int]:
        return self._major, self._minor, self._patch

class InvoiceRow:
    _id = 0

    def __init__(self, description: str, unit_cost: float, quantity: int = 1, taxable: bool = True):
        self.id = InvoiceRow._id
        InvoiceRow._id += 1
        self.description = description
        self.unit_cost = unit_cost
        self.quantity = quantity
        self.taxable = taxable
        self.value = unit_cost * quantity


class Invoice:
    def __init__(self, tax_rate: float = 0.2):
        self.tax_rate = tax_rate
        self.rows = []

    def add_row(self, row: InvoiceRow):
        self.rows.append(row)


def is_debit(row: InvoiceRow) -> bool:
    return row.unit_cost < 0


def is_credit(row: InvoiceRow) -> bool:
    return row.unit_cost > 0


def is_taxable(row: InvoiceRow) -> bool:
    return row.taxable


def printable_cost(cost: float) -> str:
    if cost == 0:
        return 'Gratis'
    return f'{cost:.2f}'


def printable_row(row: InvoiceRow, tax_rate: float) -> tuple[str, str, str, str, str, str]:
    if not is_taxable(row):
        tax_rate = 0
    return (row.description, f'{row.quantity:,d}', f'{row.unit_cost:,.2f}', f'{tax_rate:,.2f}',
            f'{row.value:,.2f}', f'{row.value * (1 + tax_rate):,.2f}')


class InvoicePrinter:
    @staticmethod
    def get_credit_rows(invoice):
        return [row for row in invoice.rows if is_credit(row)]

    @staticmethod
    def get_debit_rows(invoice):
        return [row for row in invoice.rows if is_debit(row)]

    @staticmethod
    def get_free_rows(invoice):
        return [row for row in invoice.rows if not (is_debit(row) or is_credit(row))]

    @staticmethod
    def get_sub_total(invoice):
        return sum([row.value for row in invoice.rows])

    @staticmethod
    def get_tax_total(invoice):
        return sum([row.value for row in invoice.rows if is_taxable(row)]) * invoice.tax_rate

    @staticmethod
    def get_grand_total(invoice):
        return InvoicePrinter.get_sub_total(invoice) + InvoicePrinter.get_tax_total(invoice)

    @staticmethod
    def generate_invoice(invoice):
        lines = 0
        items = 0

        tax_rate = round(invoice.tax_rate, 2)

        for row in InvoicePrinter.get_credit_rows(invoice):
            lines += 1
            items += row.quantity
            yield printable_row(row, tax_rate)

        for row in InvoicePrinter.get_debit_rows(invoice):
            lines += 1
            items += row.quantity
            yield printable_row(row, tax_rate)

        for row in InvoicePrinter.get_free_rows(invoice):
            lines += 1
            items += row.quantity
            yield printable_row(row, tax_rate)

        yield 'Lines', str(lines)
        yield 'Items', str(items)
        yield 'Sub Total', '{:.2f}'.format(InvoicePrinter.get_sub_total(invoice))
        yield 'Tax', '{:.2f}'.format(InvoicePrinter.get_tax_total(invoice))
        yield 'Total', '{:.2f}'.format(InvoicePrinter.get_grand_total(invoice))

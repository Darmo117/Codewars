def most_money(students) -> str:
    amounts = {student.name: 5 * student.fives + 10 * student.tens + 20 * student.twenties
               for student in students}
    if len(students) > 1 and all(amounts[students[0].name] == amounts[student.name] for student in students[1:]):
        return 'all'
    return max(amounts.items(), key=lambda e: e[1])[0]

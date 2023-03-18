class Person:
    def __init__(self, name: str):
        self.name = name

    def greet(self, your_name: str) -> str:
        return f'Hello {your_name}, my name is {self.name}'

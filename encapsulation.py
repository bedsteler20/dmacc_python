from datetime import date


class Employee:
    _last_name: str
    _first_name: str
    _address: str
    _phone_number: str
    _salaried: bool
    _start_date: date
    _salary: float

    def __init__(
        self,
        last_name: str,
        first_name: str,
        address: str,
        phone_number: str,
        salaried: bool,
        start_date: date,
        salary: float,
    ):
        self._last_name = last_name
        self._first_name = first_name
        self._address = address
        self._phone_number = phone_number
        self._salaried = salaried
        self._start_date = start_date
        self._salary = salary

    def display(self):
        out = ""
        out += f"{self._first_name} {self._last_name}\n"
        out += f"{self._address}\n"
        if self._salaried:
            out += f"Salaried employee: ${self._salary}/year\n"
        else:
            out += f"Hourly employee: ${self._salary}/hour\n"
        out += f"Start date: {self._start_date}\n"

        return out

    def __str__(self):
        return self.display()
    
    def __repr__(self):
        return self.display()

if __name__ == "__main__":
    emp = Employee(
        first_name="Doe",
        last_name="John",
        address="1234 Elm St",
        phone_number="555-1212",
        salaried=True,
        start_date=date(2000, 1, 1),
        salary=50000.00,
    )
    print(emp.display())

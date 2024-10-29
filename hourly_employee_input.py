def hourly_employee_input():
    """
    Get the name, hours worked, and hourly rate from the user.
    """
    try:
        name = input("Enter your name: ")
        hours = int(input("Enter the number of hours worked: "))
        rate = float(input("Enter the hourly rate: "))
    except ValueError:
        print("Please enter a valid number.")
        hourly_employee_input()

    print(
        f"{name} worked {hours} hours at ${rate:.2f} per hour for a total of ${weekly_pay(hours, rate):.2f}."
    )


def weekly_pay(hours: int, rate: float) -> float:
    """
    Calculate the weekly pay for an hourly employee.
    """
    return hours * rate


if __name__ == "__main__":
    hourly_employee_input()

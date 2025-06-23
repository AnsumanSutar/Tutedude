# Employee Management System (EMS)

def main_menu(employees):
    while True:
        print("\nEmployee Management System")
        print("--------------------------")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            add_employee(employees)
        elif choice == '2':
            view_employees(employees)
        elif choice == '3':
            search_employee(employees)
        elif choice == '4':
            print("Thank you for using the Employee Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

def add_employee(employees):
    print("\nAdd New Employee")
    print("----------------")

    while True:
        try:
            emp_id = int(input("Enter Employee ID (integer): ").strip())
            if emp_id in employees:
                print(f"Employee ID {emp_id} already exists. Please enter a unique ID.")
            else:
                break
        except ValueError:
            print("Invalid input! Employee ID must be an integer.")

    name = input("Enter Employee Name: ").strip()
    while not name:
        print("Name cannot be empty.")
        name = input("Enter Employee Name: ").strip()

    while True:
        try:
            age = int(input("Enter Employee Age: ").strip())
            if age <= 0:
                print("Age must be a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input! Age must be an integer.")

    department = input("Enter Employee Department: ").strip()
    while not department:
        print("Department cannot be empty.")
        department = input("Enter Employee Department: ").strip()

    while True:
        try:
            salary = float(input("Enter Employee Salary: ").strip())
            if salary < 0:
                print("Salary cannot be negative.")
            else:
                break
        except ValueError:
            print("Invalid input! Salary must be a number.")

    employees[emp_id] = {
        'name': name,
        'age': age,
        'department': department,
        'salary': salary
    }

    print(f"Employee {name} (ID: {emp_id}) added successfully.")

def view_employees(employees):
    print("\nAll Employees")
    print("-------------")

    if not employees:
        print("No employees available.")
        return

    # Print header
    print(f"{'ID':<10}{'Name':<20}{'Age':<10}{'Department':<15}{'Salary':<15}")
    print("-" * 70)

    # Print each employee's details
    for emp_id, details in employees.items():
        print(f"{emp_id:<10}{details['name']:<20}{details['age']:<10}{details['department']:<15}{details['salary']:<15.2f}")

def search_employee(employees):
    print("\nSearch Employee by ID")
    print("---------------------")

    try:
        emp_id = int(input("Enter Employee ID to search: ").strip())
    except ValueError:
        print("Invalid input! Employee ID must be an integer.")
        return

    if emp_id in employees:
        details = employees[emp_id]
        print(f"\nEmployee Details for ID {emp_id}:")
        print(f"Name      : {details['name']}")
        print(f"Age       : {details['age']}")
        print(f"Department: {details['department']}")
        print(f"Salary    : {details['salary']:.2f}")
    else:
        print("Employee not found.")

if __name__ == "__main__":
    # Initialize with sample data
    employees = {
        101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
        102: {'name': 'Anita', 'age': 30, 'department': 'Finance', 'salary': 60000},
        103: {'name': 'Ravi', 'age': 25, 'department': 'IT', 'salary': 55000}
    }

    main_menu(employees)

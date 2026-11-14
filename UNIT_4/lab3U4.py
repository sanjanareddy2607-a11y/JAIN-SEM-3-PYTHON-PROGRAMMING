
import csv

# Create and write employee details into CSV file
with open("payroll.csv", "w", newline="") as file:

    writer = csv.writer(file)

    # Write header
    writer.writerow(["Employee ID", "Name", "Basic Salary",
                     "Allowance", "Deduction", "Net Salary"])

    n = int(input("Enter number of employees: "))

    for i in range(n):
        print("\nEnter details of Employee", i + 1)

        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        basic = float(input("Enter Basic Salary: "))
        allowance = float(input("Enter Allowance: "))
        deduction = float(input("Enter Deduction: "))

        # Calculate net salary
        net_salary = basic + allowance - deduction

        # Write employee details into CSV
        writer.writerow([emp_id, name, basic, allowance,
                         deduction, net_salary])

print("\nPayroll records saved successfully!")

# Read and display payroll records
print("\nEmployee Payroll Records:\n")

with open("payroll.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)

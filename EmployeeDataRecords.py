TAX = 0.15 # Delcare TAX, totSal: integer
totalSal = 0


class Employee: 
    name = ""
    number = ""
    hrsWorked = 0
    rateOfPay = 0
    salary = 0
    
    def __init__(self,name,number, hrsWorked, rateOfPay):
        self.name = name
        self.number = number
        self.hrsWorked = hrsWorked
        self.rateOfPay = rateOfPay
    
    def salary(self):
        self.salary = (self.hrsWorked * self.rateOfPay)-((self.hrsWorked * self.rateOfPay)*TAX)
        return self.salary
        

menu = ""
employees = []
# Input from others
while (True): 
    entries = 0
    isSelected = False
    availRecords = False

    if len(employees) > 0:
        entries = 1
        availRecords = True
    
    print("\n======================\nEMPLOYEE TERMINAL\n 1. Create a new employee profile\n 2. View employee data records\n======================\n")
   
    menu = input("======================\nSELECT AN OPTION\n======================\n")
    while (isSelected == False):
        if ((menu < "1") or (menu > "2")):
                menu = input("Incorrect option. Please seclect: \n1. Create a new employee profile\n2. View employee data records\n")
        else:
            while (availRecords == False):
                if menu == "2":
                    menu = input("\nNo records were found. Please use option 1. to create a new record to access this feature!\n")
                elif ((menu < "1") or (menu > "2")):
                      menu = input("Incorrect option. Please seclect: \n1. Create a new employee profile\n2. View employee data records\n")
                else:
                    availRecords = True
            isSelected = True



    
    match menu:
        case "1":
            employeeName = input("Enter your name: ")
            employeeHrsWorked = int(input("Enter your hours worked: "))
            employeeRateOfPay = int(input("Enter your rate of pay: "))
            employeeNumber = input("Enter your employee ID number: ")

            if employeeNumber == "00":
                continue
            else:

                match entries:
                    case 0:
                        employees.append(Employee(employeeName, employeeNumber, employeeHrsWorked, employeeRateOfPay))
                        salary = (employeeHrsWorked * employeeRateOfPay)-((employeeHrsWorked * employeeRateOfPay)*TAX)
                        totalSal += salary
                    case 1:
                        alreadyExists = True
                        while (alreadyExists == True):
                            for employee_ID in employees:
                                if employee_ID.number == employeeNumber:
                                    employeeNumber = input("Employee ID number already being used. Please enter another employee ID number: ")
                                else:
                                    employees.append(Employee(employeeName, employeeNumber, employeeHrsWorked, employeeRateOfPay))
                                    salary = (employeeHrsWorked * employeeRateOfPay)-((employeeHrsWorked * employeeRateOfPay)*TAX)
                                    totalSal += salary
                                    alreadyExists = False
                                    break
        case "2":
            employee_count = len(employees)
            average = totalSal/ employee_count
            print("======================\nWelcome to our Employee data records!\n")
            enteredID = input("======================\nEnter the employee ID:")
            print("======================")

            for employee in employees:
                if employee.number == enteredID:   
                    print(f"\n======================\nName: {employee.name}\nTotal hours worked: {employeeHrsWorked}\nTotal gross salary paid:{employee.salary()}\nThe average salary paid per employee is: {average}\n ======================")
                    input("Press any key to continue!")
                else:
                    print("Employee ID not found!")
                    input("Press any key to continue!")
                continue

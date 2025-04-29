from EmpMenu import menu
from EmpAdd import addemp
from EmpUpdate import updateemp
from EmpView import viewallemployees, viewemployee
from EmpSearch import searchemp
from EmpDelete import deleteemp
while(True):
    try:
        menu()
        ch=int(input("Enter your choice: "))
        match(ch):
            case 1:
                addemp()
            case 2:
                deleteemp()
            case 3:
                updateemp()
            case 4:
                viewemployee()
            case 5:
                viewallemployees()
            case 6:
                searchemp()
            case 7:
                print("Thanks for using this program")
                break
            case _:
                print("\tYour Selection of choice is wrong-try again")
    except ValueError:
        print("\tDon't enter alnums, strs and symbols for Choice-try again")
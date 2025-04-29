#program fro Reading Employee Details and save then File by using Pickling Concept
import pickle
with open("emp.pickle", "ab") as fp:
    while(True):
        print("-"*50)
        #get Emp details from KBD
        empno = int(input("Enter Employee No: "))
        empname = input("Enter Employee Name: ")
        empsalary = float(input("Enter Employee Salary: "))
        empdsg = input("Enter Employee Designation: ")
        print("-"*50)
        #create an empty list and the place the above values
        lst = []
        lst.append(empno)
        lst.append(empname)
        lst.append(empsalary)
        lst.append(empdsg)
        #dump the object in the file as Record
        pickle.dump(lst, fp)
        print("Emp Record Saved in a File")
        print("-"*50)
        ch=input("Do You Want to enter another record? (Yes/No): ")
        if(ch.lower()=="No"):
            print("Thanks for this program")
            break
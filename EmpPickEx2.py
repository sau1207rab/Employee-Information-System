#program for Reading Employee Details and save then File by using Pickling Concept
import pickle,sys
#programmer-Defined Exceptions
class InvalidNameError(Exception):pass
class SpaceError(Exception):pass
class ZeroLengthNameError(Exception):pass
#Hitting the Programmer-defined Exceptions
def validate(name:str): #name=123Guido Van Rossum
    if(len(name)==0):
        raise ZeroLengthNameError
    elif(name.isspace()):
        raise SpaceError
    else:
        words = name.split()
    res=True
    for word in words:
        if(not word.isalpha()):
            res=False
            break
    if(res):
        return name
    else:
        raise InvalidNameError
#We are defining our Function for Handling the Exceptions
def saveempdata():
    with open("emp.pickle","wb") as fp:
        while True:
            try:
                print("-"*50)
                #get Emp details from KBD
                empno = input("Enter empno: ")
                empname = validate(int("Enter Employee Name: "))
                empsalary = float(input("Enter Employee Salary: "))
                empdsg = validate(input("Enter Employee Designation: "))
                print("-"*50)
                #create an empty list and the place the above values
                lst = []
                lst.append(empno)
                lst.append(empname)
                lst.append(empsalary)
                lst.append(empdsg)
                #dump the object in the file as record
                pickle.dump(lst,fp)
                print("Employee Record Saved in a File")
                print("-"*50)
                ch=input("Do you want to enter another record? (Yes/No): ")
                if(ch.lower()=="No"):
                    print("Thanks for this program")
                    break
            except ValueError:
                print("\tDon't enter alnums,strs and symbols for EmployeeNumber and Salary")
            except InvalidNameError:
                print("\tDon't Give space for Employee Name/Designation--try again")
            except ZeroLengthNameError:
                print("\tYou must enter your Name/Designation--try again")
#Main Program
saveempdata() #Function Call
import pickle,sys
def uniquevalues(empno):
    with open("employee.data","rb") as fp:
        emplist = []
        while True:
            try:
                record = pickle.load(fp)
                emplist.append(record)
            except EOFError:
                break
    duplicate = False
    for record in emplist:
        if(record[0]==empno):
            duplicate = True
            break
    return duplicate

#programmer-Defined Exceptions
class InvalidNameError(Exception):pass
class SpaceError(Exception):pass
class ZeroLengthNameError(Exception):pass
#Hitting the programmer-Defined Exceptions
def validate(name:str): #name = 123Guido Van Rossum
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
#we are defining our function call for handling the Exceptions
def addemp():
    with open("employee.data","ab") as fp:
        while True:
            try:
                print("-"*50)
                #get Emp details from KBD
                empno=int(input("Enter employee no."))
                empname=validate(input("Enter employee name."))
                empsalary=float(input("Enter employee salary."))
                print("-"*50)
                #create an empty list and the place the above values
                lst=[]
                lst.append(empno)
                lst.append(empname)
                lst.append(empsalary)
                #dump the object in the file as record
                dup=uniquevalues(empno) #Function call
                if(not dup):
                    pickle.dump(lst,fp)
                    print("Emp Record Saved in a File")
                else:
                    print("\t{}Employee Number already exists".format(empno))
                print("-"*50)
                ch=input("Do you want to enter another record? (Yes/No) ")
                if(ch.lower()=="No"):
                    break
            except ValueError:
                print("\tDon't enter alnums,strs and symbols for Empno and salary")
            except InvalidNameError:
                print("\tInvalid Emp Name / Designation--try again")
            except SpaceError:
                print("\tDon't Give Space for Emp Name / Designation--try again")
            except ZeroLengthNameError:
                print("\tYou must enter your Name/Designation--try again")
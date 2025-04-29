import pickle

from EmpPickEx import empsalary


def updateemp():
    with open("employee.data","rb") as fp:
        #get Employee Number to delete the record
        empno = int(input("Enter Employee Number to : "))
        empname = input("Enter Your Correct Name : ")
        empsalary = float(input("Enter Your New Salary : "))
        #get the record from file
        emplist = []
        while True:
            try:
                record = pickle.load(fp)
                emplist.append(record)
            except EOFError:
                break
    res = False
    for ind in range(len(emplist)):
        if(emplist[ind][0] == empno):
            index = ind
            res = True
            break
    if(res):
        emplist[ind][1] = empno
        emplist[ind][2] = empsalary
        print("Employee Number Updated Successfully")
        with open("employee.data","wb") as fp:
            for record in emplist:
                pickle.dump(record,fp)
        print("Employee Number Updated Successfully")
    else:
        print("Employee Number does not exist -- Can't Update")
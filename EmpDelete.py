import pickle
def deleteemp():
    with open("employee.data","rb") as fp:
        #get Employee Number to delete the record
        empno=int(input("Enter Employee Number to delete: "))
        #Get the Data from the File
        emplist = []
        while (True):
            try:
                record = pickle.load(fp)
                emplist.append(record)
            except EOFError:
                break
    res=False
    for ind in range(0,len(emplist)):
        if(emplist[ind][0]==empno):
            index=ind
            res=True
            break
    if(res):
        emplist.pop(index)
        print("\tEmployee Record Removed--verify")
        with open("employee.data","wb") as fp:
            for record in emplist:
                pickle.dump(record,fp)
    else:
        print("Employee Number does not exist")
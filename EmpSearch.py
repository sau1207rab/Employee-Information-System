import pickle
def searchemp():
    #get employee number from KBD
    empno = int(input("Enter employee number: "))
    #get the data from the file
    emplist = []
    with open("employee.data", "rb") as fp:
        while True:
            try:
                record = pickle.load(fp)
                emplist.append(record)
            except EOFError:
                break
        res = "NotFound"
        for emprec in emplist:
            if(emprec[0] == empno):
                res = "found"
                break
        if(res == "found"):
            print("\t{} Employee number exists".format(empno))
        else:
            print("\t{} Employee number does not exist".format(empno))
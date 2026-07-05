Chkeven= lambda no:(no%2==0)


def main():
    Data=[1,2,3,4,5,6,7,8,9,10]
    print("Input data is :",Data)

    Fdata=list(filter(Chkeven,Data))
    print("Even numbers are",Fdata)
    print("Count of even no is",len(Fdata))
    
if __name__=="__main__":
    main()
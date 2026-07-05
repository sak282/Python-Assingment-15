Chkodd=lambda no:(no%2!=0)


def main():
    Data=[1,2,3,4,5,6,7,8,9,10]
    print("Input data is :",Data)

    Fdata=list(filter(Chkodd,Data))
    print("Data after filter",Fdata)
    
if __name__=="__main__":
    main()
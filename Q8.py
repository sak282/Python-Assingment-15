Divs= lambda no:(no%3==0 and no%5==0)


def main():
    Data=[3,15,30,12,35,5]
    print("Input data is :",Data)

    Fdata=list(filter(Divs,Data))
    print("Data after filter",Fdata)
    
if __name__=="__main__":
    main()
from functools import reduce

Add =lambda no1,no2:no1+no2
    
    


def main():
    Data=[1,2,3,4,5,6,7,8,9,10]
    print("Input data is :",Data)

    Rdata=reduce(Add,Data)
    print("Data after reduce",Rdata)
    
if __name__=="__main__":
    main()
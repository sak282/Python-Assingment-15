from functools import reduce

Min=lambda no1,no2:no1 if no1<no2 else no2
    
    


def main():
    Data=[1,2,3,4,5,6,7,8,9,10]
    print("Input data is :",Data)
    
    
    Rdata=reduce(Min,Data)
    print("Data after reduce, Min num is",Rdata)
    
if __name__=="__main__":
    main()
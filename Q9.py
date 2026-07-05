from functools import reduce
Mul=lambda no1,no2:no1*no2
    
    


def main():
    Data=[1,2,3,4,5,6,7,8,9,10]
    print("Input data is :",Data)

    Rdata=reduce(Mul,Data)
    print("Data afer reduce,Multiplication of number is ",Rdata)
    
if __name__=="__main__":
    main()
Square=lambda no:no*no


def main():
    Data=[2,4,6,8,10]
    print("Input data is :",Data)

    Mdata=list(map(Square,Data))
    print("Data after map,Square of numbers are",Mdata)
    
if __name__=="__main__":
    main()
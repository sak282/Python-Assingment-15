Lstring= lambda x:len(x)>5


def main():
    Data=["Sakshi","Python","Sak","Date"]
    print("Input data is :",Data)

    Fdata=list(filter(Lstring,Data))
    print("Data afet filter",Fdata)
    
if __name__=="__main__":
    main()
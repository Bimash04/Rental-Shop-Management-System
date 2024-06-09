import datetime as dte
import List

def creturn():
    name=input("Enter Renter name: ")
    a="RentBy"+name+".txt"
    try:
        with open(a,"r") as f:
            lines=f.readlines()
            lines=[a.strip("$") for a in lines]
        with open(a,"r") as f:
            info=f.read()
            print(info)
    except:
        print("Enter correct Renter name")
        creturn()

    b="ReturnBill"+name+".txt"
    with open(b,"w+")as f:
        print("------------------------------------------------------")
        print("|            letang rental Shop            |")
        print("------------------------------------------------------")
        
        f.write("Returned By: "+ name+"\n")
        f.write("Date: " + dte.datetime.now().strftime("%y/%m/%d time %H:%M:%S")+ "\n" )
        f.write("S.N.\t\tnameOfCostume\t\tprice\n")

    total=0.0
    
    for i in range(len(List.itemNames)):
        if List.itemNames[i] in info:
            with open(b,"a") as f:
                f.write(str(i+1)+"\t\t\t"+List.itemNames[i]+"\t\t\t$"+List.price[i]+"\n")
                
                List.quantaty[i]=int(List.quantaty[i])+10
                
            total+=float(List.price[i])
     

                        
    print("price of items  is:"+"$"+str(total))
    print("Is the items  return date expired?")
    print("Press Y for Yes and N for No")
    stat=input()
    if(stat.lower()=="y"):
        print("By how many days was the Costume returned late?")
        day=int(input())
        fine=5*day
        with open(b,"a")as f:
            f.write("Fine: $"+ str(fine)+"\n")
        total=total+fine

    print("Final Total: "+ "$"+str(total))
    with open(b,"a")as f:
        f.write("Total: $"+ str(total))
    
        
    with open("stock.txt","w+") as f:
        for i in range(len(List.itemNames )):
                f.write(List.itemNames [i]+","+List.brand[i]+","+str(List.quantaty[i])+","+"$"+List.price[i]+"\n")
from unicodedata import name


def List():
    global itemNames 
    global brand
    global quantaty
    global price

    itemNames=[
        
    ]
    brand=[]
    quantaty=[]
    price=[]

    with open("stock.txt","r") as f:
        lines=f.readlines()
        lines=[x.strip('\n') for x in lines]
        for i in range(len(lines)):
            x=0
            for a in lines[i].split(','):
                if(x==0):
                    itemNames.append(a)
                elif(x==1):
                    brand.append(a)
                elif(x==2):
                    quantaty.append(a)
                elif(x==3):
                    price.append(a.strip("$"))
                x+=1
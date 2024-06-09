import datetime as dt
import List

def Rent():
    rented = False
    
    while True:
        fName = input("Enter First name of customer: ")
        if fName.isalpha():
            break
        else:
            print("Enter your First Name: ")
            
    while True:
        lName = input("Enter last name of Customer: ")
        if lName.isalpha():
            break
        print("Enter your last name")
    
    z = "RentBy" + fName + ".txt"
    with open(z, "w+") as f:
        print("------------------------------------------------------ ")
        print("|          welcome to the letang rental Shop           | ")
        print("------------------------------------------------------ ")

        f.write("------------------------------------------------------- \n")
        f.write("|        -----welcome to the letang  rental Shop-----               | \n")
        f.write("------------------------------------------------------- \n\n")

        f.write(fName + " " + lName + "  Rented the costume at  " + dt.datetime.now().strftime("%y/%m/%d time %H:%M:%S") + "\n")
        f.write("------------------------------------------------------------------------------------------  \n")
        f.write("| S.N. |                Costume Name          |            Brand      |        Price      |  \n")
        f.write("------------------------------------------------------------------------------------------  \n")
        
    while not rented:
        print("Options are available:")
        for i in range(len(List.itemNames)):
            print("Enter", i, "to rent items ", List.itemNames[i])
        
        try:
            sr = True
            while sr:
                a = int(input("Enter the items number : "))
                if a < 0 or a >= len(List.itemNames):
                    print("Invalid number entered")
                else:
                    sr = False

            l = True
            while l:
                b = int(input("How many costumes you want to rent?: "))
                if b < 0 or int(List.quantaty[a]) < b:
                    print("Not enough available stock")
                else:
                    l = False

            if int(List.quantaty[a]) > 0:
                print("The items you selected is available ")
                with open(z, "a") as f:
                    f.write("             " + List.itemNames[a] + "                              " + List.brand[a] + "                           " "$" + List.price[a] + "\n\n")
                
                List.quantaty[a] = int(List.quantaty[a]) - b
                with open("stock.txt", "w+") as f:
                    for i in range(len(List.itemNames)):
                        f.write(List.itemNames[i] + "," + List.brand[i] + "," + str(List.quantaty[i]) + "," + List.price[i] + "\n")
                    
                loop = True
                count = 1
                while loop:
                    choice = input("Do you want to rent more items ? (Y/N): ").lower()
                    if choice == "y":
                        count += 1
                        print("Options are available below:")       
                        for i in range(len(List.itemNames)):
                            print("Enter", i, "to rent items", List.itemNames[i])
                        a = int(input())
                        
                        if 0 <= a < len(List.itemNames) and int(List. quantaty[a]) > 0:
                            c = int(input("How many more do you want to rent?: "))
                            
                            if 0 < c <= int(List. quantaty[a]):
                                print("The selected items  is available.")
                                with open(z, "a") as f:
                                    f.write("             " + List.itemNames[a] + "                              " + List.brand[a] + "                           " "$" + List.price[a] + "\n\n")
                                
                                List. quantaty[a] = int(List. quantaty[a]) - c
                                with open("stock.txt", "w+") as f:
                                    for i in range(len(List.itemNames)):
                                        f.write(List.itemNames[i] + "," + List.brand[i] + "," + str(List. quantaty[i]) + "," + List.price[i] + "\n")
                            else:
                                print("Invalid quantity")
                        else:
                            print("Invalid items  or not available")
                    elif choice == "n":
                        print("Thank you for renting items  from us.")
                        rented = True
                        loop = False
                    else:
                        print("Please choose 'Y' for Yes or 'N' for No.")
            else:
                print("Sorry, the items is not available right  now  . You can Rent other items instead or you can come later on")
                rented = False
        except IndexError:
            print("Please insert according to their given number.")
        except ValueError:
            print("Please choose as per the instruction .")

if __name__ == "__main__":
    Rent()

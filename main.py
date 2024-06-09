from abc import ABC
import List
import rent

import Creturn
from tabulate import tabulate
def main():
    shop = {
        "0":["Eq name","Brand Name","Quantity","price "],
        "1":[],
        "2":[],
        "3":[],
        "4":[],
        "5":[],
        "6":[],
    }
    while(True):
        print("------------------------------------------------------")
        print("|         -----welcome to  letang  rental Shop-----  |")
        print("-----------------------------------------------------")

        print("A. Display available items  .")
        print("B. Renting a items .")
        print("C. Returning a items .")
        print("D. Quit.")

        try:
            char=input("Select a choice from A,B,C and D: ").upper()

            print()
            if(char=="A"):
                with open("stock.txt","r") as f:
                    with open("stock.txt", "r") as f:
                        lines = f.readlines()  # Read lines as a list
                        for i, l in enumerate(lines, start=1):
                            real_line = l.strip().split(",")  # Split each line by comma
                            shop[str(i)] = real_line

                # print(shop)
                table_data = [shop[key] for key in sorted(shop, key=int)]

                # Print the tabulated data
                print(tabulate(table_data, headers="firstrow",tablefmt="pretty"))
                            
   
            elif(char=="B"):
                List.List()
                rent.Rent()
            elif(char=="C"):
                List.List()
                Creturn.creturn()
            elif(char=="D"):
                print("Thank you , keep visiting! ")
            elif(char==""):
                print ("please enter valid character")
                break
            else:
                print("Please enter a valid choice from A, B, C and D")
        except ValueError:
            print("Please input as per the suggestion above.")
main()
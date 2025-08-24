#THIS PROJECT BELONGS TO GAURAV MATHPAL

#!/usr/bin/env python3

import pandas as pd
import csv

def menu():
    print("\n\n--- your personal expense tracker is ready ---\n")

    while(True):
        # main menu for the app, user chooses what action to do
        inp = str(input("\npress: sm for summary, a for adding expense, ed for editing, de for deletion, ex to exit\n> "))

        if(inp=='a' or inp=='A'):
            personalexpensetracker()
        elif(inp=="sm" or inp=="Sm" or inp=="SM"):
            expensesummary()
        elif(inp=="ed" or inp=="Ed" or inp=="ED"):
            expenseedit()
        elif(inp=="de" or inp=="De" or inp=="DE"):
            expensedelete()         
        elif(inp=='ex' or inp=='Ex'):
            print("\nclosing the tracker... goodbye!\n")
            break
        else:
            print("\nplease read the instructions carefully.\n")

def expensedelete():
    # load the file with index column preserved
    df = pd.read_csv("expenses.csv",index_col="index")
    print("\n--- current records ---\n")
    print(df)
    print("\n-----------------------\n")

    indxval = int(input("enter the index value of the row you want to delete:\n> "))

    if(indxval in df.index):
        df.drop(indxval, inplace=True)
        print("\nrow deleted successfully.\n")
        df.to_csv("expenses.csv", index_label="index")
    else:
        print("\nthat row doesn't exist.\n")

def expenseedit():
    # show existing data to help user choose which row to update
    df = pd.read_csv("expenses.csv",index_col="index")
    print("\n--- current records ---\n")
    print(df)
    print("\n-----------------------\n")

    choice = int(input("press 0 to update a single value, 1 to update whole row:\n> "))
    indxval = int(input("enter the index value of the row to update:\n> "))

    if(indxval in df.index):
        if(choice==0):
            colval = str(input("enter the column name you want to update:\n> "))
            updatedvalue=input("enter the new value:\n> ")
            df.at[indxval, colval] = updatedvalue
            print("\nvalue updated.\n")
        elif(choice==1):
            # take fresh values from user and replace the entire row
            date = str(input("updated date: "))
            travel = int(input("updated travel charges: "))
            food = int(input("updated food charges: "))
            accessories = int(input("updated accessories: "))
            miscellaneous = int(input("updated miscellaneous: "))
            moneysenthome = int(input("updated money sent home: "))
            grandtotal = travel+food+accessories+miscellaneous+moneysenthome
            newrecord = {"Date": date, "Travel charges":travel, "Food purchased":food, "Accessories":accessories, "Miscellaneous":miscellaneous, "Money sent home":moneysenthome, "Grand total":grandtotal}
            df.loc[indxval] = newrecord
            print("\nrow updated.\n")
        else:
            print("\nplease enter either 0 or 1.\n")
    else:
        print("\nthat index value doesn’t exist, try again.\n")
    df.to_csv("expenses.csv", index_label="index")

def expensesummary():
    # show summary for either one day or entire data
    df = pd.read_csv("expenses.csv", index_col="index")

    choiceinp = str(input("\ndo you want summary for a specific day? [Y/N]\n> "))

    if(choiceinp.lower() == 'y'):
        try:
            suminp = str(input("\nenter the date (dd-mm-yyyy):\n> "))
            print("\n===== expense summary =====\n")   
            print("\n".join(f"{col}: {row}" for col, row in df.loc[df['Date'] == suminp].iloc[0].items()))
            print("\n===========================\n")
        except:
            print("\nrecord not found.\n")

    elif(choiceinp.lower() == 'n'): 
        print("\n===== full summary =====\n")   
        print(df.to_string(index=False), "\n")
        print("\n========================\n")
        print("\n===== total expenditure =====\n")   
        print(df.sum(numeric_only=True))
        print("\n========================\n")
    
    else:
        print("\nplease enter either Y or N.\n")

def personalexpensetracker():
    # add a new record for today's expenses
    df = pd.read_csv("expenses.csv", index_col="index")
    print("\n--- add new expense ---\n")
    date = str(input("date: "))
    travel = int(input("travel charges: "))
    food = int(input("food charges: "))
    accessories = int(input("accessories purchased: "))
    miscellaneous = int(input("miscellaneous: "))
    moneysenthome = int(input("money sent home: "))
    grandtotal = travel+food+accessories+miscellaneous+moneysenthome
    newrecord = {"Date": date, "Travel charges":travel, "Food purchased":food, "Accessories":accessories, "Miscellaneous":miscellaneous, "Money sent home":moneysenthome, "Grand total":grandtotal}
    newdf = pd.DataFrame([newrecord])
    df = pd.concat([df, newdf], ignore_index=True)
    df.to_csv("expenses.csv", index_label="index")
    print("\nrecord added successfully.\n")

menu()

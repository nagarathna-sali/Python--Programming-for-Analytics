### Problem 4- Solution
####defining menu function
def mypymenu(): #defining menu for MYPY operations
    print("########################")
    print("MYPY PHONE BOOK")
    print("########################")
    print("1: Add New Entry")
    print("2: Delete Entry")
    print("3: Update Entry")
    print("4: Lookup Numbers")
    print("5: QUIT")
    print()
    
mylist={}###intialising the dictionary
menuOpt=0 ####variable to store choice

mypymenu()
while menuOpt != 5:### this function will run until user chooses to quit
    menuOpt=int(input("Choose Option: "))
    if(menuOpt==1):###this will add a entry 
        print("Enter Full Name and Phone Number to add")
        fullName = str(input("Enter Full Name: "))
        phNo = int(input("Enter Phone Number: "))
        if phNo in mylist:###checks whether phone number already exist else adds a record
            print("Phone number already exist")
        else:
            mylist[phNo] = fullName # store key:value set in dictionary
            print("Record Added Successfully")
    elif(menuOpt==2): ###checks a phone number to delete , if phone no not found displays error
        print("Removing a record")
        phNo = int(input("Enter Phone number to remove: "))
        if phNo in mylist:
            del mylist[phNo]
            print("Record deleted successfully")
        else:
            print(phNo, "Phone Number not found")
    elif(menuOpt==3): ###checks a phone number to update , if phone no not found allows user to add a record else updates the existing record
        phNo = int(input("Enter Phone Number to update"))
        if phNo in mylist:
            editpref = input("Want to edit Name or Number?: ")
            if editpref.lower()== "name":
                newfullName = input("Enter new name: ")
                mylist[phNo] = newfullName
                print("Update successful")
            else:
                newPhNo = int(input("Enter new Number: "))
                newfullName = mylist[phNo]
                del mylist[phNo]
                mylist[newPhNo] = newfullName
                print("Update successful")
        else:
            print("Number not found")
       # phNo = int(input("Enter Phone Number: "))
       # fullName = str(input("Enter Full Name: "))
        #mylist[phNo] = fullName
        #print("Record updated successfully")
    elif (menuOpt == 4):####looks up for a phone number displays message accordingly
        if mylist: #if Phonebook is not empty do below operation
            print("Lookup for a phone number")
            phNo = int(input("Enter Phone Number to search: "))
            if phNo in mylist:
                print("Name is ",mylist[phNo])
            else:
                print(phNo,"Phone Number not found")
                pref=input("Do you want to add new record? enter Yes or No")
                if pref.lower()=="yes":
                    print("Enter details to Add a record")
                    phNo = int(input("Enter Phone Number: "))
                    fullName = str(input("Enter Full Name: "))
                    mylist[phNo] = fullName
                else:
                    break;        
        else:
            print("Phonebook is empty")
    elif menuOpt == 5:##### this will exit from the transactions
        ##print("current list",mylist)
        print("Exit")
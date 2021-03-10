print("##################################")
print("WELCOME TO THE DBS CONSOLE")
print("##################################")
test=input("Please enter your username: ")
test1=test.split("/") # splitting the input based on delimiter
str1=test1[0] 
str2=test1[1]
if(str1.isalpha()): #checking if string has alphabet to decicde domain else username
    print("Domain: ",str1.upper())
    print("Username: ",str2.upper())
else:
    print("Domain: ",str2.upper())
    print("Username: ",str1.upper())
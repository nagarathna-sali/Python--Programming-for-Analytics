#Problem 3 - Solution
print("##################################")
print("WELCOME TO THE DBS CONSOLE")
print("##################################")
test=int(input("Input the number of elements to be stored in list: "))#prompt user to enter number of elements they want to store
print("Input",test,"elements in the list:")#print user input 
i=0
mylist=[]#declaring empty list
import collections #importing collections to use counter function
while i<test: #since i starts from zero loop will run till i<test and will input all the integers
    test1=input("element - "+str(i)+" : ")  
    mylist.append(test1) #appending each time to list created
    i +=1 #incrementing i for iterations
my_dict=collections.Counter(mylist)# storing thecount to dictionary 
print("The frequency of all the elements of the list")
for key,value in my_dict.items(): #loop through key ,value  of dictionary by using items() function
    print(key,"occurs", value,"times") #printing occurance of each number
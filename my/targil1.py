##for loops
from time import sleep
#for x in range (1,11):
  #  print(x)
 #   print("wow\n")

#list_yarin=["banna", "apple", "mango"]
#for x in list_yarin:
 #    print(x)

#for x in range (1,11,3):
 #   print(x)
print("Now we will get all the detiales about you class: \n---------------------------\n")
for i in  range (2):
    name=input("Enter a name: ")
    age=int(input("Enter an age: "))
    phone=input("Enter a phone: ")
    print("Printing student number " + str(i+1) + " Details...\n")
    sleep(3)
    print("Full name " + name + "\nage: " + str(age) + "\nphone: " + phone + "\n-----------------------\n")

    print("\nBye Bye! ")
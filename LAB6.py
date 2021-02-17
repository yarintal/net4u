from time import sleep

choise=input("Menu:\n1.Insert a number and ** it by 3\n2.here 4 ip as you ask:\n3.here you're  4 DNS:\n4.Check if a string is Polindrom\n")

if(choise=="1"):
    print("The new number is: " + str((int(input("Enter a number: ")))**3))
elif(choise=="2"):
   list_ip=[]
   list_ip.append(input("Enter new ip: "))
   list_ip.append(input("Enter new ip: "))
   list_ip.append(input("Enter new ip: "))
   list_ip.append(input("Enter new ip: "))
   print("The new list:\n" + str(list_ip))
elif(choise=="3"):
    dns_dict={}
    dns_dict.update({input("Enter a URL: "): input("Enter a ip ")})
    dns_dict.update({input("Enter a URL: "): input("Enter a ip ")})
    dns_dict.update({input("Enter a URL: "): input("Enter a ip ")})
    dns_dict.update({input("Enter a URL: "): input("Enter a ip ")})
    print("The new dns list:\n" + str(dns_dict))
elif(choise=="4"):
    word=input("Enter a word: ")
    if (word == word[::-1]):
        print("This is polindrom!")
    else:
        print("This isn't polindrom!")
else:
    print("You must pick 1-4 only!")
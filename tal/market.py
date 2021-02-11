'''
מטרת הפוריקט:
1. כתיבת תוכנית אשר תקבל סל קניות מבחוץ ותחשב מה העלות שלו:
עגבנייה - 3 ש"ח
מלפפון - 2 ש"ח
קולה - 5 ש"ח
עוף - 20 ש"ח לק"ג
התוכנית תחשב את המחיר לתשלום אחרי מעמ (17%), ללא שארית.
'''

print ("Now we will calculate your marketing:\nPrices:\nCucumber:3NIS\nTomato:2NIS\ncola=5NIS\nA pund of chicken:20NIS\nOur prices generate VAT")
Cucumber=int(input("Enter how much Cucumber do you want to buy? "))
Tomato=int(input("Enter how much Tomato do you want to buy? "))
Cola=int(input("Enter how much Cola do you want to buy? "))
chicken=int(input("Enter how much chicken do you want to buy? "))

print("Summary  of your order:\ntomatos: " + str(Tomato) + "\nCucumber: " + str(Cucumber) + "\nCola: " + str(Cola) + "\nChicken: " + str(chicken))
summary=(Tomato*3) + (Cucumber*2) + (Cola*5) + (chicken*20)
print("you have to pay: " + str(summary) + "NIS without tax")
print("you have to pay: " + str("%.2f" % (summary*1.17)) + "NIS with tax")
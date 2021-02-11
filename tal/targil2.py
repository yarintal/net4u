'''
אלפים=4
מאות=5
עשרות=6
אחדות=7
'''
num=4567
#תרגיל מספר אחד
print("Alafim= " + str(num//1000))

#תרגיל מספר שתיים
print("Meot= " + str(num%1000//100))

#תרגיל מספר שלוש
print("Asarot= " +str((num%100)//10))

#תרגיל מספר ארבע
print("Ahadot= " + str (num%10))
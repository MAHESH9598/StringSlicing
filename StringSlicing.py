"""---------- String Slicing ----------------
**** Slicing Works Only Forword direction****

---> Process of obtaining a part of main string or range of Charecters

 """

s="PYTHON"

print(s[2:5])
print(s[0:3])
print(s[0:5])
print("-------------------------------------------")

print(s[-1:-4]) # no output will come
""" it gives only empty list space/// because slicing works only forword direction """
print("-------------------------------------------")

print(s[-4:-1])
print(s[-6:-3])

print("-------------------------------------------")

print(s[1:100])
"""end value is inavalid but we dont get IndexError in Slicing,it will take up to the last position charector"""
print("-------------------------------------------")
print(s[:5])
print("-------------------------------------------")
print(s[2:])
print("-------------------------------------------")
print(s[:])





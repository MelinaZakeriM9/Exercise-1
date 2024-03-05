unit= input("covert to F or C? ")
deg= float(input("please enter degree "))

if unit == 'c' or unit == 'C':
    deg= (deg-32) *5/9
    print(deg, 'C')
elif unit == "f" or unit =='F':
    deg= deg *9/5 +32
    print(deg, 'F')
else: print("incorrect unit")
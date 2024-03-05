ent= input("Please enter a value: ")

if '.' in ent:
    try: ent= float(ent)
    except: pass
elif ent.isdigit()== True:
    ent=int(ent)
elif ent[0]=='[' and ent[-1]==']':
    ent= list(ent)

print("your entry type is ", type(ent))
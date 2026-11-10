password = input("Enter your password: ") 
Uppercase=0
Lowercase=0
Digit=0
Symbol=0
for i in password:
    if i.isupper():
         Uppercase+=1
    elif i.islower():
         Lowercase+=1
    elif i.isdigit():
         Digit+=1
    elif not i.isalnum() and not i.isspace():
         Symbol+=1
print("Password Length", len(password))
print("Uppercase Letters:", Uppercase)
print("Lowercase Letters:", Lowercase)
print("Digits:",Digit)
print("Symbols:",Symbol)
if len(password) < 8:
     print("weak password")
elif Uppercase>0 and Lowercase>0 and Digit>0 and Symbol>0:
     print("Strong password")
else:
     print("medium password")

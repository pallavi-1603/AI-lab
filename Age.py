age=int(input("Enter your age:"))
if(age<0):
    print("Age cannot be less than 0, please enter the correct age!")
elif(age>0 and age<=12):
    print("You are a child!")
elif(age>12 and age<=19):
    print("You are a teenager!")
elif(age>19):
    print("You are an adult!")
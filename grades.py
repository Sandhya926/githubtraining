a,b,c,d,e=eval(input("Enter the 5 subject marks"))
tot=a+b+c+d+e
per=tot/5.0
if(per>=75):
    print("Distinction")
elif(per>=60):
    print("First class")
elif(per>=50):
    print("Second class")
elif(per>=40):
    print("Pass class")
else:
    print("Fail")

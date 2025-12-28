# Grade Calculator program 

# if: every if means what values we are executing?
# elif: otherwise if.
# else: everything else thta doesn't come under both if and elif.  

name = input("Enter your name please:")
print("Hello" + name)

marks = int(input("Enter your marks please:"))
print(marks)

if marks >= 60:
    print("You have got an A grade.")

elif marks >= 50:
    print("You have gotten a B grade.")

elif marks >= 40:
    print("You have gotten a C grade.")

elif marks >= 30:
    print("You have gotten a D grade.")


else:
    print("You have failed the exam.")

    

 

from random import *
dig1=randint(1,9)
dig2=randint(1,9)
dig3=randint(1,9)
dig4=randint(1,9)
ui=["*","*","*","*"]
print(ui)
x=int(input("Guess a number.. "))
end=0
strikes=0
for i in range(10):
    if x==dig1:
        ui[0]=dig1
        end+=1
    elif x==dig2:
        ui[1]=dig2
        end+=1
    elif x==dig3:
        ui[2]=dig3
        end+=1
    elif x==dig4:
        ui[3]=dig4
        end+=1
    else:
        print("Wrong guess! try again.")
        strikes+=1
    print(ui)
    x=int(input("Guess a number.. "))
print(ui)
print("Congratulations! You won!")
print(f"You had {strikes} strikes.")

x=input("Input: ")
while len(x)<2:
    print("Error!")
    x = input("Input: ")
print(x[:2],x[-2:])

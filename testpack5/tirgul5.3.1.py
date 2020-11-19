a=input("Enter a word of odd length greater than 7: ")
while len(a)<7 or len(a)%2==0:
    print("Error!")
    a=input("Enter a word of odd length greater than 7: ")
b=(len(a)-3)//2
print(a[b:-b])
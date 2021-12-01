first=int(input("Enter the First Limit:"))
last=int(input("Enter the last limit"))

for num in range(first,last + 1):
    if num > 1:
        for i in range(2,num):
            if(num % i == 0):
                print(num)
                break


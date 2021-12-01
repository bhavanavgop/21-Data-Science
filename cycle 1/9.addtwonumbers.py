NumList1 = []
NumList2 = []
total = []

Number = int(input("Please enter the Total Number of List Elements: "))
print("Please enter the Items of a First List   ")
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " % i))
    NumList1.append(value)

print("Please enter the Items of a Second List   ")
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " % i))
    NumList2.append(value)

for j in range(Number):
    total.append(NumList1[j] + NumList2[j])

print("\nThe total Sum of Two Lists =  ", total)
#1
month = ["January", "February", "March", "April", "May", "June", "July", "August",
         "September", "October", "November", "December"]
m = int(input("Enter month number"))

if m in range(1, 13):
    print(month[m-1])
else:
    print("invalid input")
print("\n\n")

#2


def interest(p, n, r):
    return (p*n*r)/100


amount = int(input("Enter principal amount"))
year = int(input("Enter number of year"))
rate = int(input("Enter rate of interest"))

print(interest(amount, year, rate))
print("\n\n")

#3
i = 20
while i <= 25:
    if i == 22:
        i += 1
        continue
    else:
        print(i)
    i += 1
print("\n\n")

#4
j = 20
while j < 30:
    if j == 28:
        break
    else:
        print(j)
        j += 1

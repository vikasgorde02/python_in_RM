n=int(input("Enter a Number="))
temp=n
rev=0
order=len(str(n)) #convert into string and count the integer value
while (n>0):
    digit = n % 10
    rev = rev + digit **order
    n=n // 10
if (rev == temp):
        print("Number is Armstrong")
else:
        print("Number is Not Armstrong")
     
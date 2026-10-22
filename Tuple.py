number=input("Enter a Number=")

list1=[int(x) for x in number.split(",")] #num store x// string num convert into integer num and split and 
print("list1=",list1)
std_tuple=tuple(list1)
print("Tuple=",std_tuple)

# Enter a Number=10,20,30,40,50,60
# list1= [10, 20, 30, 40, 50, 60] //mutable
# Tuple= (10, 20, 30, 40, 50, 60) //unmutable
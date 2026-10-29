number=[1,2,4,5,3,7,9]
even_number=list(filter(lambda x: x%2==0,number)) #filter = same as itis loop 
print("Even Number=",even_number)                   #lambda= using without function name

odd_number=tuple(filter(lambda x: x%2!=0,number)) #tuple= convert in tuple 
print("odd Number=",odd_number)
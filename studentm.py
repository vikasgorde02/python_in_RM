name=(input("Enter Number Student Name=").split())
marks=[]
sname=name
java=int(input("Java mark="))
cpp=int(input("c++ mark="))
python=int(input("python mark="))
Rm=int(input("RM mark="))
marks.append(java)  #add value 
marks.append(cpp)
marks.append(python)
marks.append(Rm)
#total=java,cpp,python, Rm
#print(" Marks in list =",total,)

#list1=[int() for x in total.split(",")] #num store x// string num convert into integer num and split and 
print("Marks in list =",marks)
std_tuple=tuple(marks)
print("marks in Tuple=",std_tuple)
duplicate=[]
for i in set(marks):
    if marks.count(i) > 1:
      duplicate.append(i)
print(f"duplicate marks{duplicate}")
total=marks

higest=max(total)
lowest=min(total)
avg=sum(total) /len(total)

print("higest mark=",higest)
print("lowest mark=",lowest)
print("Avrage mark=",avg)

file=open("stud.text","a") # create automatic file
file.write("student name=\n" +" ".join(sname) )
file.write(f"marks in Tuple= {std_tuple}\n")
file.write(f"duplicate marks= {duplicate}\n")
file.write(f"higest mark= {higest}\n")
file.write(f"lowest mark= {lowest}\n")
file.write(f"Avrage mark= {avg}\n")
print("Data Saved successfully")


file.close()
#o/p=
#Enter Number Student Name=vikas
#Java mark=75
#c++ mark=94
#python mark=50
#RM mark=50
#Marks in list =[75, 94, 50, 50]
#marks in Tuple= (75, 94, 50, 50)
#duplicate marks[50]
#higest mark= 94
#lowest mark= 50
#Avrage mark= 67.25
#Data Saved successfully



    

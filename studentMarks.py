name=(input("Enter Number Student Name="))
marks=[]

java=int(input("Java mark="))
math=int(input("Math mark="))
cpp=int(input("c++ mark="))
python=int(input("python mark="))
Rm=int(input("RM mark="))
marks.append(java)  #add value 
marks.append(math)
marks.append(cpp)
marks.append(python)
marks.append(Rm)
total=java + math + cpp +python + Rm
per = total / 500*100
if java > 40 and  math > 40 and cpp > 40 and python > 40 and Rm >40:
   
    if per >= 75:
        group = "Distinction"
    elif per >= 60 and per < 75:
        group = "A group"
    elif per >= 50 and per < 60:
        group = "B group"
    elif per >= 40 and per < 50:
        group="c group"
else:
    # status = "FAIL" 
    group="FAIL"
print("Student Name =",name)
print("Mark List =",marks)
print("Total Marks =",total)
print("Percantage =",per ,"%")
# print("status = ",status)
print("group = ",group)









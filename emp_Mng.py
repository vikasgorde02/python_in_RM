#Q.2.write a python  program to accep emp name and salary from the user and 
# store the data into a list convert salary into a tuple find emp earning 
# above ahe avg salary, calculate heigst and lowest salary and save the
# reports into a file finally read and display the reports

eno=int(input("Enter Number of Employee="))
emp=[]
sal=[]
j=1
for j in range(eno):
  name=(input(f"Enter the {j+1} Name ="))
  salary=float(input(f"Enter The {j+1} Salary="))
  emp.append(name)
  sal.append(salary)
#print("Name=",emp)
#print("salary=",sal)
sal_tuple=tuple(sal)
#print(sal_tuple)

avg_sal=sum(sal) / len(sal)
#print("Employee Avrahe  Salary =a",avg_sal)
above_avg=[]
for i in range(eno):
  if sal[i] > avg_sal:
    above_avg.append(i)
#print(above_avg)

salary_min=min(sal)
salary_max=max(sal)

file=open("emp_data.txt","a")
file.write(f"Employee Name= {emp}\n")
file.write(f"Employee Salary={sal}\n")
file.write(f"Employee Avrage Salary={avg_sal}\n")
file.write(f"Employee Salary Above Avrage salary={above_avg}\n")
file.close()

file=open("emp_data.txt","r")
print(file.read())
file.close()

#o/p=
#Enter Number of Employee=2
#Enter the 1 Name =vikas
#Enter The 1 Salary=25000
#Enter the 2 Name =omkar
#Enter The 2 Salary=30000
#Employee Name= ['vikas', 'omkar']
#Employee Salary=[25000.0, 30000.0]
#Employee Avrage Salary=27500.0
#Employee Salary Above Avrage salary=[1]


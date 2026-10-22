#f=open("file.text","r") #read
#print(f.read())
#f.close()

#f1=open("file.text","w") #write
#f1.write("Welcome to python\n ")
#f1.close()

#f1=open("file.text","a") #append // add new line
#f1.write("vikas\n")
#f1.write(" python programing language\n")
#f1.close()

#file=open("file03.text","x") # create automatic file
#file.write("This is a New File\n")
#file.close()
#file=open("file03.text","a") # create automatic file
#file.write("This is a New File\n")
#file.write("This is a File\n")
#file.close()

#file=open("file03.text","r")
#print(file.readlines(1))
#file.close()

# f=open("demo1.txt","w+")
# f.writelines(["python","\njava","\nC","\ncpp"])
# #f.close()
# #f=open("demo1.txt","r")
# f.seek(0) #move conseal 1 place to another place
# print(f.read())
# f.close()
#------------------------------------------------------------------------------
# file=open("file04.txt","r")
# lines=file.readlines()
# print(len(lines))
# file.close()

file=open("file04.txt","r")
lines=file.read()
w=lines.split()
count=0
for ws in w:
    count=count+1
print(count)
file.close() 


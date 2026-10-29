list=["ram","sham","Swapnil","vikas","pankaj"]
ch1=input("Enter a Character to check=")
#convert=lambda s: s.upper() 
#check=lambda s,ch1:s.startswith(ch1) 
for i in list:
    print("original list=",i)
    print("String to upper=",i.upper())
    print("String start with ",ch1,':',i.startswith(ch1))

#check=lambda s,list:s.startswith(list)
#print("String Convert into upper case =",up(list))
#print("Check String Start With =",ch1,":",check(list,ch1))

#Enter a Character to check=r
#original list= ram
#String to upper= RAM
#String start with  r : True
#original list= sham
#String to upper= SHAM
#String start with  r : False
#original list= Swapnil
#String to upper= SWAPNIL
#String start with  r : False
#original list= vikas
#String to upper= VIKAS
#String start with  r : False
#original list= pankaj
#String to upper= PANKAJ
#String start with  r : False
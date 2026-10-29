str1=input("enter string=")
ch1=input("Enter a Character to check=")
convert=lambda s: s.upper() #upper=string conver into upper case
check=lambda s,ch1:s.startswith(ch1) #startswith=check char  with first letter same asel tr =true other wise ,false  
print("String Convert into upper case =",convert(str1))
print("Check String Start With =",ch1,":",check(str1,ch1))

# o/p=
#enter string=vikas gorde
#Enter a Character to check=v
#String Convert into upper case = VIKAS GORDE
#Check String Start With = v : True
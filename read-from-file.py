valid = open("test-file.txt","r")
infoun= valid.readlines()
data=[]
for x in infoun:
   data.append(x.split(','))
print(data)
emc=input("Please Enter Your Email")
psc=input("Please Enter Your Password")
identify = False
for line in data:
   if line[0]== emc and line[1]==psc:
       identify = True
       print(line[2],line[3],line[4])
       break
if identify == True:
   print("Welcome")
else:
   print ("Incorrect email or password")

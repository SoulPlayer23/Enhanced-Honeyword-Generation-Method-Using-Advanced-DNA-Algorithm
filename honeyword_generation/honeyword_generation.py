import random

getpass = input("Enter the user passwoerd : ")
no=input("Enter the no of honeyword :")
honey=[]

for i in getpass:
	honey.append(i)


numset=''.join(format(i)for i in range(1,len(getpass)))
for i in range(int(no)-1):
	honeywords=''


	x=random.sample(numset,1)
	#select last n charaters from real password

	for i in range(len(getpass)-int(x[0]),len(getpass)):
		honey[i]=chr(random.randint(33,126))

	for i in honey :

		honeywords+=i
	print(honeywords)
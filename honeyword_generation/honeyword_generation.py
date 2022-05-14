import random

def create_honeywords(password):
	no=10
	honey=[]
	honeyword = [None]*9
	j=0

	for i in password:
		honey.append(i)


	numset=''.join(format(i)for i in range(1,len(password)))
	for i in range(int(no)-1):
		honeywords=''


		x=random.sample(numset,1)
		#select last n charaters from real password

		for i in range(len(password)-int(x[0]),len(password)):
			honey[i]=chr(random.randint(33,126))

		for i in honey :

			honeywords+=i
		honeyword[j] = honeywords
		j = j + 1

	print(honeyword)
	
	return honeyword
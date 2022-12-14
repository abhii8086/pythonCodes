import random

class NumTooLargeError(Exception):
	def __init__(self,msg):
		self.msg=msg
class NumTooSmallError(Exception):
	def __init__(self,msg):
		self.msg=msg
num=random.randint(1,100)
count = 0
while True:
	count+=1
	try:
		inum=int(input("Enter a num"))
	if(inum<num):
		raise NumTooSmallError("Enter a greaer no")
		
	elif(inum>num)
	    raise NumTooLargeError("Enter a small no")
	else:
		break
	except NumTooSmallError as me:
		print(me)
	except NumTooLargeError as me:
		print(me)
	print(f"correctly guessed numner:{num}in guessed{count}")

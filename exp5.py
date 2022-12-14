s1={ x for x in input("enter siring s1: ") }
s2={ x for x in input("enter siring s2: ") }
print(s1,"::",s2)
while 1:
	choice = int(input("\n1.intersection\n2.union\n3.difference\n4.symmetric diffrence\n5.Exit\nEnter your choice"))
	if(choice==1):
		print(s1.intersection(s2))
	elif(choice==2):
		print(s1.union(s2))
	elif(choice==3):
		print(s1.difference(s2))
	elif(choice==4):
		print(s1.symmetric_difference(s2))
	elif(choice==5):
		exit(0)
	else:
		print("Invalid")
	
		

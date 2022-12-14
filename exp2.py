def factorial(number):
	factorial=1 
	for i in range(1,number+1):
		factorial = factorial*i
	print(f"factorial of {number} is {factorial}")

def palindrome(string):
	if(string==string[::-1]):
		print("string is palindrome")
	else:
		print("not palindrome")
		
while 1:
	choice = int(input("\n1 factorial\n2 palindrome\n3 Exit\n\n Enter your choice  "))
	if (choice ==1):
		number = int(input("Eneter a no: "))
		factorial(number)
	elif (choice ==2):
		a_string=input("Enter a string: ")
		palindrome(a_string)
	elif (choice == 3):
		 exit(0)
	else:
		print("inavlid choice")

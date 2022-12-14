import sys
                       # for[0] itself script/file name so we didn't use it
a = int(sys.argv[1])   # for accepting first argument
b = int(sys.argv[2])   #for accepting second argument

print("Value before swaping:")
print("a=",a)
print("b=",b)

a=a+b
b=a-b
a=a-b

print("Value After swaping:")
print("a=",a)
print("b=",b)

if (a>0):
	print(a,"is Positive")
elif (a<0):
	print(a,"is Negative")
else:
	print(" no is Zero")
	





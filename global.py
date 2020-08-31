x = 99;
y = 90;
def adding():
	x = 22

adding()	

print x
# prints the global x made in the adding method, not the new local x

def adding2():
	global y;
	y = 11

adding2()
 
print y
#prints the local x. By saying global y, you are telling the program that the y in y = 11 is not a new variable,
#but rather the global one
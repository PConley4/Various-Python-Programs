def callbyname(a,b):
	print a,b


def defaultname(c="chu",d="pi"):
	#here the parameters are set before the method call. Thus, if the method call does not assign values to the variables,
	#these will act as the defaults.
	print c,d

	
callbyname(b="chu", a="pika")
#if the values aren't input then null is printed
	
defaultname()
#prints the default
defaultname(d="rai")
#prints the default c and the given d.
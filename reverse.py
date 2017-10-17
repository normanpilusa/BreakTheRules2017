#Reverses a string
def reverse(str):
	
	#Null input
	if str == None:
		return ""
	elif len(str) < 2:
		return str
	else:
		reversed = ""
		
		for word in str.split(" "):
			reversed = word + " " +reversed 
		
		return reversed
		
if __name__== '__main__':
	print reverse("The rain in Spain stays mainly in the plain")
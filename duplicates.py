#Removes duplicates in a string
def remove(str):
	current = ""
	output = ""
	
	#Check for null inputs
	if str != None :
		current = str[0:1] 
		output += current
	else:
		return current
		
	#Remove subsequent duplicates
	for character in str:
		if character != current:			
			current = character
			output += current
	
	#return the final string
	return output
			
			
if __name__=='__main__':
	print remove("bbbbbbrrrrrreakk")
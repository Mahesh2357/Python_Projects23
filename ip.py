# Python3 implementation to find the
# defanged version of the IP address

# Function to generate a
# defanged version of IP address.
def GeberateDefangIP(str):

	defangIP = "";
	
	# Loop to iterate over the
	# characters of the string
	for c in str:
		if(c == '.'):
			defangIP += "[.]"
		else:
			defangIP += c;
	return defangIP;

# Driver Code
str = "255.100.50.0";
print(GeberateDefangIP(str));

# This code is contributed by Nidhi_biet

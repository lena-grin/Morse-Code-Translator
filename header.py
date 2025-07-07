table =  {        '.-': 'A', 
		'-...': 'B', 
		'-.-.': 'C', 
		'-..' : 'D', 
		'.'   : 'E', 
		'..-.': 'F', 
		'--.' : 'G', 
		'....': 'H', 
		'..'  : 'I', 
		'.---': 'J', 
		'-.-' : 'K', 
		'.-..': 'L', 
		'--'  : 'M', 
		'-.'  : 'N', 
		'---' : 'O',
		'.--.': 'P',
		'--.-': 'Q',
		'.-.' : 'R', 
		'...' : 'S', 
		'-'   : 'T', 
		'..-' : 'U', 
		'...-': 'W', 
		'-..-': 'X', 
		'-.--': 'Y', 
		'--..': 'Z', 
		'.----': '1', 
		'..---': '2', 
		'...--': '3', 
		'....-': '4', 
		'.....': '5', 
		'-....': '6', 
		'--...': '7', 
		'---..': '8', 
		'----.': '9', 
		'-----': '0', 
		'.......': ' ', 
		'...----.--.': '\n'}


#searches table for input, returns value of the key
def lookup(input):
	for item in table:
		if item == input:
			return table[item]
			break
	else:
		return "error"
	
#takes in a list, converts it to a string, returns the index where the substring STOP is found
def where_stop(input):
	return ''.join(input).find(' STOP ') 

#takes a value and a dictionary; returns the key corresponding to that value in it. otherwise returns None
def getkey(value, dictionary):
	for item in dictionary:
		if value.upper() == dictionary[item]:
			return item
			break
	else: 
		print(value,':'+ 'no key found!')
		
	

#takes in a string of morse code, outputs it in uppercase characters. 'STOP' is interpreted as line breaks
def decode(input): 
    input = input.split(' ')
    M = []
    for i in range(len(input)):
        M.append(lookup(input[i]))

    while where_stop(M) != -1:
        n = where_stop(M)
        M[n:n+6] = '\n'

    M = ''.join(M)
    return M

#takes in a string of text, outputs it in morse code
def encode(input): 
	output = []
	for item in input:
		output.append(getkey(item,table))
	output = ''.join(output)
	return output
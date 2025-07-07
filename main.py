from header import decode
from header import encode
text = open('input.txt','r').read()
print(text)
output = decode(text)
print(output)

recoded = encode('stop')
print(recoded)
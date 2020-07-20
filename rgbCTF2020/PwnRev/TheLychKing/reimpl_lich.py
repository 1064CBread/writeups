img = "./lich"

fh = open('./cipher', 'rb')
goal = bytearray(fh.read())

fh = open('./uncipher', 'rb')
other = bytearray(fh.read())


def revDig(num):
	rev_num=0
	while (num > 0):
		rev_num = rev_num*10 + num%10
		num = num//10
	return rev_num

# Function to check whether the number is palindrome or not
def isPalindrome(num):
	return (revDig(num) == num)

def getPad(seed):
	res = ""
	while not isPalindrome(seed) and len(res) < 1000:
		res += str(seed)
		seed += revDig(seed)
	return res

def xor_b_str(a,b):
	xored = []
	for i in range(min(len(a), len(b))):
		xored_value = a[i%len(a)] ^ ord(b[i%len(b)])
		xored.append(chr(xored_value))
	return ''.join(xored)

for seed in range(0,2000):
	pad = getPad(seed)
	#print(pad)
	out = xor_b_str(goal, pad)
	print(seed)
	print(out)
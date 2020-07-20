import subprocess
import string
import random

img = "./itwk.so"

goal = [117, 148, 123, 5, 54, 9, 61, 234, 45, 4, 2, 40, 88, 111, 65, 65, 46, 23, 114, 110, 102, 148, 136, 123, 30, 5, 214, 231, 225, 255, 239, 138, 211, 208, 250, 232, 178, 187, 171, 242, 255, 30, 39, 19, 64, 17, 40, 29, 13, 27]
#goal = [114, 20, 119, 59, 104, 47, 75, 56, 81, 99, 23, 71, 56, 75, 124, 31, 65, 32, 77, 55, 103, 31, 96, 18, 76, 41, 27, 122, 29, 47, 83, 33, 78, 59, 10, 56, 15, 34, 94]

query = 'rgbCTF{th1s_pr0bably_w@s_d1ff1cult6362_aaabbbcccd}'
matchingNow = 0

while True:

	flipper = random.randrange(0,len(query))
	sub = random.choice(string.printable)
	trial = query[0:flipper] + sub + query[flipper+1:]

	result = subprocess.Popen([img,  trial], universal_newlines=True, stdout=subprocess.PIPE)
	arr = eval(result.stdout.readlines()[0].strip())
	matchingTrial = 0
	while(arr[matchingTrial] == goal[matchingTrial]):
		matchingTrial += 1

	if matchingTrial > matchingNow:
		query = trial
		matchingNow = matchingTrial
		print("Built ",query)
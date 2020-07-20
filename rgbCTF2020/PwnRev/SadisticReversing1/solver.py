import subprocess
import string
import random

img = "./itJX.so"

goal = [114, 20, 119, 59, 104, 47, 75, 56, 81, 99, 23, 71, 56, 75, 124, 31, 65, 32, 77, 55, 103, 31, 96, 18, 76, 41, 27, 122, 29, 47, 83, 33, 78, 59, 10, 56, 15, 34, 94]

query = ''
matchingNow = 0

while True:

	sub = random.choice(string.printable)
	trial = query + sub

	result = subprocess.Popen([img,  trial], universal_newlines=True, stdout=subprocess.PIPE)
	arr = eval(result.stdout.readlines()[0].strip())
	matchingTrial = 0
	if(arr == goal[0:len(arr)]):
		query = trial
		matchingNow = matchingTrial
		print("Built ",query)
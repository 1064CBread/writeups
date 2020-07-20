playfile = open('play', 'r')
playlines = playfile.readlines()

numfile = open('some_numbers.txt', 'r')

secretmessage = ""

for line in numfile.readlines():
    coords = line.strip().split(",")
    print(playlines[int(coords[0])][int(coords[1])])
    secretmessage += playlines[int(coords[0])][int(coords[1])]

print(secretmessage)    

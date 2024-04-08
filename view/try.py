score = 200
f = open("hs.txt", "r")
highscore_value = int('f.read()')
print(highscore_value)


f = open("hs.txt", "w")
f.write(str(highscore_value))
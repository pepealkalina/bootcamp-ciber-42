import os

i = 1

while i <= 100:
    j = 1
    while j <= 100:
        os.system("./corsair si/{0}.pem si/{1}.pem si/{0}.bin".format(i, j))
        j += 1
    i += 1
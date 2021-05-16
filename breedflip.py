inputData = open("breedflip.in", "r")
outputData = open("breedflip.out", "w")

n = inputData.readline()
n = int(n)
strA = inputData.readline()
strB = inputData.readline()

ret = 0
mismatched = False

for i in range(n):
 if (strA[i] != strB[i]):
   if (not mismatched):
     mismatched = True
     ret = ret + 1
 else:
   mismatched = False   
      
print(ret)
outputData.write("{}\n".format(ret))
inputData.close()
outputData.close()

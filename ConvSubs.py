x = 0
myList= []
myListNumber = []
myListTime = []
myListWords = []
result = []

with open("/home/sam1206morfey/.ssh/converterSubtitles/ConverterSubtitles/1.txt", "r") as file1:
    for line in file1:
        myList.append(line)
        number = int(myList.index(line)) + 1
        myListNumber.append(number)

        if number % 2 == 0:
            print('Четное число')
            myListWords.append(line)

        else:
            print('Нечентное число')
            myListTime.append(line.split())

try:
    while True:
        num = myListNumber[x]
        result.append(num)

        stringTime = "00:" + str(myListTime[x])[2:-2] + ",001" + " --> " + "00:" + str(myListTime[x + 1])[2:-2] + ",001"
        result.append(stringTime)

        myWords = str(myListWords[x])
        result.append(myWords)
        
        x = x + 1

except:
    result = result[:-1]
    print("Конец!")

print(result)


f = open("1138.srt", 'w')
for item in result:
    f.write("%s\n" % item)
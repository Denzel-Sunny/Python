inputFile = "data_file.txt"

readFile = open(inputFile, "r")

outputFile = "PrintOddLines.txt"

writeFile = open(outputFile, "w")

ReadFileLines = readFile.readlines()

for excelLineIndex in range(0, len(ReadFileLines)):


   if(excelLineIndex % 2 != 0):

      writeFile.write(ReadFileLines[excelLineIndex])

      print(ReadFileLines[excelLineIndex])


writeFile.close()
readFile.close()
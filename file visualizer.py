import os

def analyzeFile(fileName):
    returnToBaseFilePath()
    try:
        os.chdir("tests")
    except:
        print("tests folder could not be found!")
        return
    file = open(fileName)
    returnToBaseFilePath()
    try:
        os.chdir("output")
    except:
        os.mkdir("output")
        os.chdir("output")
    try:
        os.chdir(fileName + "Output")
    except:
        os.mkdir(fileName + "Output")
        os.chdir(fileName + "Output")
    outputFile = open("outputFile.txt", "w")
    candidate0 = open("candidate0.txt", "w")
    candidate1 = open("candidate1.txt", "w")
    candidate2 = open("candidate2.txt", "w")
    candidate3 = open("candidate3.txt", "w")
    candidate4 = open("candidate4.txt", "w")
    candidate5 = open("candidate5.txt", "w")
    candidate6 = open("candidate6.txt", "w")
    candidate7 = open("candidate7.txt", "w")
    pattern = open("pattern.txt", "w")
    outputString = ""
    patternOrCandidateNumber = 0
    counter = 0
    listOfStrings = ["","","","","","","","","","","",""]
    stringListCounter = 0
    for line in file:
        line = line.split(":")[1]
        line = line.strip()
        outputString += line +", "
        counter += 1
        if counter % 12 == 0:
            listOfStrings[stringListCounter] = listOfStrings[stringListCounter] + outputString
            outputString = outputString[:-2]
            outputString += "\n"
            if patternOrCandidateNumber == 0:
                candidate0.write(outputString)
            elif patternOrCandidateNumber == 1:
                candidate1.write(outputString)
            elif patternOrCandidateNumber == 2:
                candidate2.write(outputString)
            elif patternOrCandidateNumber == 3:
                candidate3.write(outputString)
            elif patternOrCandidateNumber == 4:
                candidate4.write(outputString)
            elif patternOrCandidateNumber == 5:
                candidate5.write(outputString)
            elif patternOrCandidateNumber == 6:
                candidate6.write(outputString)
            elif patternOrCandidateNumber == 7:
                candidate7.write(outputString)
            elif patternOrCandidateNumber == 8:
                pattern.write(outputString)
            outputString = ""
            stringListCounter += 1
        if counter == 144:
            counter = 0
            patternOrCandidateNumber += 1
            stringListCounter = 0
    for string in listOfStrings:
        string = string[:-2] + "\n"
        outputFile.write(string)
    file.close()
    outputFile.close()
    candidate0.close()
    candidate1.close()
    candidate2.close()
    candidate3.close()
    candidate4.close()
    candidate5.close()
    candidate6.close()
    candidate7.close()
    pattern.close()

def analyzeAllFiles():
    filesSuccessfullyAnalyzed =[]
    for fileName in os.listdir():
        returnToBaseFilePath()
        try:
            os.chdir("tests")
        except:
            print("tests folder could not be found!")
            return
        if ".txt" in fileName:
            try:
                analyzeFile(fileName)
                filesSuccessfullyAnalyzed.append(fileName)
            except:
                print("Failed to analyze " + fileName)

    print("Files successfully analyzed:")
    for fileName in filesSuccessfullyAnalyzed:
        print(fileName)

def returnToBaseFilePath():
    while True:
        if "output" in os.getcwd():
            os.chdir("..")
        elif "tests" in os.getcwd():
            os.chdir("..")
        else:
            break

os.chdir("tests")
while True:
    print(os.listdir())
    fileName = input("What test file would you like to analyze? Alternatively type all to analyze all .txt files in the test folder. \n")
    if "all" in fileName:
        analyzeAllFiles()
        break
    else:
        try:
            analyzeFile(fileName)
            break
        except:
            print("Failed to open file. Please try again.")

print("Done!")

input("Press enter to close terminal window")

    
    
        
    
    

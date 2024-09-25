# Description:
# Read data from a CSV (comma-separated value) file and write data to another file.
# Practice defining and calling functions and working with lists.

# Open the CSV file and get the header row with the languages and return it as list
#
# Input parameter: fileName the opening file name, default is languages.csv
# Output value: the language list
def getAllLanguages(fileName='languages.csv'):
    # Open file
    langurageList = []
    readFile = open(fileName, 'r')
    line = readFile.readline()  # read 1st line
    langurageList = line.strip().split(",")
    print(langurageList)
    readFile.close()
    return langurageList


# Read csv file and get all word list corresponding to the special language
#
# Input parameter: languagesList The language list
# Input parameter: languageStr A string of containing the name of a language and it has a default value of "English"
# Input parameter: fileName a string containing the name of a CSV file to read from
#                  and it has a default value of "languages.csv"
# Output value: a list of words in the language identified by the languageStr parameter
def readDataFile(languagesList, languageStr='English', fileName='languages.csv'):
    idx = languagesList.index(languageStr)
    # Open file
    langurageList = []
    readFile = open(fileName, 'r')
    lineNum = 1
    while True:
        line = readFile.readline()
        if not line:  # end of file
            break
        if (lineNum == 1):  # skip the head line
            lineNum += 1
            continue
        lineList = line.strip().split(",")
        langurageList.append(lineList[idx])
        lineNum += 1

    readFile.close()
    return langurageList

# Display to the user the languages that are available for translation,
# which are all of the languages in languagesList parameter except English.
#
# Input parameter: languagesList A list of the languages
# Output value: Return the language such that the first letter is capitalized and the remaining letters are lower case.
def getTranslationLanguage(languagesList):
    excludeEnglishLangList = languagesList[1::1]  # skip 1st column english
    print("Translate English words to one of the following languages:")
    # print(excludeEnglishLangList) # debug
    while (True):
        inputLang = input("Enter a language: ")
        if inputLang in excludeEnglishLangList:
            return inputLang.title()
        else:
            print("This program does not support " + inputLang)


# Create a text file and write a text into it.
#
# Input parameter: language is a string containing the name of the language for translation
# Output value: none
def createTextFile(language):
    fileName = language + ".txt"
    f = open(fileName, 'w')
    f.write("Words translated from English to " + language + "\n")
    f.close()

# Translate words and save it into file.
#
# Input parameter: englishList is a list of words in English
# Input parameter: translationList is a list of words in another language (not English)
# Input parameter: language is a string containing the language of the words in the translationList
# Output value: none
def translateWords(englishList, translationList, language):
    fileName = language + ".txt"
    f = open(fileName, 'a')
    while (True):
        inputEngWord = input("Enter a word to translate:")
        if (inputEngWord in englishList):
            indexInEngList = englishList.index(inputEngWord)
            translationWord = translationList[indexInEngList]
            if (translationWord == "-"):
                print(inputEngWord + " did not have a translation ")
            else:
                print(inputEngWord + " is translated to " + translationWord)
                f.write(inputEngWord + "=" + translationWord + "\n")
        else:
            print(inputEngWord + "is not in the English list.")
        anotherWord = input("Another word (y or n)?")
        if (anotherWord.lower() == 'n'):
            break
    f.close()


def main():
    print("Language Translator")
    languages = getAllLanguages()
    # print(languages) # debug
    englishList = readDataFile(languages)
    translateLang = getTranslationLanguage(languages)
    translationList = readDataFile(languages, translateLang)
    # print(translationList) # debug
    createTextFile(translateLang)
    translateWords(englishList, translationList, translateLang)


main()

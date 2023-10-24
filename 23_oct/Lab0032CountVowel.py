#Count vowels and consonants in a String

name=input("Enter your name : ")

vowels=set("aAeEiIoOuU")
def countVowel(name):
    countV = 0
    countC = 0
    for i in name:
        if i in vowels:
            countV+=1
        else:
            countC+=1

    print("Total Vovels : ", countV)
    print("Total Constants : ", countC)

countVowel(name)
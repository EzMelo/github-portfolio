

text = input("Please enter your sentence: ")
senList = text.split(' ')
wordCount = len(senList)
print(senList)
if wordCount >= 5:
    print(wordCount)
    print(*senList)
    senList.reverse()
    print(*senList)
else:
    print("You have", str(wordCount), "words in your sentence. \nYour sentence must at least have 5 words")


# wordCount = len(senList)
    # print(wordCount)
    # if wordCount > 5:
     #   print(senList)
      #  break




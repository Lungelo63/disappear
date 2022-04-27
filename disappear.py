#Taking users sentence
sentence = input("Enter a sentence: ")
remove = input("Enter letters you'd like to be removed: ")  #taking user letters to be removed

for x in remove:                                            #for loop to remove more than one of the same letter
    sentence = sentence.replace(x, " ")                     #replacing
    print(sentence)                                         #printing new statement
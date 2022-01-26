# take any text file form of English dictionary and name it "dictionary.txt"
with open("dictionary.txt", "r", encoding = "utf-8") as f:
    text = f.read().lower()
    length = 5

    chars = "aw"

    first = []
    second = []
    third = []

    # positively select for correct placement
    word = " wha** "
    for i in range(0,len(text)):
        p = True
        for j in range(0, len(word)):
            if word[j] == text[j+i]:
                pass
            elif word[j] == "*" and text[j+i].isalpha():
                pass
            else:
                p = False
                break
        if p:
            first.append(text[i+1:i+len(word)-1])

    # negatively select against wrong placement
    word = "*a*a*"
    for i in first:
        p = True
        for j in range(0, len(i)):
            if word[j] == i[j]:
                p = False
                break
        if p:
            second.append(i)
            
    # filter words without possible characters "chars"
    for i in second:
        p = True
        for j in chars:
            if j in i:
                pass
            else:
                p = False
                break
        if p and i not in third:
            third.append(i)

    # print all unique possible words
    for i in third:
        print(i)
        

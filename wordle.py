# take any text file form of English dictionary and name it "dictionary.txt"
with open("dictionary.txt", "r", encoding = "utf-8") as f:
    text = f.read().lower()
    length = 5

    chars = "floy"

    first = []
    second = []
    third = []

    # positively select for correct placement
    word = "*o**y"
    for i in range(0,len(text)):
        p = True
        
        try:
            if text[i-1].isalpha():
                continue
            if text[i+5].isalpha():
                continue
        except:
            continue
        
        for j in range(0, len(word)):
            if word[j] == text[i+j]:
                pass
            elif word[j] == "*" and text[i+j].isalpha():
                pass
            else:
                p = False
                break
        if p:
            first.append(text[i:i+len(word)])

    # negatively select against wrong placement
    words = ["serai", "phon*", "m*mm*", "b*gg*", "r*wd*", "f*ll*"]
    for i in first:
        p = True
        for j in words:
            for k in range(0, len(i)):
                if j[k] == i[k]:
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
        

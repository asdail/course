def letter_replace(word,let,index):
    "Replaces a letter in a word in a certain index"
    d1={}
    count=-1
    newword=""
    word=str(word)
    let=str(let)
    for i in word:
        count+=1
        d1.update({count:i})
    d1[index]=let
    for c in d1.values():
        newword+=c
    word=newword
    return word
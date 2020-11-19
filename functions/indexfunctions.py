def str_indexnum(word,index):
    "Takes a word and a letter and returns the index number in that word."
    d1={}
    let=-1
    for i in word:
        let+=1
        d1.update({i:let})
    return (d1[index])
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
def str_index(word,index):
    "Takes a word and an index number in a word and returns the letter that's in that index"
    d1={}
    let=-1
    for i in word:
        let+=1
        d1.update({let:i})
    return (d1[index])
def str_indexdict(word):
    "Takes a word and an index number in a word and returns the letter that's in that index"
    d1={}
    let=-1
    for i in word:
        let+=1
        d1.update({let:i})
    return d1
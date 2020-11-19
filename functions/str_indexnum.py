def str_indexnum(word,index):
    "Takes a word and a letter and returns the index number in that word."
    d1={}
    let=-1
    for i in word:
        let+=1
        d1.update({i:let})
    return d1[index], d1
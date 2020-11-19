def str_indexdict(word):
    "Takes a word and an index number in a word and returns the letter that's in that index"
    d1={}
    let=-1
    for i in word:
        let+=1
        d1.update({let:i})
    return d1
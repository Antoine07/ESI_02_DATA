phrase = [1,3,7,8,9,1,2,3,8, 1, 2, 3, 7, 8, 9, 1, 2, 3, 8, 10, 1, 2, 3]
word  = [1, 2, 3]

def search_pos(word, phrase):
    lWord = len(word)
    lPhrase = len(phrase)
    s = {}

    for i in range( lPhrase - lWord + 1):
        k = 0
        for j in range( lWord ):
            if  phrase[j + i] == word[j] :
                k += 1

        if k == lWord:
            s['pos'] = i 
            s['word'] = word
            break

    return s

print(search_pos(word, phrase))
    
def search_pos_all(word, phrase):
    lWord = len(word)
    lPhrase = len(phrase)
    s = {'pos': []}

    for i in range( lPhrase - lWord + 1):
        k = 0
        for j in range( lWord ):
            if  phrase[j + i] == word[j] :
                k += 1

        if k == lWord:
            s['pos'].append(i)
            

    return s
   
print(search_pos_all(word, phrase))


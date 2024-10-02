def single_root_words(root_word, *other_words):
    same_words = []
    rw =root_word.lower()
    for ww in other_words:
       if rw in ww :
           same_words.append(ww)
       elif ww.lower() in rw.lower():
           same_words.append(ww)
    return same_words
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
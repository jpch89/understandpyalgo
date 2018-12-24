def find_anagrams(words):
    words_pair = zip(words, [str(sorted(w)) for w in words])
    res_dict = {}
    for i, j in words_pair:
        res_dict.setdefault(j, [])
        res_dict[j].append(i)
    return list(res_dict.values())


words = ['cars', 'thing', 'scar', 'dog', 'god', 'arcs', 'the']
res = find_anagrams(words)
print(res)

"""
[['cars', 'scar', 'arcs'], ['thing'], ['dog', 'god'], ['the']]
"""

def repalce_words(d, sentence):
    s = sentence.split(' ')
    for item in d:
        for i in range(len(s)):
            n = len(item)
            if item == s[i][:n]:
                s[i] = item
    return ' '.join(s)

d = ['cat', 'bat', 'rat']
sentence = 'the cattle was rattled by the battery'
print(repalce_words(d, sentence))

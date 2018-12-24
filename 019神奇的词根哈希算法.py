from collections import defaultdict


def replace_words(d, sentence):
    # dic 是词根的字典
    # 值是一个集合，保存以同一个首字母开始的词根
    dic = defaultdict(set)
    s = defaultdict(int)
    sentence = sentence.split()

    # d 是词根的列表
    for w in d:
        print(w[0])
        # 注意这一句的 add 来自于集合的 add
        dic[w[0]].add(w)
        s[w[0]] = max(s[w[0]], len(w))

    for i, w in enumerate(sentence):
        for j in range(s[w[0]]):
            if w[:j + 1] in dic[w[0]]:
                sentence[i] = w[:j + 1]
                break

    return ' '.join(sentence)


d = ['cat', 'bat', 'rat']
sentence = 'the cattle was rattled by the battery'
print(replace_words(d, sentence))

"""
c
b
r
the cat was rat by the bat
"""

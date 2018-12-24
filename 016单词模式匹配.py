def match_pattern(word_pattern, target):
    if len(target) != len(word_pattern):
        return False

    d = {}
    used = {}

    for i in range(len(word_pattern)):
        # 已经记录过的模式字符串
        if word_pattern[i] in d:
            if d[word_pattern[i]] != target[i]:
                return False
        # 没有记录过的模式字符串
        else:
            # 没有记录过的模式字符串
            # 对应的目标字符串已经被匹配
            # 这样就出现了一个模式对应多个目标的情况
            # 返回 False
            if target[i] in used:
                return False
            d[word_pattern[i]] = target[i]
            used[target[i]] = True
    return True


word_pattern = ['一', '二', '二', '一']
t1 = ['苹果', '香蕉', '香蕉', '苹果']
t2 = ['香蕉', '苹果', '苹果', '香蕉']
t3 = ['我', '我', '我', '我']

print(match_pattern(word_pattern, t1))
print(match_pattern(word_pattern, t2))
print(match_pattern(word_pattern, t3))
"""
True
True
False
"""

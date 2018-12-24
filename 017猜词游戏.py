def get_hint(secret, guess):
    A = 0
    B = 0
    secretd = {}
    guessd = {}

    for i in range(len(guess)):
        if guess[i] == secret[i]:
            A += 1
        else:
            guessd.setdefault(guess[i], 0)
            guessd[guess[i]] += 1
            secretd.setdefault(secret[i], 0)
            secretd[secret[i]] += 1

    for letter in guessd:
        if letter in secretd:
            B += min(guessd[letter], secretd[letter])

    return str(A) + 'A' + str(B) + 'B'


hint = get_hint('hello', 'holla')
print(hint)

"""
3A1B
"""

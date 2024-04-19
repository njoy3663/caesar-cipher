alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def encrypt(word, n):
    global alphabet
    wordIndex = 0
    for i in word:
        alphIndex = 0
        for letter in alphabet:
            if i == letter:
                break
            alphIndex += 1
        alphIndex += n
        if alphIndex == 23:
            alphIndex = 0
        elif alphIndex == 24:
            alphIndex = 1
        elif alphIndex == 25:
            alphIndex = 2
        word[wordIndex] = alphabet[alphIndex]
        wordIndex += 1
    return word

word = input("type encryoptec poisesage")
encryption = encrypt(word, 4)
print(encryption)
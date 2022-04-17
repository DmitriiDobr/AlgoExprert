"""
CaesarCipherEncryptor
"""
def caesarCipherEncryptor(string, key):
    alphabet_idx =  {idx: letter for idx, letter in enumerate(list('abcdefghijklmnopqrstuvwxyz'))}
    alphabet_letter =  {letter: idx for idx, letter in enumerate(list('abcdefghijklmnopqrstuvwxyz'))}
    length = len(alphabet_idx)
    my_string = list(string)
    empty_str = ''
    for idx in range(len(my_string)):
        idx_alphabet = alphabet_letter.get(my_string[idx])
        if (idx_alphabet +key) % length == 0:
            empty_str+=alphabet_idx.get(0)
        else:
            empty_str+=alphabet_idx.get((idx_alphabet+key) % length)
    return empty_str


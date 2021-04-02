ROTOR_DICT = {
    0: "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    1: "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
    2: "AJDKSIRUXBLHWTMCQGZNPYFVOE",
    3: "BDFHJLCPRTXVZNYEIWGAKMUSQO",
    4: "ESOVPZJAYQUIRHXLNFTGKDCMWB",
    5: "VZBRGITYUPSDNHLXAWMJQOFECK",
    6: "JPGVOUMFYQBENHZRDKASXLICTW",
    7: "NZJHGRCXMYSWBOUFAIVLPEKQDT",
    8: "FKQHTLXOCBJSPDZRAMEWNIUYGV",
    "beta": "LEYJVCNIXWPBQMDRTAKZGFUHOS",
    "gamma": "FSOKANUERHMBTIYCWLQPZXVGJD",
}

REFLECTORS = {
    "A": "EJMZALYXVBWFCRQUONTSPIKHGD",
    "B": "YRUHQSLDPXNGOKMIEBFZCWVJAT",
    "C": "FVPJIAOYEDRZXWGCTKUQSBNMHL",
    "B Thin": "ENKQAUYWJICOPBLMDXZVFTHRGS",
    "C Thin": "RDOBJNTKVEHMLFCWZAXGYIPSUQ",
}

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

ROTOR_MOVES = {
    0: [],
    1: [ 17 ],
    2: [ 5 ],
    3: [ 22 ],
    4: [ 10 ],
    5: [ 0 ],
    6: [ 0, 13 ],
    7: [ 0, 13 ],
    8: [ 0, 13 ]
}

ROTOR_LOOP = {}
for rotor in ROTOR_DICT:
    letters = set(alphabet)
    rotor_alphabet = ROTOR_DICT[rotor]
    loops = []
    while len(letters) > 0:
        first = sorted(list(letters))[0]
        loop = first
        letters.remove(first)
        i = alphabet.index(first)
        ch = rotor_alphabet[i]
        while first != ch:
            loop += ch
            letters.remove(ch)
            i = alphabet.index(ch)
            ch = rotor_alphabet[i]
        loops.append(loop)
    ROTOR_LOOP[rotor] = loops

print(ROTOR_LOOP)


def rotor(symbol, n, reverse=False):
    rotor = ROTOR_LOOP[n]
    for loop in rotor:
        if symbol in loop:
            i = loop.index(symbol)
            if reverse:
                i -= 1
            else:
                i += 1
            i = i % len(loop)
            return loop[i]


def reflector(symbol, n):
    r = REFLECTORS[n]
    i = alphabet.index(symbol)
    return r[i]


def shift(symbol, symbol_shift):
    i = alphabet.index(symbol)
    i += symbol_shift
    i %= len(alphabet)
    return alphabet[i]


def process_rotor(symbol, rot, rot_shift, reverse=False):
    before = shift(symbol, rot_shift)
    after = rotor(before, rot, reverse)
    return shift(after, -rot_shift)


def rotate(rot1, shift1, rot2, shift2, rot3, shift3):
    shift1 = (shift1 + 1) % len(alphabet)
    moves1 = ROTOR_MOVES[rot1]
    if shift1 in moves1:
        shift2 = (shift2 + 1) % len(alphabet)
        moves2 = ROTOR_MOVES[rot2]
        if shift2 in moves2:
            shift3 = (shift3 + 1) % len(alphabet)
    else:
        moves2 = ROTOR_MOVES[rot2]
        shift2_next = (shift2 + 1) % len(alphabet)
        if shift2_next in moves2:
            shift2 = (shift2 + 1) % len(alphabet)
            shift3 = (shift3 + 1) % len(alphabet)
    return (shift1, shift2, shift3)


def enigma_symbol(symbol, refl, rot1, shift1, rot2, shift2, rot3, shift3):
    after_rot1 = process_rotor(symbol, rot1, shift1)
    after_rot2 = process_rotor(after_rot1, rot2, shift2)
    after_rot3 = process_rotor(after_rot2, rot3, shift3)
    
    after_reflector = reflector(after_rot3, refl)
    
    after_rot3_back = process_rotor(after_reflector, rot3, shift3, reverse=True)
    after_rot2_back = process_rotor(after_rot3_back, rot2, shift2, reverse=True)
    after_rot1_back = process_rotor(after_rot2_back, rot1, shift1, reverse=True)
    
    return after_rot1_back


def enigma(s, refl, rot1, shift1, rot2, shift2, rot3, shift3, pairs = ""):
    replace = {}
    for pair in pairs.split():
        c1 = pair[0].upper()
        c2 = pair[1].upper()
        replace[c1] = c2
        replace[c2] = c1
    
    res = ""
    for c in s:
        ch = c.upper()
        if ch not in alphabet:
            continue
        if ch in replace:
            ch = replace[ch]
        shift1, shift2, shift3 = rotate(rot1, shift1, rot2, shift2, rot3, shift3)
        encrypted = enigma_symbol(ch, refl, rot1, shift1, rot2, shift2, rot3, shift3)
        if encrypted in replace:
            encrypted = replace[encrypted]
        res += encrypted
    return res
    
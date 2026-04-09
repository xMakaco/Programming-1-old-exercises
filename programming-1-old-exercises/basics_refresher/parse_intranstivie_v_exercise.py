VERBS = ('schwimmt', 'schwimmen', 'beobachtet', 'kommt zurück')

def v(words, first_pos, second_pos):
    '''Slice a list of strings at a set interval and validate against VERBS'''
    x = " ".join(words[first_pos:second_pos])
    if x in VERBS:
        return True
    else:
        return False

''' Shorter version:
def v(p1, p2, p3):
    return " ".join(p1[p2:p3]) in VERBS
'''

def main():
    assert v(['Amna', 'schwimmt'], 1, 2) == True
    assert v(['Amna', 'schwimmen'], 1, 2) == True
    assert v([], 0, 0) == False
    assert v(['Amna', 'schwimmt'], 0, 1) == False
    assert v(['Amna', 'kommt', 'zurück'], 1, 3) == True
    assert v(['Amna', 'kommt', 'zurück'], 1, 2) == False


if __name__ == '__main__':
    main()

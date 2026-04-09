'''
Write a function func(p1, p2, p3) which takes the three following parameters:
p1: list of strings
p2: start position in the list
p3: end position in the list

and returns:
True iff the strings from position p2 to p3 correspond to a correct name-hobby pair in the HOBBIES dictionary
False otherwise

When you extend this file, make sure that every variable and function has a meaningful name and that you add a header
with your name, the date and a docstring explaining its content
'''

HOBBIES = {'maria': 'synchronized swimming', 
           'frank': 'indoor gardening', 
           'louise': 'cross-country skiing', 
           'sara': 'creative writing', 
           'daniele': 'rock climbing'}

# Longer version
def check_name_hobby_pairs(words, first_pos, last_pos):
    x = ' '.join(words[first_pos:last_pos])
    split = x.split(' ', 1)
    name_slice = split[0]
    hobby_slice = split[1] if len(split) > 1 else ''
    if name_slice in HOBBIES and HOBBIES[name_slice] == hobby_slice:
        return True
    else:
        return False

# Shorter version
def check_name_hobby_pairs(words, first_pos, last_pos):
    if not words or first_pos >= last_pos:
        return False
    name = words[first_pos]
    hobby = ' '.join(words[first_pos + 1:last_pos])
    return name in HOBBIES and HOBBIES[name] == hobby


def main():
    assert check_name_hobby_pairs(['frank', 'indoor', 'gardening', 'louise'], 0, 3) == True
    assert check_name_hobby_pairs([], 0, 0) == False
    assert check_name_hobby_pairs(['frank', 'skiing', 'daniele', 'rock', 'climbing'], 2, 5) == True
    assert check_name_hobby_pairs(['gardening', 'louise', 'skiing', 'swimming', 'sara', 'creative', 'climbing'], 4, 7) == False
    assert check_name_hobby_pairs(['swimming', 'louise', 'cross-country', 'skiing'], 1, 4) == True

if __name__ == '__main__':
    main()
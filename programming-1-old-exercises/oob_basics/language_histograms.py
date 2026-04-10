# First version
def histogram_characters_ger(input_sentence):
    ger_characters_dict = {}
    for i in input_sentence.casefold():
        char_count = input_sentence.casefold().count(i)
        ger_characters_dict[i] = char_count
    print(ger_characters_dict)

# Second version


def histogram_characters_ger(input_sentence):
    ger_characters_dict = {}
    cleaned_sentence = input_sentence.casefold()
    for i in cleaned_sentence:
        if i in ger_characters_dict:
            ger_characters_dict[i] += 1
        else:
            ger_characters_dict[i] = 1
    return (ger_characters_dict)

# First version


def histogram_characters_en(input_sentence):
    chars_conversion = [("ö", "oe"), ("ü", "ue"), ("ä", "ae"), ("ß", "ss")]
    eng_characters_dict = {}

    def convert_chars(input_sentence):
        for k, v in chars_conversion:
            input_sentence = input_sentence.replace(k, v)
        return input_sentence
    input_sentence = convert_chars(input_sentence)
    for i in input_sentence.casefold():
        char_count = input_sentence.casefold().count(i)
        eng_characters_dict[i] = char_count
    print(eng_characters_dict)

# Second version


def histogram_characters_en(input_sentence):
    chars_conversion = [("ö", "oe"), ("ü", "ue"), ("ä", "ae"), ("ß", "ss")]
    eng_characters_dict = {}
    cleaned_sentence = input_sentence.casefold()
    for k, v in chars_conversion:
        cleaned_sentence = cleaned_sentence.replace(k, v)
    for i in cleaned_sentence:
        if i in eng_characters_dict:
            eng_characters_dict[i] += 1
        else:
            eng_characters_dict[i] = 1
    return (eng_characters_dict)


def histogram_all_en(input_sentence):
    chars_conversion = [("ö", "oe"), ("ü", "ue"), ("ä", "ae"), ("ß", "ss")]
    whole_alphabet = list(map(chr, range(97, 123)))
    cleaned_sentence = input_sentence.casefold()
    all_en_characters_dict = {}
    for k, v in chars_conversion:
        cleaned_sentence = cleaned_sentence.replace(k, v)
    for i in cleaned_sentence:
        if i == " ":
            continue
        else:
            if i in all_en_characters_dict:
                all_en_characters_dict[i] += 1
            else:
                all_en_characters_dict[i] = 1
    for j in whole_alphabet:
        if j not in cleaned_sentence:
            all_en_characters_dict[j] = 0
    print(all_en_characters_dict)


def make_histogram(
        input_sentence,
        special_characters=False,
        count_all=False,
        include_whitespaces=False):
    chars_conversion = [("ö", "oe"), ("ü", "ue"), ("ä", "ae"), ("ß", "ss")]
    whole_alphabet = list(map(chr, range(97, 123)))
    cleaned_sentence = input_sentence.casefold()
    complete_dict = {}
    for i in cleaned_sentence:
        if special_characters:
            for k, v in chars_conversion:
                cleaned_sentence = cleaned_sentence.replace(k, v)
        else:
            continue
        if include_whitespaces:
            if i in complete_dict:
                complete_dict[i] += 1
            else:
                complete_dict[i] = 1
        else:
            if i == " ":
                continue
            else:
                if i in complete_dict:
                    complete_dict[i] += 1
                else:
                    complete_dict[i] = 1
    for j in whole_alphabet:
        if count_all:
            if j not in cleaned_sentence:
                complete_dict[j] = 0
        else:
            continue

    return (complete_dict)


def make_histogram(
        input_sentence,
        special_characters=False,
        count_all=False,
        include_whitespaces=False):
    chars_conversion = [("ö", "oe"), ("ü", "ue"), ("ä", "ae"), ("ß", "ss")]
    whole_alphabet = list(map(chr, range(97, 123)))
    cleaned_sentence = input_sentence.casefold()
    complete_dict = {}
    if special_characters:
        for k, v in chars_conversion:
            cleaned_sentence = cleaned_sentence.replace(k, v)
    for i in cleaned_sentence:
        if i == ' ' and not include_whitespaces:
            continue
        if i in complete_dict:
            complete_dict[i] += 1
        else:
            complete_dict[i] = 1
        # complete_dict[i] = complete_dict.get(i, 0) + 1 Shorter version
    if count_all:
        for j in whole_alphabet:
            if j not in cleaned_sentence:
                complete_dict[j] = 0

    return complete_dict


input_sentence = "Die Studierenden klönen"
print(make_histogram(input_sentence))

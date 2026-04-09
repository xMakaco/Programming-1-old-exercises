def histogram_characters_ger(input_sentence):
    ger_characters_dict = {}
    for i in input_sentence.casefold():
        char_count = input_sentence.casefold().count(i)
        ger_characters_dict[i] = char_count
    print(ger_characters_dict)

def histogram_characters_en(input_sentence):
    chars_conversion = [("ö", "oe"), ("ü", "ue"), ("ä", "ae"), ("ß", "ss")]
    eng_characters_dict = {}
    def convert_chars(input_sentence):
        for k, v in chars_conversion:
            converted_sentence = input_sentence.replace(k, v)
            return converted_sentence
    input_sentence = convert_chars(input_sentence)
    for i in input_sentence.casefold():
        char_count = input_sentence.casefold().count(i)
        eng_characters_dict[i] = char_count
    print(eng_characters_dict)

def histogram_all_en(input_sentence):
    chars_conversion = [("ö", "oe"), ("ü", "ue"), ("ä", "ae"), ("ß", "ss")]
    whole_alphabet = [list(map(chr, range(97, 123)))]
    whole_alphabet = str(whole_alphabet).replace("'", "").replace(", ", "").replace("[", "").replace("]", "")
    all_en_characters_dict = {}
    def convert_chars(input_sentence):
        for k, v in chars_conversion:
            converted_sentence = input_sentence.replace(k, v)
            return converted_sentence
    input_sentence = convert_chars(input_sentence)
    for i in input_sentence.casefold():
        if i == " ":
            continue
        char_count = input_sentence.casefold().count(i)
        all_en_characters_dict[i] = char_count
    for j in whole_alphabet:
        if j not in input_sentence.casefold():
            all_en_characters_dict[j] = 0
    print(all_en_characters_dict)

input_sentence = "Die Studierenden klönen"
histogram_all_en(input_sentence)

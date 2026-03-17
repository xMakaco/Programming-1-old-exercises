def histogram_characters_ger(input_sentence):
    ger_characters_dict = {}
    for i in input_sentence.casefold():
        char_count = input_sentence.casefold().count(i)
        ger_characters_dict[i] = char_count
    print(ger_characters_dict)

input_sentence = "Die Studierenden klönen"
histogram_characters_ger(input_sentence)

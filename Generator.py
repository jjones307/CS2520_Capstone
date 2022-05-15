from CsvReader import reader
import random



def generate(lang_choice):
    lang_file = lang_choice.lower() + ".txt"
    vowel_frequency = dict()
    consonant_frequency = dict()
    vowel_group_frequency = dict()
    consonant_group_frequency = dict()
    rel_frequencies = dict()
    n = 1
    
    inf = reader(lang_file)
    counts=[vowel_frequency, consonant_frequency, vowel_group_frequency, consonant_group_frequency, rel_frequencies]
    c_index = 0

    n = int(next(inf)[0])
    while c_index < len(counts):
        line = next(inf)
        if line[0] == "#":
            c_index += 1
        else:            
            # Division by n occurs here in order to produce an average frequency
            counts[c_index][line[0] ] = float(line[1])/n

    name_length = random.randint(5,8)
    generated_name = ""
    next_letter = ""

    v_or_c = ["v", "c"]
    choice = random.choices(v_or_c, weights=[rel_frequencies["v"], rel_frequencies["c"]])
    next_letter = choice[0]

    while(len(generated_name) < name_length):
        if next_letter == 'v':
            choice = random.choices(['v', 'vg'], weights = [rel_frequencies['v'] - rel_frequencies['vg'], rel_frequencies['vg']])[0]
            if choice == 'v':
                letter_to_add = random.choices(list(vowel_frequency.keys()), weights=list(vowel_frequency.values()))[0]
                generated_name += letter_to_add
            else:
                group_to_add = random.choices(list(vowel_group_frequency.keys()), weights=list(vowel_group_frequency.values()))[0]
                generated_name += group_to_add
            next_letter = 'c'
        elif next_letter == 'c':
            choice = random.choices(['c', 'cg'], weights = [rel_frequencies['c'] - rel_frequencies['cg'], rel_frequencies['cg']])[0]
            if choice == 'c':
                letter_to_add = random.choices(list(consonant_frequency.keys()), weights=list(consonant_frequency.values()))[0]
                generated_name += letter_to_add
            else:
                group_to_add = random.choices(list(consonant_group_frequency.keys()), weights=list(consonant_group_frequency.values()))[0]
                generated_name += group_to_add
            next_letter = 'v'
    
    return generated_name

# Just here for testing purposes, we'll have to comment this out in the finished product
print("Spanish:", generate("spanish"))
print("French:", generate("french"))
    



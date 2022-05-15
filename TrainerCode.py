import string
from CsvReader import reader 

def main():
    print("Which language is the text in? \n * German\n * French\n * Spanish")
    lang_choice = input("Choose a language from the options provided above:\n")
    lang_file = lang_choice.lower() + ".txt"
    user_input = input("Enter the text you would like to analyze:\n")

    # Accented characters don't seem to be recognized at the moment, but I'm leaving them in
    # in case we can figure it out
    vowels = "aàáâãäåeèéêëiìíîïoòóõöuùúûü"
    special_characters = "çñ"
    vowel_total = 0
    cons_total = 0
    uncounted = 0  

    # These are used for finding the counts in the given text  
    vowel_counts = dict()
    vowel_group_counts = dict()
    consonant_counts = dict()
    consonant_group_counts = dict()

    # These are read in from the language file and used for actually processing and storing the data
    vowel_frequency = dict()
    consonant_frequency = dict()
    vowel_group_frequency = dict()
    consonant_group_frequency = dict()
    rel_frequencies = dict()

    # This is our sample size, which is read from the file and incremented every time we run the trainer code
    # Here it is initialized as 0; it gets incremented to 1 when saving the first sample data
    n = 0

    try:
        inf = reader(lang_file)
        counts = [vowel_frequency, consonant_frequency, vowel_group_frequency, consonant_group_frequency, rel_frequencies]
        c_index = 0

        n = int(next(inf)[0])
        while c_index < len(counts):
            line = next(inf)
            if line[0] == "#":
                c_index += 1
            else:            
                counts[c_index][line[0]] = float(line[1])
    except FileNotFoundError:
        pass

    user_input = user_input.lower()
    # Spaces are left in so that the last letter in a word and the first letter in the next word don't get
    # counted as a letter grouping
    user_input = [char for char in user_input if char in string.ascii_lowercase or char in vowels or char in special_characters or char == " "]
    user_input = "".join(user_input)
    #print(user_input)
    i = 0

    # This first pass through is a simple count of the vowels and consonants in the text. These counts are used to determine
    # the relative frequency of vowels and consonants in the target language.
    for num in range(0, len(user_input)):
        if user_input[num] != " ":
            if user_input[num] in vowels:
                vowel_total += 1
            else:
                cons_total += 1
        else:
            uncounted += 1

    # This second pass through counts how often each vowel, consonant, vowel group, and consonant group appears in the test. 
    # This is done so that later on we can use weighted random choices construct letter groupings which mimic those of the target language.
    while i < len(user_input):
        if user_input[i] == " ":
            i += 1
            pass
        elif user_input[i] not in vowels: 
            if i == len(user_input) - 1:
                try:
                    consonant_counts[user_input[i]] += 1
                except KeyError:
                    consonant_counts[user_input[i]] = 1
                finally:
                    i += 1
            elif i+1 < len(user_input):
                if user_input[i+1] in vowels or (user_input[i+1] not in string.ascii_lowercase and user_input[i+1] not in special_characters):
                    try:
                        consonant_counts[user_input[i]] += 1
                    except KeyError:
                        consonant_counts[user_input[i]] = 1
                    finally:
                        i += 1
                elif user_input[i+1] not in vowels:
                    consonant_group = user_input[i]
                    j = i+1
                    while j < len(user_input) and user_input[j] not in vowels and (user_input[j] in string.ascii_lowercase or user_input[j] in special_characters):                    
                        consonant_group += user_input[j]
                        j += 1
                    try:
                        consonant_group_counts[consonant_group] += 1
                    except KeyError:
                        consonant_group_counts[consonant_group] = 1
                    finally:
                        i = j
        elif user_input[i] in vowels:
            if i == len(user_input) - 1:
                try:
                    vowel_counts[user_input[i]] += 1
                except KeyError:
                    vowel_counts[user_input[i]] = 1
                finally:
                    i += 1
            elif i+1 < len(user_input):
                if user_input[i+1] not in vowels:
                    try:
                        vowel_counts[user_input[i]] += 1
                    except KeyError:
                        vowel_counts[user_input[i]] = 1
                    finally:
                        i += 1
                elif user_input[i+1] in vowels:
                    vowel_group = user_input[i]
                    j = i+1
                    while j < len(user_input) and user_input[j] in vowels:                    
                        vowel_group += user_input[j]
                        j += 1
                    try:
                        vowel_group_counts[vowel_group] += 1
                    except KeyError:
                        vowel_group_counts[vowel_group] = 1
                    finally:
                        i = j  

    # This series of loops finds the frequency with which different vowels and consonants appear next to each other.
    # The goal is to use the frequency of adjacency to produce more readable outputs that more closely resemble the 
    # target language.

    '''
    Notes to self:
    iterate through list of vowels
        for each single vowel in the text, note and count its adjacencies
            store in dictionary of dictionaries
    iterate through list of consonants
        do same as above
    iterate through list of vowel groups
        search through text for each instance of the given vowel group
            maybe something like "if text[i:len(vg)]"
    iterate through consonant groups
        do same as above
    '''
    ################################### Nothing between this bar and the one below actually does anything yet ###################################
    '''
    letter_counts = [list(vowel_counts.keys()), list(consonant_counts.keys()), list(vowel_group_counts.keys()), list(consonant_group_counts.keys())]
    # adjacencies is a dictionary of dictionaries
    adjacencies = dict()

    for key_list in letter_counts:
        for key in key_list:
            adjacencies[key] = dict()

    i = 0
    for i in range(len(user_input)):
        if user_input[i] == " ":
            pass
        elif i+1 < len(user_input):
            if user_input[i] in letter_counts[0] and user_input[i+1] in letter_counts[1]:
                try:
                    adjacencies[user_input[i]][user_input[i+1]] += 1
                except KeyError:
                    adjacencies[user_input[i]][user_input[i+1]] = 1
            elif user_input[i] in letter_counts[1] and user_input[i+1] in letter_counts[0]:
                try:
                    adjacencies[user_input[i]][user_input[i+1]] += 1
                except KeyError:
                    adjacencies[user_input[i]][user_input[i+1]] = 1
    '''
    ################################### Nothing between this bar and the one above actually does anything yet ###################################            

    rel_vowel_frequency = vowel_total/(len(user_input) - uncounted)
    rel_consonant_frequency = cons_total/(len(user_input) - uncounted)
    rel_vowel_group_frequency = (sum(vowel_group_counts.values()))/(len(user_input) - uncounted)
    rel_cons_group_frequency = (sum(consonant_group_counts.values()))/(len(user_input) - uncounted)
    
    try:
        rel_frequencies["v"] += rel_vowel_frequency
    except KeyError:
        rel_frequencies["v"] = rel_vowel_frequency
    try:
        rel_frequencies["c"] += rel_consonant_frequency
    except KeyError:
        rel_frequencies["c"] = rel_consonant_frequency
    try:
        rel_frequencies["vg"] += rel_vowel_group_frequency
    except KeyError:
        rel_frequencies["vg"] = rel_vowel_group_frequency
    try:
        rel_frequencies["cg"] += rel_cons_group_frequency
    except KeyError:
        rel_frequencies["cg"] = rel_cons_group_frequency
    
    # This block divides the counts for the provided text by the length of the text to find the
    # relative frequency of each letter in the text.
    # It then adds this relative frequency to the values read in from the file so they can be
    # written back to it.
    # During generation, this resulting value is divided by n in order to obtain an average that
    # we can use as our weight for random selection.
    for v in list(vowel_counts.keys()):
        vf = vowel_counts[v] / (len(user_input) - uncounted)
        try:
            vowel_frequency[v] = vowel_frequency[v] + vf
        except KeyError:
            vowel_frequency[v] = vf
    for c in list(consonant_counts.keys()):
        cf = consonant_counts[c] / (len(user_input) - uncounted)
        try:
            consonant_frequency[c] = consonant_frequency[c] + cf
        except KeyError:
            consonant_frequency[c] = cf
    for vg in list(vowel_group_counts.keys()):
        vgf = vowel_group_counts[vg] / (len(user_input) - uncounted)
        try:
            vowel_group_frequency[vg] = vowel_group_frequency[vg] + vgf
        except KeyError:
            vowel_group_frequency[vg] = vgf
    for cg in list(consonant_group_counts.keys()):
        cgf = consonant_group_counts[cg] / (len(user_input) - uncounted)
        try:
            consonant_group_frequency[cg] = consonant_group_frequency[cg] + cgf
        except KeyError:
            consonant_group_frequency[cg] = cgf

    outf = open(lang_file, "w")

    # Data is written into the file in the order vowel, consonant, vowel group, consonant group
    # Sections are separated by a # delimiter

    n += 1
    outf.write(str(n) + "\n")
    for vowel in list(vowel_frequency.items()):
        outf.write(vowel[0] + "," + str(vowel[1]) + "\n")
    outf.write("#\n")
    for cons in list(consonant_frequency.items()):
        outf.write(cons[0] + "," + str(cons[1]) + "\n")
    outf.write("#\n")
    for vg in list(vowel_group_frequency.items()):
        outf.write(vg[0] + "," + str(vg[1]) + "\n")
    outf.write("#\n")
    for cg in list(consonant_group_frequency.items()):
        outf.write(cg[0] + "," + str(cg[1]) + "\n")
    outf.write("#\n")
    for freq in list(rel_frequencies.items()):
        outf.write(freq[0] + "," + str(freq[1]) + "\n")
    outf.write("#\n")

    outf.close()

if __name__ == '__main__':
    main()

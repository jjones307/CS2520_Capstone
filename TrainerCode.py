import string
from CsvReader import reader 

def main():
    print("Which language is the text in? \n * German\n * French\n * Spanish")
    lang_choice = input("Choose a language from the options provided above:\n")
    lang_file = lang_choice.lower() + ".txt"
    user_input = input("Enter the text you would like to analyze:\n")
    vowels = "aeiou"
    vowel_count = 0
    cons_count = 0
    uncounted = 0    
    vowel_frequency = dict()
    vowel_group_frequency = dict()
    consonant_frequency = dict()
    consonant_group_frequency = dict()
    rel_frequencies = dict()
    # This is our sample size, which is read from the file and incremented every time we run the trainer code
    # Here it is initialized as 1 so it can be written to files when training on a language for the first time
    n = 1

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
    user_input = [char for char in user_input if char in string.ascii_lowercase or char == " "]
    user_input = "".join(user_input)
    #print(user_input)
    i = 0

    # This first pass through is a simple count of the vowels and consonants in the text. These counts are used to determine
    # the relative frequency of vowels and consonants in the target language.
    for num in range(0, len(user_input)):
        if user_input[num] in string.ascii_lowercase:
            if user_input[num] in vowels:
                vowel_count += 1
            else:
                cons_count += 1
        else:
            uncounted += 1

    # This second pass through counts how often each vowel, consonant, vowel group, and consonant group appears in the test. 
    # This is done so that later on we can use weighted random choices construct letter groupings which mimic those of the target language.
    while i < len(user_input):
        if user_input[i] not in string.ascii_lowercase:
            i += 1
            pass
        elif user_input[i] not in vowels: 
            if i == len(user_input) - 1:
                try:
                    consonant_frequency[user_input[i]] += 1
                except KeyError:
                    consonant_frequency[user_input[i]] = 1
                finally:
                    i += 1
            elif i+1 < len(user_input):
                if user_input[i+1] in vowels or user_input[i+1] not in string.ascii_lowercase:
                    try:
                        consonant_frequency[user_input[i]] += 1
                    except KeyError:
                        consonant_frequency[user_input[i]] = 1
                    finally:
                        i += 1
                elif user_input[i+1] not in vowels:
                    consonant_group = user_input[i]
                    j = i+1
                    while j < len(user_input) and user_input[j] not in vowels and user_input[j] in string.ascii_lowercase:                    
                        consonant_group += user_input[j]
                        j += 1
                    try:
                        consonant_group_frequency[consonant_group] += 1
                    except KeyError:
                        consonant_group_frequency[consonant_group] = 1
                    finally:
                        i = j
        elif user_input[i] in vowels:
            if i == len(user_input) - 1:
                try:
                    vowel_frequency[user_input[i]] += 1
                except KeyError:
                    vowel_frequency[user_input[i]] = 1
                finally:
                    i += 1
            elif i+1 < len(user_input):
                if user_input[i+1] not in vowels:
                    try:
                        vowel_frequency[user_input[i]] += 1
                    except KeyError:
                        vowel_frequency[user_input[i]] = 1
                    finally:
                        i += 1
                elif user_input[i+1] in vowels:
                    vowel_group = user_input[i]
                    j = i+1
                    while j < len(user_input) and user_input[j] in vowels:                    
                        vowel_group += user_input[j]
                        j += 1
                    try:
                        vowel_group_frequency[vowel_group] += 1
                    except KeyError:
                        vowel_group_frequency[vowel_group] = 1
                    finally:
                        i = j    

    rel_vowel_frequency = vowel_count/(len(user_input) - uncounted)
    rel_consonant_frequency = cons_count/(len(user_input) - uncounted)
    rel_vowel_group_frequency = (sum(vowel_group_frequency.values()))/(len(user_input) - uncounted)
    rel_cons_group_frequency = (sum(consonant_group_frequency.values()))/(len(user_input) - uncounted)
    
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
    '''
    vowel_frequency = dict()
    vowel_group_frequency = dict()
    consonant_frequency = dict()
    consonant_group_frequency = dict()
    rel_frequencies = dict()
    '''
    # Counts should always be updated as averages
    # This block divides the current counts by our sample size n to get an average
    for v in list(vowel_frequency.keys()):
        vowel_frequency[v] /= n
    for c in list(consonant_frequency.keys()):
        consonant_frequency[c] /= n
    for vg in list(vowel_group_frequency.keys()):
        vowel_group_frequency[vg] /= n
    for cg in list(consonant_group_frequency.keys()):
        consonant_group_frequency[cg] /= n
    for f in list(rel_frequencies.keys()):
        rel_frequencies[f] /= n

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

    #print(list(vowel_frequency.items()))
    #print(list(vowel_group_frequency.items()))
    #print(list(consonant_frequency.items()))
    #print(list(consonant_group_frequency.items()))  

    #print(rel_vowel_frequency)
    #print(rel_consonant_frequency)
    #print(rel_vowel_group_frequency)
    #print(rel_cons_group_frequency)

if __name__ == '__main__':
    main()

import string
from CSVReader import reader 

def main():
    # Eventually we'll need to have data read into our dictionaries from the files generated for each language
    user_input = input("Enter the text you would like to analyze:\n")
    vowels = "aeiou"
    vowel_count = 0
    cons_count = 0
    uncounted = 0
    vowel_frequency = dict()
    vowel_group_frequency = dict()
    consonant_frequency = dict()
    consonant_group_frequency = dict()

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
            if (i+1 < len(user_input) and user_input[i+1] in vowels or user_input[i+1] not in string.ascii_lowercase) or i == len(user_input) - 1:
                try:
                    consonant_frequency[user_input[i]] += 1
                except KeyError:
                    consonant_frequency[user_input[i]] = 1
                finally:
                    i += 1
            elif i+1 < len(user_input) and user_input[i+1] not in vowels:
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
            if (i+1 < len(user_input) and user_input[i+1] not in vowels) or i == len(user_input) - 1:
                try:
                    vowel_frequency[usr_input[j]] += 1
                except KeyError:
                    vowel_frequency[usr_input[j]] = 1
                finally:
                    i += 1
            elif i+1 < len(user_input) and user_input[i+1] in vowels:
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

    print(list(vowel_frequency.items()))
    print(list(vowel_group_frequency.items()))
    print(list(consonant_frequency.items()))
    print(list(consonant_group_frequency.items()))    

    rel_vowel_frequency = vowel_count/(len(user_input) - uncounted)
    rel_consonant_frequency = cons_count/(len(user_input) - uncounted)
    rel_vowel_group_frequency = (sum(vowel_group_frequency.values()))/(len(user_input) - uncounted)
    rel_cons_group_frequency = (sum(consonant_group_frequency.values()))/(len(user_input) - uncounted)

    print(rel_vowel_frequency)
    print(rel_consonant_frequency)
    print(rel_vowel_group_frequency)
    print(rel_cons_group_frequency)

if __name__ == '__main__':
    main()

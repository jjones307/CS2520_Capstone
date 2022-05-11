import string

def main():
    user_input = input("Enter the text you would like to analyze:\n")
    vowels = "aeiou"
    vowel_frequency = dict()
    vowel_group_frequency = dict()
    consonant_frequency = dict()
    consonant_group_frequency = dict()

    user_input = user_input.lower()
    user_input = [char for char in user_input if char in string.ascii_lowercase or char == " "]
    user_input = "".join(user_input)
    print(user_input)
    i = 0

    # This first pass through counts vowel, vowel group, consonant, and consonant group frequencies. Vowels and consonants which
    # appear in groups are not counted twice.
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
                    vowel_frequency[user_input[i]] += 1
                except KeyError:
                    vowel_frequency[user_input[i]] = 1
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

    # The second pass through will count how often vowel A appears next to consonant B and how often vowel group A appears
    # next to consonant group B.


if __name__ == '__main__':
    main()

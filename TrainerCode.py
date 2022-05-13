import string
from CsvReader import reader


def main():
    usr_input = input("Enter the text you would like to analyze:\n").lower()
    vowels = "aeiou"
    vowel_frequency = dict()
    vowel_group_frequency = dict()
    consonant_frequency = dict()

    usr_input = [char for char in usr_input if char in string.ascii_lowercase]
    usr_input = "".join(usr_input)

    i = 0
    while i < len(usr_input):
        if usr_input[i] not in vowels:          # if not in vowels adds to frequency of consonant
            try:
                consonant_frequency[usr_input[i]] += 1
            except KeyError:
                consonant_frequency[usr_input[i]] = 1
            finally:
                i += 1
        else:                                   # else is in vowels, adds to frequency of vowels
            try:
                vowel_frequency[usr_input[i]] += 1
            except KeyError:
                vowel_frequency[usr_input[i]] = 1
            finally:
                vowel_group = usr_input[i]
                j = i+1
            """
            goes through list and checks if following
            chars are vowels, if they are vowels, groups them together and adds
            to vowel_group_frequency
            """
            while j < len(usr_input) and usr_input[j] in vowels:

                try:
                    vowel_frequency[usr_input[j]] += 1
                except KeyError:
                    vowel_frequency[usr_input[j]] = 1
                finally:
                    vowel_group += usr_input[j]
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


if __name__ == '__main__':
    main()

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

    for i in range(len(usr_input)):
        if usr_input[i] not in vowels:
            try:
                consonant_frequency[usr_input[i]] += 1
            except KeyError:
                consonant_frequency[usr_input[i]] = 1
        else:
            if i+1 < len(usr_input) and usr_input[i+1] not in vowels:
                try:
                    vowel_frequency[usr_input[i]] += 1
                except KeyError:
                    vowel_frequency[usr_input[i]] = 1
            elif i+1 < len(usr_input) and usr_input[i+1] in vowels:
                vowel_group = usr_input[i]
                j = i+1
                while j < len(usr_input) and usr_input[j] in vowels:
                    vowel_group += usr_input[j]
                    j += 1
                try:
                    vowel_group_frequency[vowel_group] += 1
                except KeyError:
                    vowel_group_frequency[vowel_group] = 1

    print(list(vowel_frequency.items()))
    print(list(vowel_group_frequency.items()))
    print(list(consonant_frequency.items()))


if __name__ == '__main__':
    main()

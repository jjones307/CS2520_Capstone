import string
from CsvReader import reader


def main():
    user_input = input("Enter the text you would like to analyze:\n")
    vowels = "aeiou"
    vowel_frequency = dict()
    vowel_group_frequency = dict()
    consonant_frequency = dict()

    user_input = user_input.lower()
    user_input = [char for char in user_input if char in string.ascii_lowercase]
    user_input = "".join(user_input)
    print(user_input)
    i = 0

    while i < len(user_input):
        #print(i)
        if user_input[i] not in vowels:
            try:
                consonant_frequency[user_input[i]] += 1
            except KeyError:
                consonant_frequency[user_input[i]] = 1
            finally:
                i += 1
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


if __name__ == '__main__':
    main()

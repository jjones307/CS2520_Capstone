string = input("Enter the text you would like to analyze:\n")
vowels = "aeiou"
vowel_frequency = {}
vowel_group_frequency = {}
consonant_frequency = {}

testing = string.lower()
string = [char for char in string if char in 'abcdefghijklmnopqrstuvwxyz']
string = "".join(string)
#print(string)
i = 0

while i < len(string):
  if string[i] not in vowels:
    try:
      consonant_frequency[string[i]] += 1
    except KeyError:
      consonant_frequency[string[i]] = 1
    finally:
      i += 1
  elif string[i] in vowels:
    if i+1 < len(string) and string[i+1] not in vowels:
      try:
        vowel_frequency[string[i]] += 1
      except KeyError:
        vowel_frequency[string[i]] = 1
      finally:
        i += 1
    elif i+1 < len(string) and string[i+1] in vowels:
      vowel_group = string[i]
      j = i+1
      while j < len(string) and string[j] in vowels:
        vowel_group += string[j]
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
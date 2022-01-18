translation = ''
original = input("What would you like to translate? ")
original_list = original.split()
for word in original_list:
    new_word = word[1:] + word[0].lower() + 'ay'
    translation = translation + new_word + ' '
print(translation)

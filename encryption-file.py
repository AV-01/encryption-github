def get_task():
    task = input('Press 1 to encrypt, 2 to decrypt: \n')
    if task == "1":
        encrypt()
    elif task == "2":
        decrypt()
    elif task == '3':
        solve()
    else:
        print("That's not a valid option. Try again.\n")
        get_task()

def encrypt():
    phrase = input('What would you like to encrypt? \n')
    # phrase = 'jogrwikbzf'
    key = input('What should the key be? \n')
    letters = []
    num = []
    try:
        test = int(key)
    except(ValueError):
        print("The key has to be a number, and can't contain any letters")
        encrypt()
    key = str(key)
    num = [int(a) for a in str(key)]
    # num = [4,12,9,23,15,22]
    for x in phrase:
        if x.isalpha():
            if not x.isdigit():
                letters.append(ord(x) - 96)
        else:
            letters.append(x)
    key_length = len(num)
    iteration = 0
    for x in letters:
        index_key = iteration%key_length
        try:
            if phrase[iteration].isalpha():
                if not phrase[iteration].isdigit():
                    letters[iteration] = int(x) + int(key[index_key])
        except:
            thing = True
        iteration += 1
    iteration2 = 0
    # int_letter = 0
    for x in letters:
        if str(phrase[iteration2]).isupper():
            if int(letters[iteration2]) >= -5:
                if int(letters[iteration2]) <= 3:
                    letters[iteration2] += -26
        elif phrase[iteration2].islower():
            if int(letters[iteration2]) > 26:
                int_letter = int(letters[iteration2])
                int_letter += -26
                letters[iteration2] = int_letter
        try:
            letters[iteration2] = chr(letters[iteration2]+96)
        except:
            thing = True
            # print(letters[iteration2])
        iteration2 += 1
    letters_string = str(letters)
    # print(letters_string)
    # letters_string = letters_string.replace()
    letters_string = letters_string[2:]
    letters_string = letters_string[:len(letters_string) - 2]
    # letters_string = letters_string.replace("'[", '[')
    letters_string = letters_string.replace("]'", ']')
    letters_string = letters_string.replace("', '", '')
    letters_string = letters_string.replace("', \"", '')
    letters_string = letters_string.replace("\", '", '')
    letters_string = letters_string.replace(", '", "")
    letters_string = letters_string.replace("\\\\","\\")
    letters_string = letters_string.replace("\\t","  ")
    # letters_string
    print(letters_string)
def decrypt():
    phrase = input('What would you like to decrypt? \n')
    key = input('What is the key? \n')
    letters = []
    num = []
    try:
        test = int(key)
    except(ValueError):
        print("The key has to be a number, and can't contain any letters")
        decrypt()
    key = str(key)
    num = [int(a) for a in str(key)]
    for x in phrase:
        if x.isalpha():
            if not x.isdigit():
                letters.append(ord(x) - 96)
        else:
            letters.append(x)
    key_length = len(num)
    iteration = 0
    for x in letters:
        index_key = iteration%key_length
        try:
            if phrase[iteration].isalpha():
                if not phrase[iteration].isdigit():
                    letters[iteration] = int(x) - int(key[index_key])
        except:
            thing = True
        iteration += 1
    iteration2 = 0
    # int_letter = 0
    for x in letters:
        if str(phrase[iteration2]).isupper():
            if int(letters[iteration2]) >= -40:
                if int(letters[iteration2]) <= -32:
                    letters[iteration2] += 26
        if phrase[iteration2].islower():
            if int(letters[iteration2]) <= 0:
                int_letter = int(letters[iteration2])
                int_letter += 26
                letters[iteration2] = int_letter
        try:
            letters[iteration2] = chr(letters[iteration2]+96)
        except:
            thing = True
            # print(letters[iteration2])
        iteration2 += 1
    letters_string = str(letters)
    # print(letters_string)
    # letters_string = letters_string.replace()
    letters_string = letters_string[2:]
    letters_string = letters_string[:len(letters_string) - 2]
    # letters_string = letters_string.replace("'[", '[')
    letters_string = letters_string.replace("]'", ']')
    letters_string = letters_string.replace("', '", '')
    letters_string = letters_string.replace("', \"", '')
    letters_string = letters_string.replace("\", '", '')
    letters_string = letters_string.replace(", '", "")
    letters_string = letters_string.replace("\\\\","\\")
    letters_string = letters_string.replace("\\t","  ")
    # letters_string
    print(letters_string)
def solve():
    phrase = input('What would you like to solve? \n')
    letters = []
    num = []
    # try:
    #     test = int(key)
    # except(ValueError):
    #     print("The key has to be a number, and can't contain any letters")
    #     encrypt()
    # key = str(key)
    # num = [int(a) for a in str(key)]
    num = [4,12,9,23,15,22]
    for x in phrase:
        if x.isalpha():
            if not x.isdigit():
                letters.append(ord(x) - 96)
        else:
            letters.append(x)
    key_length = len(num)
    iteration = 0
    for x in letters:
        index_key = iteration%key_length
        try:
            if phrase[iteration].isalpha():
                if not phrase[iteration].isdigit():
                    letters[iteration] = int(x) + int(num[index_key])
        except:
            thing = True
        iteration += 1
    iteration2 = 0
    # int_letter = 0
    for x in letters:
        if str(phrase[iteration2]).isupper():
            if int(letters[iteration2]) >= -5:
                if int(letters[iteration2]) <= 3:
                    letters[iteration2] += -26
        elif phrase[iteration2].islower():
            if int(letters[iteration2]) > 26:
                int_letter = int(letters[iteration2])
                int_letter += -26
                letters[iteration2] = int_letter
        try:
            letters[iteration2] = chr(letters[iteration2]+96)
        except:
            thing = True
            # print(letters[iteration2])
        iteration2 += 1
    letters_string = str(letters)
    # print(letters_string)
    # letters_string = letters_string.replace()
    letters_string = letters_string[2:]
    letters_string = letters_string[:len(letters_string) - 2]
    # letters_string = letters_string.replace("'[", '[')
    letters_string = letters_string.replace("]'", ']')
    letters_string = letters_string.replace("', '", '')
    letters_string = letters_string.replace("', \"", '')
    letters_string = letters_string.replace("\", '", '')
    letters_string = letters_string.replace(", '", "")
    letters_string = letters_string.replace("\\\\","\\")
    letters_string = letters_string.replace("\\t","  ")
    # letters_string
    print(letters_string)
get_task()

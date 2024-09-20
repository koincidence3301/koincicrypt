def DecodeFunction (message, shift):
    message = message.strip("|")
    shift = 0
    value = 0
    result = []
    for c in message:
        if c == ' ':
            result += ''
        elif c == ':':
            result += ':'
        elif c == ';':
            result += ';'
        elif c == ',':
            result += ','
        elif c == '"':
            result += '"'
        elif c == '.':
            result += '.'
        elif c == '?':
            result += '?'
        elif c == '!':
            result += '!'
        elif c == "'":
            result += "'"
        elif c == '\t':
            result += ''
        elif c == '|':
            result += ''
        else:
            result += c

    print(result)

if __name__ == '__main__':
    a = ['+ 0: Decipher Message']

    print(*a, sep = "\n")

    choice = input(" ")

    if choice == '0':
        print('ENTER MESSAGE:')
    print('DECIPHERED RESULT: ', DecodeFunction(input(), 2))



def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    result = ''
    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            result += chr(num)
        else:
            result += symbol
    return result
   


if __name__ == "__main__":
    for i in range(0, 35):
        result = getTranslatedMessage('d', "vbqwyivxgshofjeiycfbu", i)
        print(str(i) + ": " + result)

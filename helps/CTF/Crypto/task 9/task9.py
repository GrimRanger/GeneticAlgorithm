

def getTranslatedMessage(message, first_char, offset):
    result = message[first_char]
    ptr = first_char + offset
    while ptr != first_char:
        result += message[ptr]
        ptr += offset
        ptr %= len(message)
        
    return result
   


if __name__ == "__main__":
   result = getTranslatedMessage("GRIREAAEEALRALSNNLLITFT EWAVHPT", 0, 8)
   print result

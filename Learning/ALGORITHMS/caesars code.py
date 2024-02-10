def casears(key, text): # doesnt work with capitallized letters
    code = ""
    for char in text:
        letter = key + ord(char) # ord changed normal letter to ASCII
        if letter > ord('z'): # if we get out of alphabet on the right side
            letter -=26 # ASCII range for alphabet is 97 for 'a' and 122 for 'z' so if someone is out of bounds then we need to decrement by 26
        elif letter < ord('a'): # if we get out of alphabet on the left side
            letter +=26
        
        code +=chr(letter) # chr is changing ASCII to normal 
    return code

txt_to_change = 'qzuipo' # python in key=1
key = -1

print(casears(key,txt_to_change))
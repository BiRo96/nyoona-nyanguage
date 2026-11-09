def first(s):
    return s[:1].lower()

def first2(s):
    return s[:2].lower()

def first3(s):
    return s[:3].lower()

def nyoonize_word(word :str):
    consonants = [
        'b', 'c', 'cs', 'd', 'dz', 'dzs', 'f', 'g', 'gy', 'h', 
        'j', 'k', 'l', 'ly', 'm', 'n', 'ny', 'p', 'r', 's', 
        'sz', 't', 'ty', 'v', 'z', 'zs',
        
        'th', 'ch', 'sh'
    ]
    
    if first3(word) in consonants:
        word = "ny" + word[3:]
                
    elif first2(word) in consonants:
        word = "ny" + word[2:]
        
    elif first(word) in consonants:
        word = "ny" + word[1:]
            
    return word


def nyoonize(raw_text :str):
    splitted_text = raw_text.split(" ")
    reassembled_text = ""
    for word in splitted_text:
        word = nyoonize_word(word)
        reassembled_text += word + " "
    return reassembled_text


def main():
    raw_text = input("Write the message here: ")
    print(nyoonize(raw_text))
    return 0


main()
def first(s):
    return s[:1]

def first2(s):
    return s[:2]

def nyoonize_word(word :str):
    consonants = [
        'b', 'c', 'cs', 'd', 'dz', 'dzs', 'f', 'g', 'gy', 'h', 
        'j', 'k', 'l', 'ly', 'm', 'n', 'ny', 'p', 'r', 's', 
        'sz', 't', 'ty', 'v', 'z', 'zs',
        
        'th', 'ch', 'sh'
    ]
    
    for first_letters in consonants:
        if first_letters == first2(word):
            word = "ny" + word[2:]
            break
        
        elif first_letters == first(word):
            word = "ny" + word[1:]
            break
            
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
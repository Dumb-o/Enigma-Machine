#Hope this works
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#Rotor details
first_rotor = "LUSHQOXDMZNAIKFREPCYBWVGTJ"
second_rotor = "ZOUESYDKFWPCIQXHMVBLGNJRAT"
third_rotor = "EHRVXGAOBQUSIMZFLYNWKTPDJC"


#for words in word_switch:
#    alphabets = alphabets.replace(words[0],"-")
#    alphabets = alphabets.replace(words[1],words[0])
#    alphabets = alphabets.replace("-",words[1])

i = 0
j = 0

def first(text):
    global i
    global j
    global first_rotor
    first_text=""
    for word in text:
        a = alphabets.index(word)
        first_text = first_text + first_rotor[a]
        i+=1    
        if i == 26:
            i = 0
            j += 1
            first_alphabet_second_rotor = second_rotor[0]
            second_rotor = second_rotor.replace(first_alphabet_second_rotor,"")
            second_rotor = second_rotor + first_alphabet_second_rotor
        first_alphabet_first_rotor = first_rotor[0]
        first_rotor = first_rotor.replace(first_alphabet_first_rotor,"")
        first_rotor = first_rotor + first_alphabet_first_rotor
        print(first_rotor)
    return first_text

def second(text):
    global j
    global second_rotor
    second_text = ""
    for word in text:
        j+=1
        a = alphabets.index(word)
    j += 1
    return second_text

def third(text):
    global third_rotor
    third_text = ""
    for word in text:
        a = alphabets.index(word)
        third_text = third_text + third_rotor[a]
    return third_text

def reflector(text):
    reflected_text = ""
    for word in text:
        a = alphabets.index(word)
        reflected_text = reflected_text + third_rotor[a]
    return reflected_text

def word_switch(text):
    word_switch = [["A","C"],["H","O"],["R","Q"],["G","M"],["V","X"]]
    
    for words in word_switch:
        for word in text:
            if words[0] == word:
                text = text.replace(words[0],"-")
                text = text.replace(words[1],words[0])    
                text = text.replace("-",words[1])
                
    return text

word = "IXAMXHERE" #X was used as space

prep = word_switch(word)

first_final = third(second(first(prep)))
reflected = reflector(first_final)
second_final = first(second(third(reflected)))
final_text = word_switch(second_final)

print(final_text)


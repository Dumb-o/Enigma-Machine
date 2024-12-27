wheel = {
    "a":1,
    "b":2,
    "c":3,
    "d":4,
    "e":5,
    "f":6,
    "g":7,
    "h":8,
    "i":9,
    "j":10,
    "k":11,
    "l":12,
    "m":13,
    "n":14,
    "o":15,
    "p":16,
    "q":17,
    "r":18,
    "s":19,
    "t":20,
    "u":21,
    "v":22,
    "w":23,
    "x":24,
    "y":25,
    "z":26
}

reverse_wheel = {
    1:"a",
    2:"b",
    3:"c",
    4:"d",
    5:"e",
    6:"f",
    7:"g",
    8:"h",
    9:"i",
    10:"j",
    11:"k",
    12:"l",
    13:"m",
    14:"n",
    15:"o",
    16:"p",
    17:"q",
    18:"r",
    19:"s",
    20:"t",
    21:"u",
    22:"v",
    23:"w",
    24:"x",
    25:"y",
    26:"z"
    }
    
class enigma():
    def convert(self,text):
        text = text.replace(" ","")
        text = text.lower()
        i=0
        final_list = []
        final = ""
        for word in text:
            current_word_count = wheel.get(word)
            word_to_get = current_word_count+i
            if i>26:
                i-=26
                if word_to_get > 26:
                    word_to_get = word_to_get -  26
                    final_list.append(reverse_wheel.get(word_to_get))
                else:
                    final_list.append(reverse_wheel.get(word_to_get))
            else:
                if word_to_get > 26:
                    word_to_get = word_to_get -  26
                    final_list.append(reverse_wheel.get(word_to_get))
                else:
                    final_list.append(reverse_wheel.get(word_to_get))                
            i+=1
        final = "".join(final_list)
        return final 
    
eg = enigma()
first = eg.convert("Hello World This is a random")
print(first)

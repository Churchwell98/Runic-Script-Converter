'''
Runic to Latin script conversion algorithm
For English, uses the Anglo-Saxon runes as used by J. R. R. Tolkien (https://en.wikipedia.org/wiki/Cirth)
For Swedish, uses the medieval runes as used by Sven Salvenson (https://omniglot.com/conscripts/swedishrunes.htm)
'''

#Function
def is_vowel(character):#Determines if character is a vowel
    if character=='ᚪ' or character=='ᚫ' or character=='ᛖ' or character=='ᛁ' or character=='ᚩ' or character=='ᚢ' or character=='ᛠ' or character=='ᛟ' or character=='ᛇ' or character=='ᛳ':
        return True
    else:
        return False

def convert_Eng(text):#Conversion function for English
    #Declaration
    output=""#Output text
    index=0#keeps track of current loop index
    rune_previous=''

    #Processing
    while index<len(text):#Iterate through text
        rune=text[index]
        if index<len(text)-1:#If not on last rune
            next_rune=text[index+1]
        else:
            next_rune=''
        if rune=='ᚪ' or rune=='ᚫ':#u16aa and u16ab (phonemic when used by Tolkien)
            letter='A'
        elif rune=='ᛒ':#u16d2
            letter='B'
        elif rune=='ᚳ':#u16b3
            if next_rune=='ᚹ':#u16b9
                letter='Q'#forms digraph QU
            else:
                letter='C'
        elif rune=='ᛞ':#u16de
            letter='D'
        elif rune=='ᛖ':#u16d6
            letter='E'
        elif rune=='ᚠ':#u16a0
            letter='F'
        elif rune=='ᚷ':#u16b7
            letter='G'
        elif rune=='ᚻ':#u16bb
            letter='H'
        elif rune=='ᛁ':#u16c1
            if is_vowel(next_rune) and next_rune!='ᛖ' and next_rune!='ᚢ':#If next rune is a vowel except for E and U
                letter='J'
            else:
                letter='I'
        elif rune=='ᛱ':#u16f1
            letter='K'
        elif rune=='ᛚ':#u16da
            letter='L'
        elif rune=='ᛗ':#u16d7
            letter='M'
        elif rune=='ᚾ':#u16be
            letter='N'
        elif rune=='ᚩ':#u16a9
            letter='O'
        elif rune=='ᛈ':#u16c8
            letter='P'
        elif rune=='ᚱ':#u16b1
            letter='R'
        elif rune=='ᛋ':#u16cb
            letter='S'
        elif rune=='ᛏ':#u16cf
            letter='T'
        elif rune=='ᚢ':#u16a2
            #if not is_vowel(next_rune) or rune_previous=='ᚩ':#If next rune is a consonant or the previous rune is represents 'O'
            #    letter='U'
            if not is_vowel(next_rune):
                letter='U'
            else:#next rune is a vowel
                letter='V'#There are few exceptions
        elif rune=='ᚹ':#u16b9
            if rune_previous=='ᚳ':#u16b3
                letter='U'#Digraph QU
            else:
                letter='W'
        elif rune=='ᛉ':#u16c9
            letter='X'
        elif rune=='ᚣ':#u16a3
            letter='Y'
        elif rune=='ᛣ':#u16e3
            letter='Z'
        elif rune=='ᚦ':#u16a6
            output=output+'T'
            letter='H'
        elif rune=='ᛠ':#u16e0
            output=output+'E'
            letter='A'
        elif rune=='ᛥ':#u16e5
            output=output+'S'
            letter='T'
        elif rune=='ᛟ':#u16df
            output=output+'E'
            letter='E'
        elif rune=='ᛝ':#u16dd
            output=output+'N'
            letter='G'
        elif rune=='ᛇ':#u16c7
            output=output+'E'
            letter='O'
        elif rune=='ᛳ':#u16f3
            output=output+'O'
            letter='O'
        elif rune=='ᛲ':#u16f2
            output=output+'S'
            letter='H'
        else:
            letter=rune#Reprint rune

        output=output+letter
        rune_previous=rune#update previous rune
        index+=1#Move to next rune

    #Output
    return output

def convert_Swe(text):#Conversion function for Swedish
    #Declaration
    output=""#Output text
    index=0#keeps track of current loop index

    #Processing
    while index<len(text):#Iterate through text
        rune=text[index]
        if index<len(text)-1:
            rune_next=text[index+1]
        else:
            rune_next=''

        if rune=='ᚠ':
            letter='F'
        elif rune=='ᚡ':
            letter='V'
        elif rune=='ᚢ':
            letter='U'
        elif rune=='ᚤ':
            letter='J'
        elif rune=='ᚥ':
            letter='W'
        elif rune=='ᚦ' or rune=='ᚧ':#digraph TH
            output=output+'T'
            letter='H'
        elif rune=='ᛆ':
            letter='A'
        elif rune=='ᛅ':
            letter='Ä'
        elif rune=='ᚯ':
            letter='Ö'
        elif rune=='ᚱ':
            letter='R'
        elif rune=='ᚴ':
            if rune_next=='ᛋ':#Digraph KS
                letter='X'
                index+=1#Skip next rune
            elif rune_next=='ᚡ':#Digraph KV
                letter='Q'
            else:
                letter='K'
        elif rune=='ᚵ':
            letter='G'
        elif rune=='ᚼ':
            letter='H'
        elif rune=='ᚿ':
            letter='N'
        elif rune=='ᛁ':
            letter='I'
        elif rune=='ᛂ':
            letter='E'
        elif rune=='ᚮ':
            letter='O'
        elif rune=='ᚰ':
            letter='Å'
        elif rune=='ᛋ':
            letter='S'
        elif rune=='ᛪ':
            letter='Z'
        elif rune=='ᛐ' or rune=='ᛏ':
            letter='T'
        elif rune=='ᛑ':
            letter='D'
        elif rune=='ᛒ':
            letter='B'
        elif rune=='ᛔ' or rune=='ᛕ':
            letter='P'
        elif rune=='ᛘ':
            letter='M'
        elif rune=='ᛚ':
            letter='L'
        elif rune=='ᛌ':#Soft S
            letter='S'
        elif rune=='ᛍ':
            letter='Y'
        elif rune=='ᛦ':#Soft G
            letter='G'
        elif rune=='ᛜ':
            letter=','
        elif rune=='᛬':
            letter='.'
        elif rune=='᛫':
            letter=' '#Space
        else:
            letter=rune#Reprint rune

        output=output+letter
        index+=1#Move to next rune

    #Output
    return output
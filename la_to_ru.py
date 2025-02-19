'''
Latin to Runic script conversion algorithm
For English, uses the Anglo-Saxon runes as used by J. R. R. Tolkien (https://en.wikipedia.org/wiki/Cirth)
For Swedish, uses the medieval runes as used by Sven Salvenson (https://omniglot.com/conscripts/swedishrunes.htm)
'''

#Function
def convert_Eng(text):#Conversion function for English
    #Declaration
    output=""#Output text
    letter_previous=''#Keeps track of previous letter
    index=0#keeps track of current loop index

    #Processing
    while index<len(text):#Iterate through text
        letter=text[index]
        if letter=='A' or letter=='a':
            rune='ᚪ'#u16aa (phonemic when used by Tolkien)
        elif letter=='B' or letter=='b':
            rune='ᛒ'#u16d2
        elif letter=='C' or letter=='c' or letter=='Q' or letter=='q':#Q has no rune of its own
            rune='ᚳ'#u16b3
        elif letter=='D' or letter=='d':
            rune='ᛞ'#u16de
        elif letter=='E' or letter=='e':
            if index<len(text)-1:
                if text[index+1]=='A' or text[index+1]=='a':#Digraph ea
                    rune='ᛠ'#u16e0
                    index+=1#Skip next letter
                elif text[index+1]=='E' or text[index+1]=='e':#Digraph ee
                    rune='ᛟ'#u16df
                    index+=1
                elif text[index+1]=='O' or text[index+1]=='o':#Digraph eo
                    rune='ᛇ'#u16c7
                    index+=1
                else:
                    rune='ᛖ'#u16d6
            else:
                rune='ᛖ'#u16d6
        elif letter=='F' or letter=='f':
            rune='ᚠ'#u16a0
        elif letter=='G' or letter=='g':
            rune='ᚷ'#u16b7
        elif letter=='H' or letter=='h':
            rune='ᚻ'#u16bb
        elif letter=='I' or letter=='i' or letter=='J' or letter=='j':
            rune='ᛁ'#u16c1
        elif letter=='K' or letter=='k':
            rune='ᛱ'#u16f1 (this rune was invented by Tolkien)
        elif letter=='L' or letter=='l':
            rune='ᛚ'#u16da
        elif letter=='M' or letter=='m':
            rune='ᛗ'#u16d7
        elif letter=='N' or letter=='n':
            if index<len(text)-1:
                if text[index+1]=='G' or text[index+1]=='g':#digraph ng
                    rune='ᛝ'#u16dd
                    index+=1#Skip next letter
                else:
                    rune='ᚾ'#u16be
            else:
                rune='ᚾ'#u16be
        elif letter=='O' or letter=='o':
            if index<len(text)-1:
                if text[index+1]=='O' or text[index+1]=='o':#digraph oo
                    rune='ᛳ'#u16f3 (this rune was invented by Tolkien)
                    index+=1#Skip next letter
                else:
                    rune='ᚩ'#u16a9 (phonemic when used by Tolkien)
            else:
                rune='ᚩ'#u16a9 (phonemic when used by Tolkien)
        elif letter=='P' or letter=='p':
            if index<len(text)-1:
                if text[index+1]=='H' or text[index+1]=='h':#Digraph ph
                    rune='ᚠ'#u16a0
                    index+=1#Skip next letter
                else:
                    rune='ᛈ'#u16c8
            else:
                rune='ᛈ'#u16c8
        elif letter=='R' or letter=='r':
            rune='ᚱ'#u16b1
        elif letter=='S' or letter=='s':
            if index<len(text)-1:
                if text[index+1]=='H' or text[index+1]=='h':#digraph sh
                    rune='ᛲ'#u16f2 (this rune was invented by Tolkien)
                    index+=1#Skip next letter
                elif text[index+1]=='T' or text[index+1]=='t':#digraph st
                    rune='ᛥ'#u16e5
                    index+=1#Skip next letter
                else:
                    rune='ᛋ'#u16cb
            else:
                rune='ᛋ'#u16cb
        elif letter=='T' or letter=='t':
            if index<len(text)-1:
                if text[index+1]=='H' or text[index+1]=='h':#digraph th
                    rune='ᚦ'#u16a6
                    index+=1#Skip next letter
                else:
                    rune='ᛏ'#u16cf
            else:
                rune='ᛏ'#u16cf
        elif letter=='U' or letter=='u':
            if letter_previous=='Q' or letter_previous=='q':#digraph qu
                rune='ᚹ'#u16b9
            else:
                rune='ᚢ'#u16a2
        elif letter=='V' or letter=='v':
            rune='ᚢ'#u16a2
        elif letter=='W' or letter=='w':
            rune='ᚹ'#u16b9
        elif letter=='X' or letter=='x':
            rune='ᛉ'#u16c9
        elif letter=='Y' or letter=='y':
            rune='ᚣ'#u16a3
        elif letter=='Z' or letter=='z':
            rune='ᛣ'#u16e3
        else:
            rune=letter#reprint letter

        output=output+rune
        letter_previous=letter#Update previous letter
        index+=1#Move to next letter

    #Output
    return output

def convert_Swe(text):#Conversion function for Swedish
    #Declaration
    output=""#Output text
    letter_previous=''#Keeps track of previous letter
    rune_previous=''#Keeps track of previous rune
    index=0#keeps track of current loop index

    #Processing
    while index<len(text):#Iterate through text
        letter=text[index]
        if letter=='A' or letter=='a' or letter=='À' or letter=='à':
            rune='ᛆ'
        elif letter=='B' or letter=='b':
            rune='ᛒ'
        elif letter=='C' or letter=='c':
            rune='ᚴ'#K rune
        elif letter=='D' or letter=='d':
            rune='ᛑ'
        elif letter=='E' or letter=='e' or letter=='É' or letter=='é':
            rune='ᛂ'
        elif letter=='F' or letter=='f':
            rune='ᚠ'
        elif letter=='G' or letter=='g':#Has hard and soft variants
            if index<len(text)-1 and (text[index+1]=='Å' or text[index+1]=='å'):
                rune='ᚵ'#hard
            elif letter_previous=='N' or letter_previous=='n' or letter_previous=='Å' or letter_previous=='å':
                rune='ᚵ'#hard
            elif letter_previous=='R' or letter_previous=='r':
                rune='ᛦ'#soft
            elif index<len(text)-1 and (text[index+1]=='E' or text[index+1]=='e' or 
                                        text[index+1]=='I' or text[index+1]=='i' or 
                                        text[index+1]=='Ä' or text[index+1]=='ä' or 
                                        text[index+1]=='Ö' or text[index+1]=='ö'):
                rune='ᛦ'#soft
            else:
                rune='ᚵ'#hard
        elif letter=='H' or letter=='h':
            rune='ᚼ'
        elif letter=='I' or letter=='i':
            rune='ᛁ'
        elif letter=='J' or letter=='j':
            if index<len(text)-1 and not is_vowel_Sv(text[index+1]):#If at end of word or next char is a consonant
                rune='ᛁ'
            else:
                rune='ᚤ'
        elif letter=='K' or letter=='k':
            if index<len(text)-1 and (text[index+1]=='E' or text[index+1]=='e' '''Inconsistent'''or
                                      text[index+1]=='I' or text[index+1]=='i' '''Inconsistent'''or
                                      text[index+1]=='Y' or text[index+1]=='y' or
                                      text[index+1]=='Ä' or text[index+1]=='ä' or
                                      text[index+1]=='Ö' or text[index+1]=='ö'):#Soft k, rules have very few exceptions (kille)
                output=output+'ᛌ'#Print additional soft s rune
            rune='ᚴ'
        elif letter=='L' or letter=='l':
            rune='ᛚ'
        elif letter=='M' or letter=='m':
            rune='ᛘ'
        elif letter=='N' or letter=='n':
            rune='ᚿ'
        elif letter=='O' or letter=='o':
            rune='ᚮ'
        elif letter=='P' or letter=='p':
            rune='ᛔ'
        elif letter=='Q' or letter=='q':#Rare, equivalent to hard k
            rune='ᚴ'
        elif letter=='R' or letter=='r':
            rune='ᚱ'
        elif letter=='S' or letter=='s':
            if index<len(text)-2 and (text[index+1]=='K' or text[index+1]=='k') and (text[index+2]=='E' or text[index+2]=='e' or
                                                                                        text[index+2]=='I' or text[index+2]=='i' or
                                                                                        text[index+2]=='Y' or text[index+2]=='y' or
                                                                                        text[index+2]=='Ä' or text[index+2]=='ä' or
                                                                                        text[index+2]=='Ö' or text[index+2]=='ö'):#Soft k, rules have very few exceptions
                rune='ᛌ'
            elif index<len(text)-2 and (text[index+1]=='T' or text[index+1]=='t') and (text[index+2]=='J' or text[index+2]=='j'):
                rune='ᛌ'
            elif index<len(text)-1 and (text[index+1]=='C' or text[index+1]=='c' or
                                        text[index+1]=='J' or text[index+1]=='j'):
                rune='ᛌ'
            else:
                rune='ᛋ'
        elif letter=='T' or letter=='t':
            if index<len(text)-1 and (text[index+1]=='H' or text[index+1]=='h'):#If next letter is H
                rune='ᚦ'
                index+=1#Skip next letter
            else:
                rune='ᛐ'
        elif letter=='U' or letter=='u':
            rune='ᚢ'
        elif letter=='V' or letter=='v':
            rune='ᚡ'
        elif letter=='W' or letter=='w':#Rare
            rune='ᚥ'
        elif letter=='X' or letter=='x':
            output=output+'ᚴ'#Print additional k rune
            rune='ᛋ'
        elif letter=='Y' or letter=='y' or letter=='Ü' or letter=='ü':
            rune='ᛍ'
        elif letter=='Z' or letter=='z':#Rare
            rune='ᛪ'
        elif letter=='Å' or letter=='å':
            rune='ᚰ'
        elif letter=='Ä' or letter=='ä' or letter=='Æ' or letter=='æ':
            rune='ᛅ'
        elif letter=='Ö' or letter=='ö' or letter=='Ø' or letter=='ø':
            rune='ᚯ'
        elif letter==' ':#Space
            if is_punctuation(letter_previous):#If previous character was a punctuation mark
                rune=''#Print nothing
            else:
                rune='᛫'
        elif letter==',':
            rune='ᛜ'
        elif letter=='.':
            rune='᛬'
        #Continue
        else:
            rune=letter#reprint letter

        if rune!=rune_previous:#Don't print double runes
            output=output+rune
        letter_previous=letter#Update previous letter
        rune_previous=rune
        index+=1#Move to next letter

    #Output
    return output

def is_vowel_Sv(character):#Used to determine if a character is a vowel
    if (character=='A' or character=='a' or
        character=='E' or character=='e' or
        character=='I' or character=='i' or
        character=='O' or character=='o' or
        character=='U' or character=='u' or
        character=='Å' or character=='å' or
        character=='Ä' or character=='ä' or
        character=='Ö' or character=='ö'):
        return True
    else:
        return False
    
def is_punctuation(character):#Used to determine if a character is a punctuation mark
    if character==',' or character=='.' or character=='!' or character=='?':
        return True
    else:
        return False
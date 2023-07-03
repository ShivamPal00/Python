# The Atbash cipher is an encryption method in which each letter of a word is replaced with its "mirror" letter in the alphabet: A <=> Z; B <=> Y; C <=> X; etc. Create a function that takes a string and applies the Atbash cipher to it.


# A  B  C  D  E  F  G  H  I  J  K  L  M  

# Z  Y  X  W  V  U  T  S  R  Q  P  O   N



def atbash():
    n = input("enter the string")
    mi=[] 
    for i in n:
        ascci_val = ord(i)
        # print(ascci_val)
        mirror_char = chr(90-(ascci_val-65))
        mi.append(mirror_char)
    # mirror = ''.join(mi)
    print(mi)


atbash()
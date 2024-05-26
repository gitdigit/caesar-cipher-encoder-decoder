alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
logo = """
  _____                             _____ _       _             
 / ____|                           / ____(_)     | |            
| |     __ _  ___  ___  __ _ _ __ | |     _ _ __ | |_ ___  _ __ 
| |    / _` |/ _ \/ __|/ _` | '__|| |    | | '_ \| __/ _ \| '__|
| |___| (_| |  __/\__ \ (_| | |   | |____| | | | | || (_) | |   
 \_____\__,_|\___||___/\__,_|_|    \_____|_|_| |_|\__\___/|_|   

"""
print(logo)
#direction = input("Type \'encode\' to encrypt or \'decode\' to decrypt:\n")
#text = input("Say what you want: \n").lower()
#shift = int(input("Type the shift number:\n"))

def encryptage(plain, shiftnb):
    cipher_text = ""
    for letter in plain:
        #   look for the index of the letter in the list
        position = alphabet.index(letter)
        #   set a new position according the shift amount
        new_position = position + shiftnb
        #   set the new letter
        new_letter = alphabet[new_position]
        #   add the new letter to the cipher text
        cipher_text += new_letter
    return cipher_text

def decryptage(the_text, the_shift):
    cipher_text = ""
    for letter in the_text:
        position = alphabet.index(letter)
        new_position = position - the_shift
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    return cipher_text

def caesar_cipher(shift_amount, cipher_direction):
    if cipher_direction == "encode":
        new_text = encryptage(text, shift_amount)
    elif cipher_direction == "decode":
        new_text = decryptage(text, shift_amount)
    print(f"The {cipher_direction}d text is {new_text}")

end_game = False
while not end_game:
    direction = input("Type \'encode\' to encrypt or \'decode\' to decrypt:\n")
    text = input("Say what you want: \n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar_cipher(shift, direction)
    if(input("Do you want to quit? (y/n) ").lower() == "y"):
        end_game =True



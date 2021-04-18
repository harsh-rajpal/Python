
# This program is used to encrypt the entered text by shifting the alphabets by a desired number in aplhabetical order and decrypt them by using the value by which  they were shifted.
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#Ask the user whether he want to encrypt or decrypt the data.
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#Convert all the alphabets enterd by the user in the lower case to find their positon in alphabetical order.
text = input("Type your message:\n").lower()
#Take the input from the user about the number by which he want to shift for encryption or has already shifted the letter in case of decryption.
shift = int(input("Type the shift number:\n"))
#Define the encryption function


def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    cipher_text += alphabet[new_position]
    #printing the final text after decrypting all the letters .
  print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text, shift_amount):
  plain_text = ""
  for letter in cipher_text:
    position = alphabet.index(letter)
    new_position = position - shift_amount
    plain_text += alphabet[new_position]
  #printing the final text after encrypting all the letters .  
  print(f"The decoded text is {plain_text}")



if direction == "encode":
  encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
  decrypt(cipher_text=text, shift_amount=shift)
else:
    print("Please enter the correct option.")
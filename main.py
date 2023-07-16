import sys
import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)


def caesar(input_text, input_shift, input_direction):
    end_text = ""
    for letter in input_text:
        if input_direction == "encode":
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position + input_shift
                new_letter = alphabet[new_position]
                end_text += new_letter
            else:
                end_text += letter
        elif input_direction == "decode":
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position - input_shift
                new_letter = alphabet[new_position]
                end_text += new_letter
            else:
                end_text += letter
        else:
            print("You entered wrong command")
    print(f"The {input_direction} text is {end_text}\n")


while True:
    try:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
        text = input("Type your message: ").lower()
        shift = int(input("Type the shift number: "))

        shift %= 26
        caesar(text, shift, direction)

        ask_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
        if ask_again == "yes":
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))

            shift %= 26

            caesar(text, shift, direction)
        elif ask_again == "no":
            print("Goodbye..")
            break
    except KeyboardInterrupt:
        print("\n[-] ctrl + c detected, program terminated")
        sys.exit(0)

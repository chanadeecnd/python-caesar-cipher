import string
alphabet = list(string.ascii_lowercase)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
while True:
    try:
        shift = int(input("Type the shift number:\n"))
        break
    except ValueError:
        print("Shift as a number!")

def caesarCipher(text, shift, direction):
    original_index = []
    result_message = ""
    shift_alphabet = alphabet[-shift:] + alphabet[:-shift] if direction == "decode" else alphabet[shift:] + alphabet[:shift]
    for detect in text:
        if detect == " ":
            original_index.append(" ")
            continue
        for i in range(len(alphabet)):
            if detect == alphabet[i]:
                original_index.append(i)
                break
    for index in original_index:
        if index == " ":
            result_message += " "
            continue
        index = int(index)
        result_message += shift_alphabet[index]
    message = f"The encoded text is {result_message}" if direction == "encode" else f"The decoded text is {result_message}"
    return result_message, message

result,message = caesarCipher(text, shift, direction)
print(message, result)
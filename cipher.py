# add your code here
message = input("Please enter a sentence:")
message = message.lower()

alpha = "abcdefghijklmnopqrstuvwxyz"
encrypt = ""
index_message = 0

for letters in message:
    index_alpha = 0
    while alpha[index_alpha] != message[index_message]:
        index_alpha += 1
        if index_alpha == 26:
            break
    if index_alpha != 26:
        index_alpha = index_alpha + 5
        if index_alpha > 26:
            index_alpha = index_alpha - 26
        encrypt = encrypt + alpha[index_alpha]
    else:
        encrypt = encrypt + letters
    index_message += 1

print("The encrypted sentence is:", encrypt)

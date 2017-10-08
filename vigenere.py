# Define lowercase unicode conversion
MOD_a = ord("a") % 26
# Define uppercase unicode conversion
MOD_A = ord("A") % 26

# Get Cypher Key (one word, all text)
CipherKey = input("Please give cipher key (One word, all text): ")
while CipherKey.isalpha() is False:
        CipherKey = input("Cipher key must be single word in letters,"
                          " try again! ")

PlainText = input("What plain text would you like to encipher? ")

# CipherKeyCounter for separate iterating from PlainText
CipherKeyCounter = 0
for PlainTextLetter in range(len(PlainText)):
    # 1st layer if statement makes sure to iterate over only plain text letters
    if PlainText[PlainTextLetter].isalpha():
        # 2nd layer if branch ciphers lower case letters of Cipher Key.
        if CipherKey[CipherKeyCounter % len(CipherKey)].islower():
            # 3rd layer if statement ciphers lower case plain text letters.
            if PlainText[PlainTextLetter].islower():
                # Index plain text character to 0, index key character to 0,
                # add the two together. Mod by alphabet length, index back up
                # to lower case plaintext character.
                print(chr((((ord(PlainText[PlainTextLetter]) - MOD_a)
                      + (ord(CipherKey[CipherKeyCounter 
                         % len(CipherKey)]) - MOD_a)) % 26)
                      + ord('a')), end="")
                # Move to next letter of Cipher Key.
                CipherKeyCounter += 1
            # 3rd layer if statement ciphers upper case plain text letters.
            if PlainText[PlainTextLetter].isupper():
                # Index plain text character to 0, index key character to 0,
                # add the two together. Mod by alphabet length, index back up
                # to upper case plaintext character.
                print(chr((((ord(PlainText[PlainTextLetter]) - MOD_A)
                          + (ord(CipherKey[CipherKeyCounter
                            % len(CipherKey)]) - MOD_a))
                          % 26) + ord('A')), end="")
                # Move to next letter of Cipher Key.
                CipherKeyCounter += 1
        # 2nd layer else branch ciphers upper case key character.
        else:
            # 3rd layer if statement ciphers lower case plain text letters.
            if PlainText[PlainTextLetter].islower():
                # Index plain text character to 0, index key character to 0,
                # add the two together. Mod by alphabet length, index back up
                # to lower case plaintext character.
                print(chr((((ord(PlainText[PlainTextLetter]) - MOD_a)
                      + (ord(CipherKey[CipherKeyCounter
                         % len(CipherKey)]) - MOD_A))
                      % 26) + ord('a')), end="")
                # Move to next letter of Cipher Key.
                CipherKeyCounter += 1
            # 3rd layer if statement ciphers upper case plain text letters.
            if PlainText[PlainTextLetter].isupper():
                # Index plain text character to 0, index key character to 0,
                # add the two together. Mod by alphabet length, index back up
                # to upper case plaintext character.
                print(chr((((ord(PlainText[PlainTextLetter]) - MOD_A)
                      + (ord(CipherKey[CipherKeyCounter
                         % len(CipherKey)]) - MOD_A))
                      % 26) + ord('A')), end="")
                # Move to next letter of Cipher Key.
                CipherKeyCounter += 1
    # If plain text character is not a letter.
    else:
        # Print it without advancing the Cipher Key.
        print(PlainText[PlainTextLetter], end="")
# Line break at end of Cipher text
print()
# Success
exit(0)

import re

pattern = r'(?P<artist>^[A-Z][a-z\' ]+):(?P<song>[A-Z ]+)$'

while True:
    input_command = input()

    if input_command == "end":
        break
    match = re.fullmatch(pattern, input_command)

    if match is None:
        print("Invalid input!")
    else:
        encryption_key = len(match['artist'])
        encryptedArtist = ""
        encryptedSong = ""
        for char in match['artist']:
            if char.isalpha():
                if char.isupper():
                    if ord(char) + encryption_key > 90:
                        encryptedArtist += chr(64 + ord(char) + encryption_key - 90)
                    else:
                        encryptedArtist += chr(ord(char) + encryption_key)
                elif char.lower():
                    if ord(char) + encryption_key > 122:
                        encryptedArtist += chr(96 + ord(char) + encryption_key - 122)
                    else:
                        encryptedArtist += chr(ord(char) + encryption_key)
            else:
                encryptedArtist += char

        for char in match['song']:
            if char.isalpha():
                if char.isupper():
                    if ord(char) + encryption_key > 90:
                        encryptedSong += chr(64 + ord(char) + encryption_key - 90)
                    else:
                        encryptedSong += chr(ord(char) + encryption_key)
            else:
                encryptedSong += char
        print(f"Successful encryption: {encryptedArtist}@{encryptedSong}")

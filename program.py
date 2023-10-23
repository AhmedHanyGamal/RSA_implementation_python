# RSA Implementation by Ahmed Hany
# I didn't really put that much thought in defensive programming.
# I didn't really put that much thought in writing clean code
# The main purpose of this code was to implement RSA to make sure that I understood how it works/how it's made

import key_pair


print("""
Welcome to the Asymmetric encryption program that I made.
This program utilizes the RSA encryption algorithm to encrypt and decrypt messages so that you can either
1. encrypt messages so that your adversaries can't read your secret messages
2. digitally sign things so that you can authenticate your messages/transactions so that people know that it's you""")
public_key_dictionary = {}
private_key_dictionary = {}

mistake_counter = 0

while(True):
    print("""
please enter your desired command
    1. Generate Key pair
    2. enter private key manually
    3. enter public key manually
    4. print all public key names
    5. print all private key names
    6. print a specific public key
    7. print a specific private key

    a. encrypt a secret message 🤫
    b. decrypt a secret message 🤫
    c. Sign a message
    d. authenticate a signature
    e. make public key from private key
    
    0. Exit program
    """)
    command = input("    > ")

    if command == '0' or command.lower() == "exit":
        print("Thank you for using our program 😁")
        print("Have a wonderful day")
        break
    elif command == '1' or command.lower() == "generate":
        public_key, private_key = key_pair.generate_key_pair(1024)
        key_name = input("    Enter a Name to save the keys by\n    > ")

        while (key_name in public_key_dictionary) or (key_name in private_key_dictionary):
            print("    Invalid Name, as you have used it before in either a public key, private key, or both")
            key_name = input("    please enter a valid name that you haven't used in any of your keys yet: ")

        public_key_dictionary[key_name] = public_key
        private_key_dictionary[key_name] = private_key
    elif command == '2':
        d = int(input("    please enter the d value: "))
        N = int(input("    Now enter the N value: "))
        phi_N = int(input("    Now last but not least, enter the phi N value: "))
        private_key = key_pair.PrivateKey(d, N, phi_N)

        key_name = input("    Now, What name will you give to the key?\n    ")
        private_key_dictionary[key_name] = private_key
    elif command == '3':
        e = int(input("    please enter the e value: "))
        N = int(input("    Now the N value: "))
        public_key = key_pair.PublicKey(e, N)

        key_name = input("    What name will you give to the key?\n    ")
        public_key_dictionary[key_name] = public_key
        public_key = 0
    elif command == '4':
        print("    Public key names:")
        for i, name in enumerate(public_key_dictionary.keys(), 1):
            print(f"    {i}. {name}")
        
    elif command == '5':
        print("    private key names:")
        for i, name in enumerate(private_key_dictionary.keys(), 1):
            print(f"    {i}. {name}")

    elif command == '6':
        print(f"    you have {len(public_key_dictionary)} key(s)")
        print("    choose a public key to print:")
        for name in public_key_dictionary.keys():
            print(f"    {name}")
        
        desired_key = input("    enter the name of the desired key: ")
        
        if desired_key not in public_key_dictionary:
            print("Invalid key, please try again")
            continue
        
        public_key = public_key_dictionary[desired_key]
        print(f"e = {public_key.e}\nN = {public_key.N}")

    elif command == '7':
        print(f"    you have {len(private_key_dictionary)} key(s)")
        print("    choose a private key to print:")
        for name in private_key_dictionary.keys():
            print(f"    {name}")

        print("\n\nWARNING\nThese are your private keys, meaning that NO ONE should have access/see your private key(s)\nTreat your private key like you treat your house keys, if not more seriously\nSo, proceed with caution")
        desired_key = input("\n\n    enter the name of the desired key: ")
        
        if desired_key not in private_key_dictionary:
            print("Invalid key, please try again")
            continue
        
        private_key = private_key_dictionary[desired_key]
        print(f"d = {private_key.d}\nN = {private_key.N}\nphi N = {private_key.phi_N}")


    elif command.lower() == 'a' or command.lower() == "encrypt":
        print(f"    you have {len(public_key_dictionary)} key(s)")
        print("    choose a public key to encrypt with:")
        for name in public_key_dictionary.keys():
            print(f"    {name}")
        
        desired_key = input("    enter the name of the desired key: ")

        if desired_key not in public_key_dictionary:
            print("Invalid key, please try again")
            continue

        public_key = public_key_dictionary[desired_key]
        
        message = input("    enter the message that you want to encrypt: \n    ")

        encrypted_message = public_key.encrypt_message(message)
        print(f"    encrypted message: {encrypted_message}")
    elif command.lower() == 'b' or command.lower() == "decrypt":
        print(f"    you have {len(private_key_dictionary)} key(s)")
        print("    choose a private key to encrypt with:")
        for name in private_key_dictionary.keys():
            print(f"    {name}")

        desired_key = input("    enter the name of the desired key: ")

        if desired_key not in private_key_dictionary:
            print("Invalid key, please try again")
            continue

        private_key = private_key_dictionary[desired_key]

        encrypted_message = input("    enter the encrypted message that you wish to decrypt \n(Note that it has to be encrypted with the public key corresponding with the chosen private key)\n")
        decrypted_message = private_key.decrypt_message(encrypted_message)
        print(f"    original message: {decrypted_message}")

    elif command.lower() == 'c' or command.lower() == 'sign':
        print(f"    you have {len(private_key_dictionary)} key(s)")
        print("    choose a private key to sign a message with with:")
        for name in private_key_dictionary.keys():
            print(f"    {name}")

        desired_key = input("    enter the name of the desired key: ")

        if desired_key not in private_key_dictionary:
            print("Invalid key, please try again")
            continue

        private_key = private_key_dictionary[desired_key]

        message = input("    enter the message that you wish to sign: ")

        signature = private_key.sign_message(message)

        print(f"    the signature: {signature}")
    elif command.lower() == 'd' or command.lower() == 'authenticate':
        print(f"    you have {len(public_key_dictionary)} key(s)")
        print("    choose the public key that corresponds with the private key used to sign the message in order to authenticate the signature:")
        for name in public_key_dictionary.keys():
            print(f"    {name}")
        
        desired_key = input("    enter the name of the desired key: ")

        if desired_key not in public_key_dictionary:
            print("Invalid key, please try again")
            continue

        public_key = public_key_dictionary[desired_key]

        message = input("    enter the message that was signed: ")
        signature = input("    enter the signature in question: ")

        if not signature.isnumeric():
            print("Invalid Input. The signature should ONLY consist of unseparated digits")
            continue

        signature = int(signature)
        is_authentic_signature = public_key.authenticate_message(message, signature)
        if is_authentic_signature:
            print("The signature is authentic. It has been signed by the private key")
        else:
            print("FALSE SIGNATURE.\nThis means 1 of 3 things\n1. You did something wrong while trying to authenticate the signature (didn't copy the message correctly, added a character that wasn't in the original message, like a space for example)\n2. You used the wrong public key\n3. The signature is wrong/False, so whatever you were going to do, don't do it")

    elif command.lower() == 'e':
        print(f"    you have {len(private_key_dictionary)} key(s)")
        print("    choose choose the private key that you wish to generate a public key from:")
        for name in private_key_dictionary.keys():
            print(f"    {name}")

        desired_key = input("    enter the name of the desired key: ")

        if desired_key not in private_key_dictionary:
            print("Invalid key, please try again")
            continue

        private_key = private_key_dictionary[desired_key]

        public_key = private_key.generate_public_key()
        print(f"e = {public_key.e}\nN = {public_key.N}")

    else:
        mistake_counter += 1

        if mistake_counter == 1:
            print("Invalid input, try entering the number/letter next to your desired command")
        elif mistake_counter == 2:
            print("Invalid input again. Don't worry, happens to the best of us")
        elif mistake_counter == 3:
            print("... This is getting kinda ridiculous. All you have to do is write ONE CHARACTER out of the given options. What's so hard in that?")
        elif mistake_counter == 4:
            print("Are you doing this on purpose? cause if not, then I have some serious concerns. And if so, then please stop, you're just wasting both of our time")
        elif mistake_counter == 5:
            print("You should FUCKING KYS as soon as possible. The world has a serious YOU problem and the best thing you can do to help is not exist in it.")
            print("Fucking IDIOT")
            break
        continue

    mistake_counter = 0
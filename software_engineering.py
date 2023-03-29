def encoder(password):
    # shifts the characters by 3
    i = 0
    en_password = ""
    while i < len(password):
        temp = int(password[i]) + 3
        en_password += str(temp)
        i += 1
    return en_password



def print_menu():
    print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')

def main():
    while True:
        print_menu()
        # user input menu
        choice = int(input('Please enter an option: '))
        if choice == 1:
            password = input('Please enter your password to encode: ')
            en_password = encoder(password)
            print(f'Your password has been encoded and stored!')
        elif choice == 2:
            de_password = decoder(en_password)
            print(f'The encoded password is {en_password}, and the original password is {de_password}.')
        elif choice == 3:
            break

if __name__ == '__main__':
    main()
    
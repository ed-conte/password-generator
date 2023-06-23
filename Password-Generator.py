import secrets
import string


# Function to generate password
def generatePwrd():
    password = ''
    for i in range(password_len):
        password += ''.join(secrets.choice(possible_chars))
    print("Your password is: " + "".join(password))

#welcome messg
print("Welcome to password generator!")

#password length
password_len = int(input("Please enter your desired password length: "))


#character variables
letters = string.ascii_letters
nums = string.digits
spec_characters = string.punctuation
slim_spec = '.'

#character selection
print('''Please choose which set(s) of characters you would like to include in your password, then choose "Generate Password".
            [a] Numbers
            [b] Letters
            [c] All Special Characters
            [d] Only Periods
            [e] Generate Password
            ''')

possible_chars = ''
while True:
    choice = (input("Please enter a letter corresponding to your desired option: "))

    if choice == 'a': 
        possible_chars += nums
    elif choice == 'b':
        possible_chars += letters
    elif choice == 'c':
        possible_chars += spec_characters
    elif choice == 'd':
        possible_chars += slim_spec
    elif choice == 'e':
        generatePwrd()
        break
    else:
        print("Invalid input. Please try again.")

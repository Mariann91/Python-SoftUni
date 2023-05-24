def password_validator(pass_word):
    len_check, letter_digit_check, digit_count_check = False, False, False
    digit_list = [digit for digit in pass_word if digit.isdigit()]
    letter_list = [letter for letter in pass_word if letter.isalpha()]

    if 6 <= len(pass_word) <= 10:
        len_check = True

    if len(digit_list) >= 2:
        digit_count_check = True

    if len(digit_list) + len(letter_list) == len(pass_word):
        letter_digit_check = True

    if len_check and letter_digit_check and digit_count_check:
        print("Password is valid")
    else:
        if not len_check:
            print("Password must be between 6 and 10 characters")
        if not letter_digit_check:
            print("Password must consist only of letters and digits")
        if not digit_count_check:
            print("Password must have at least 2 digits")


password = input()
password_validator(password)

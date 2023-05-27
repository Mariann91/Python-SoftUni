string = input().split()
focus_word = input()

palindromes = [palindrome for palindrome in string if palindrome == palindrome[::-1]]
print(f"{palindromes}\nFound palindrome {palindromes.count(focus_word)} times")

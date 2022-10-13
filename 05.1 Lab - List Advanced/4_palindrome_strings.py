def palindrom(word):
    if word == word[::-1]:
        return word


list = input().split()
palindrom_word = input()

list_of_palindroms = [word for word in list if palindrom(word)]
print(list_of_palindroms)
print(f"Found palindrome {list_of_palindroms.count(palindrom_word)} times")

def minimum_chars_palindrome(string: str) -> int:
    # The string is already a palindrome
    if not string or len(string) == 1:
        return 0

    if string[0] == string[-1]:
        return minimum_chars_palindrome(string[1:-1])
    return 1 + min(minimum_chars_palindrome(string[1:]), minimum_chars_palindrome(string[:-1]))

print(minimum_chars_palindrome("aebcbda"))

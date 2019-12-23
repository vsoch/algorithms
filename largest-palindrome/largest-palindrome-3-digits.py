# A palindromic number reads the same both ways. The largest palindrome
# made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


def largest_palindrome():

    largest = -1

    # First try brute force
    for i in range(100, 999):
        for j in range(100, 999):
            product = str(i * j)

            # Come at from both sides
            start = 0
            end = len(product) - 1

            is_palindrome = True
            while start <= end:

                if start == end:
                    break

                # If they aren't equal, get our early
                if product[start] != product[end]:
                    is_palindrome = False
                    break

                start += 1
                end -= 1

            if is_palindrome and (i * j > largest):
                largest = i * j

    print("The largest palindrome is %s" % largest)

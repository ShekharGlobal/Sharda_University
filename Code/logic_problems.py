# Logic-building practice

# 1. Even / Odd
number = 17
if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# 2. Maximum of three numbers
a, b, c = 10, 25, 15
print("Maximum:", max(a, b, c))


# 3. Factorial
number = 5
factorial = 1

for i in range(1, number + 1):
    factorial *= i

print("Factorial:", factorial)


# 4. Prime number
number = 29
is_prime = True

if number < 2:
    is_prime = False
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

print("Prime:", is_prime)


# 5. Fibonacci
n = 8
a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

print()


# 6. Palindrome
text = "madam"

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")


# 7. Count vowels
text = "Python Programming"
count = 0

for ch in text.lower():
    if ch in "aeiou":
        count += 1

print("Vowels:", count)

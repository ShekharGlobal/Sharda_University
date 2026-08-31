# Nested loops
for row in range(1, 4):
    for column in range(1, 4):
        print("*", end=" ")
    print()

print("\nMultiplication table:")
for i in range(1, 4):
    for j in range(1, 6):
        print(i * j, end=" ")
    print()

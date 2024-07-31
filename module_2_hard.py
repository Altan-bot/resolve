n = int(input())

result = ""

for a in range(1, n + 1):
    for b in range(a, n + 1):
        if n % (a + b) == 0:
            result += str(a) + str(b)
print(result)
N = int(input())
numbersStr = input().split(" ")
numbers = []
for nStr in numbersStr:
    numbers.append(int(nStr))

# average (mean)
print("%.1f" % (sum(numbers) / N))

# median
numbers.sort()
if N % 2 == 0:
    print("%.1f" % ((numbers[int(N / 2)] + numbers[int(N / 2) - 1]) / 2))
else:
    print("%.1f", (numbers[int(N / 2)]))

# mode
counter = {}
largestCount = 1
for n in numbers:
    if n in counter:
        counter[n] += 1
        largestCount = max(largestCount, counter[n])
    else:
        counter[n] = 1
modeNumber = None
for n in counter:
    if counter[n] == largestCount:
        if modeNumber is None:
            modeNumber = n
        else:
            modeNumber = min(modeNumber, n)
print(modeNumber)


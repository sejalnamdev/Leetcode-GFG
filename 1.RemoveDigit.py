number = str(input())
digit = str(input())

for i in range(len(number) - 1):
    if number[i] == digit and number[i+1] > number[i]:
        print(number[ : i]  +  number[i+1 : ])
        found = True
        break

if not found:
    last = number.rfind(digit)
    print(number[ : last] + number[last+1 : ])
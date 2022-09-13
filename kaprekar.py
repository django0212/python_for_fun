from textwrap import wrap

for i in range(1, 100000):
    if len(list(str(i**2)))%2 == 0:
        parts = wrap(str(i**2), len(list(str(i**2)))//2)
        if int(parts[0]) + int(parts[1]) == i:
            print(i)
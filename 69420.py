from random import randint

count = 0

while True:
	num = randint(10**4, 10**5)
	count += 1
	print(num)
	if num == 69420:
		 break 
	else:
		 continue

print(f'Generated 69420! Took {count} tries')

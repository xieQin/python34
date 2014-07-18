ten_things = "Apple Orange"

print("Wait！There isn't 10 things in the list!Let's fix it.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Month", "Year", "Red", "Blue", "Green", "Black", "Master", "Exercise", "Python"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print("Adding: ",next_one)
	stuff.append(next_one)
	print("The length of stuff is %d.", len(stuff))

print("Now here is: ",stuff)
print(stuff[1])
print(stuff[-1])
print(stuff.pop())

print("Now here is: ",stuff)
print(' '.join(stuff))
print('#'.join(stuff[3:5]))



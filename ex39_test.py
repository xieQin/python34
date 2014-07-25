import hashmap

jazz = hashmap.new()
hashmap.set(jazz, 'Miles Davis', 'Flamenco Sketches')
hashmap.set(jazz, 'Miles Davis', 'Kind Of Blue')
hashmap.set(jazz, 'Duke Ellington', 'Beginning To See The Light')
hashmap.set(jazz, 'Billy Strayhorn', 'Lush Life')

print("---- List Test ----")
hashmap.list(jazz)

print("---- Get List ----")
print(hashmap.get(jazz, 'Miles Davis'))
print(hashmap.get(jazz, 'Duke Ellington'))
print(hashmap.get(jazz, 'Billy Strayhorn'))

print("---- Delete Test ----")
print("** Goodbye Miles")
hashmap.delete(jazz, 'Miles Davis')
hashmap.list(jazz)

print("** Goodbye Duke")
hashmap.delete(jazz, "Duke Ellington")
hashmap.list(jazz)

print("** Goodbye Billy")
hashmap.delete(jazz, "Billy Strayhorn")
hashmap.list(jazz)

print("** Test Delete of Missing Key")
hashmap.delete(jazz, "Charles Mingus")


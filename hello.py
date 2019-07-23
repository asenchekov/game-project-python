name = "Asen Chekov"
hi = "Hello, there!"

# function definition
def backwards(string):
  return string[::-1]

# string slicing
# [start:stop:step]
print(name[::-1] + " " + hi)
print(backwards(name))
print(backwards(hi))
print(hi*3)
print(bool("False"))

# for loop
for number in range(-10,10):
  print(number)
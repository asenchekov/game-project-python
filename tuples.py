screenSize = (900, 700)
print(screenSize[0])

testTuple = ('screen size', ) + screenSize
print(len(testTuple))

print("screen size" in testTuple)

for var in testTuple:
  print(var)
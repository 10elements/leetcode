from enum import Enum
class Region(Enum): 
	WEST = 1
	EAST = 2
	NORTH = 3
	SOUTH = 4


print(Region.NORTH.name)
print(Region.NORTH.value)
print(Region(3))
print(Region['NORTH'])
print(Region(4))
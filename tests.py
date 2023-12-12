# Everyone runs his tests in here, don't remove them afterwards, just comment them

from helpers import every, flat

print(flat([[1,2,3,4,5], [21]]) == [1,2,3,4,5,21])

print(every(lambda val: type(val) == int, [1,2,3]) == True)
print(every(lambda val: type(val) == int, [1,2,"omar"]) == False)
# initializing list  
test_list = [[1, 2, 3, 4], [10, 20, 30, 40]]

# using zip() 
# to print list vertically
for x, y in zip(*test_list):
    print (x, [y for y in reversed ([y])])
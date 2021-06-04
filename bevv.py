firstColumn = [1, 2, 3, 4]
    #print(firstColumn)


# Operating System List
secondColumn = [10, 20, 30, 40]

# Printing Elements in Reversed Order
for o in reversed(secondColumn):
    #print(o,firstColumn)

    test_list = firstColumn , secondColumn

for firstColumn, secondColumn in zip(*test_list):
    print(firstColumn,[secondColumn for secondColumn in reversed ([10,20,30,40])])
def print_comparisons(container, cardlist): 

    for item in cardlist: 
        curr_price = container[item][0]
        lowest = curr_price
        highest = curr_price
        print('--' + item + '-- price trends:', end=' ')
        for price in container[item]:
            if curr_price > price: 
                print(',', end = ' ')
                highest = price
                curr_price = price
            if curr_price < price: 
                print('^', end=' ')
                lowest = price
                curr_price = price
            if curr_price == price: 
                print('=', end=' ')
        print(' ')
        print('lowest price: ' + str(lowest))
        print('highest price: ' + str(highest))

def print_to_file(container, cardlist, filename):

    f = open(filename, "w+")

    for item in cardlist: 
        curr_price = container[item][0]
        lowest = curr_price
        highest = curr_price
        f.write('--' + item + '-- price trends:')
        for price in container[item]:
            if curr_price > price: 
                f.write(',')
                highest = price
                curr_price = price
            if curr_price < price: 
                f.write('^')
                lowest = price
                curr_price = price
            if curr_price == price: 
                f.write('=')
        f.write('\n')
        f.write('lowest price: ' + str(lowest) + '\n')
        f.write('highest price: ' + str(highest) + '\n')   

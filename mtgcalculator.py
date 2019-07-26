import pickle
import mtgpickle
import filehandler
import sys
import scraper
import printer

def fetchmedian(cardname): 
    return scraper.fetchmedian(cardname)

def build_dict(inlist):
    dictionary = dict()
    #item is each line in the input file 
    for item in inlist: 
        dictionary[item] = [] 
        dictionary[item].append(fetchmedian(item))
    return dictionary

def update_dict(dictionary, inlist): 
    for item in inlist: 
        if item in dictionary.keys():
            dictionary[item].append(fetchmedian(item))
        else: 
            dictionary[item] = []
            dictionary[item].append(fetchmedian(item))
    return dictionary

def control(args): 
    if (args[0] == 'update'): 
        update(args)

    if (args[0] == 'display'):
        display_info(args)

    if (args[0] == 'exit'):
        sys.exit()

def update(args):
    name = 'pricinginfo'
    if (len(args) > 1):
        if (args[1] == "clean"):
            print('cleaning database...')
            obj = filehandler.build_obj('cardnames.txt')
            container = build_dict(obj)
            print(container)
            mtgpickle.save_obj(container,name)
    else:
        print('updating database...')
        container = mtgpickle.load_obj(name)
        obj = filehandler.build_obj('cardnames.txt')
        new_container = update_dict(container,obj)
        mtgpickle.save_obj(new_container, name)



def display_info(args): 
    #has to have internet to run? 
    if (len(args) > 1):
        cardlist = filehandler.build_obj('cardnames.txt')
        if args[1] == 'update':
            print('updating prices...')        
            container = mtgpickle.load_obj('pricinginfo')
            container = update_dict(container, cardlist)
            mtgpickle.save_obj(container, 'pricelist')
            if (len(args) > 2):
                printer.print_to_file(container, cardlist, args[2])
            else:
                printer.print_comparisons(container, cardlist) 

        if args[2] == 'update':
            print('updating prices...')
            container = mtgpickle.load_obj('pricinginfo')
            container = update_dict(container, cardlist)
            mtgpickle.save_obj(container, 'pricelist')
            printer.print_to_file(container, cardlist, args[1])
        
    else: 
        container = mtgpickle.load_obj('pricinginfo')
        cardlist = filehandler.build_obj('cardnames.txt')
        printer.print_comparisons(container, cardlist)

while True: 
    statement = input()
    args = statement.split()
    control(args)



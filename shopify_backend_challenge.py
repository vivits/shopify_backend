import csv

#item class for storing information about each item
#deleted is either True or False (deleted or not).
#comments are only valid if "deleted" field is True
class Item:
    def __init__(self, name, cost, deleted, comments):
         self.name = name
         self.cost = cost
         self.deleted = deleted
         self.comments = comments
    def __str__(self):
        return 'Name: '+self.name+' | Cost: '+self.cost

#function takes in item list, takes and execute commands from the user
def main_loop(items):
    going = True
    while going:
        action = input('Enter \"display\" to display inventory list, \"delete\" to delete an item, \"add\" to add an item, \"edit\" to edit an item,\"removed\" to view deleted items and their comments, or \"stop\" to exit the app: ')
        if action == 'stop':
            break
        elif action == 'display':
            print('\n')
            print("Item name | Item cost\n")
            for item in items:
                if item.deleted == 'FALSE':
                    print(item)
            print('\n')
            
        elif action == 'delete':
            name = input("Enter name of item to delete: ")
            deleted = False
            for item in items:
                #assumes that there are no duplicate items
                if item.name == name:
                    item.deleted = 'TRUE'
                    com = input("Enter deletion comments: ")
                    item.comments = com
                    print("Deleted "+item.name+" successfully")
                    deleted = True
                    
            if deleted==False:
                print("Failed to delete")
            
        elif action == 'add':
            name = input("Enter item name: ")
            cost = input("Enter item cost: ")
            thing = Item(name, cost, 'FALSE', '')
            items.append(thing)

        elif action == 'removed':
            print('\n')
            print("Deleted item | Comments\n")
            for item in items:
                if item.deleted == 'TRUE':
                    print(item.name+ ' | ' + item.comments)
            print('\n')
            undel = input("Undelete item? (y/n)")
            if undel == 'y':
                restored = False
                restore = input("Enter name of item to restore: ")
                for item in items:
                    if item.name == restore:
                        item.deleted = 'FALSE'
                        item.comments = ''
                        restored = True
                if restored == True:
                    print(restore + ' restored')
                else:
                    print('Failed to restore ' + restore)
                

        elif action == 'edit':
            name = input("Enter name of item to edit: ")
            for item in items:
                if item.name == name:
                    edit = input("Change name? (y/n)")
                    if edit == 'y':
                        new_name = input("Enter new name: ")
                        item.name = new_name
                    edit = input("Change cost? (y/n)")
                    if edit == 'y':
                        new_cost = input("Enter new cost: ")
                        item.cost = new_cost

        else:
            print("Please enter a valid command.\n")

            
#list to store inventory
items = []        
old = input("Would you like to load previous data? (y\\n)")
if old == 'y':
    path = input("Enter path to csv file (with extension): ")
    
    #open the entered file
    try:
        data = open(path, 'r')
        reader = csv.reader(data)
        #skip header line
        next(reader)
        #extract all items from provided file
        for item in reader:
            if item == []:
                break
        
            thing = Item(item[0], item[1], item[2], item[3])
            items.append(thing)
        data.close()

    except FileNotFoundError:
        print('Could not find file named \"' + path +'\". Proceeding without loading data.')


path = ''   
#only accept .csv file names
export = input("Save information to a file? (y/n)")
if export == 'y':
    while path[-4:] != '.csv':
        path = input("Enter output csv file name (with extension): ")

     
    with open(path,'w', newline='') as file:
        writer = csv.writer(file)
        header = ['name', 'cost', 'deleted', 'comments']
        writer.writerow(header)

#main loop
    main_loop(items)
    if export == 'y':
        for item in items:
            row = [item.name, item.cost, item.deleted, item.comments]
            writer.writerow(row)
#not saving information to file
else:
    print('here')
    main_loop(items)


if export == 'y':
    file.close()



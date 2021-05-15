'''
Sylvan Avery Dekker
University of Massachusetts, Amherst
Project 2
ECE 122
17 June 2019
'''
import inventory 


'''------------------------------------------------------
                Main program starts here 
---------------------------------------------------------'''

print("Welcome to BestMedia")
print("====================")
all_items = inventory.initialize()
while True:
    inventory.display_menu()
    command = input("Enter Command:\n")
    if command == "0":
        print("Goodbye!")
        break
    if command == "1":
        inventory.display(all_items)
        continue
    if command == "2":
        inventory.info(all_items)
        continue
    if command == "3":
        inventory.display(all_items, "Book")
        continue
    if command == "4":
        inventory.display(all_items, "Movie")
        continue
    if command == "5":
        target_ref = input("Enter item reference:\n")
        inventory.search_item(all_items, target_ref)
        continue
    if command == "6":
        target_ref = input("Enter item reference:\n")
        del all_items[inventory.search_item_index(all_items, target_ref)]
        print()
    if command == "7":
        all_items = all_items + [inventory.create_item(media_type=input("Book or Movie?\n"))]
        print()
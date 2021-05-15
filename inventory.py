from MediaItem import MediaItem


def initialize():
    """Declares the list all_items and adds
    the initial MediaItem objects. 
    Note that these data would come from a database in real-world
    applications. The data would then be represented in the program
    as MediaItem objects as below.
    """
    all_items = []
    # item 1
    item = MediaItem()
    item.media = "Movie"
    item.title = "2001: A Space Odyssey"
    item.price = 11.99
    item.ref = "TU2RL012"
    item.director = "Stanley Kubrick"
    item.lead_actor = "Keir Dullea"
    all_items = all_items+[item]
    # item 2
    item = MediaItem()
    item.media = "Book"
    item.title = "A Brief History of Time"
    item.price = 10.17
    item.ref = "GV5N32M9"
    item.author = "Stephen Hawking"
    all_items = all_items + [item]
    # item 3
    item = MediaItem()
    item.media = "Movie"
    item.title = "North by Northwest"
    item.price = 8.99
    item.ref = "1DB6HK3L"
    item.director = "Alfred Hitchcock"
    item.lead_actor = "Cary Grant"
    all_items = all_items + [item]
    # item 4
    item = MediaItem()
    item.media = "Movie"
    item.title = "The Good, The Bad and The Ugly"
    item.price = 9.99
    item.ref = "PO5T7Y89"
    item.director = "Sergio Leone"
    item.lead_actor = "Clint Eastwood"
    all_items = all_items + [item]
    # item 5
    item = MediaItem()
    item.media = "Book"
    item.title = "The Alchemist"
    item.price = 6.99
    item.ref = "TR3FL0EW"
    item.author = "Paulo Coelho"
    all_items = all_items + [item]
    # item 6
    item = MediaItem()
    item.media = "Book"
    item.title = "Thus Spoke Zarathustra"
    item.price = 7.81
    item.ref = "F2O9PIE9"
    item.author = "Friedrich Nietzsche"
    all_items = all_items + [item]
    # item 7
    item = MediaItem()
    item.media = "Book"
    item.title = "Jonathan Livingston Seagull"
    item.price = 6.97
    item.ref = "R399CED1"
    item.author = "Richard Bach"
    all_items = all_items + [item]
    # item 8
    item = MediaItem()
    item.media = "Movie"
    item.title = "Gone with the Wind"
    item.price = 4.99
    item.ref = "2FG6B3N9"
    item.director = "Victor Fleming"
    item.lead_actor = "Vivien Leigh"
    all_items = all_items + [item]
    # item 9
    item = MediaItem()
    item.media = "Book"
    item.title = "Gone with the Wind"
    item.price = 7.99
    item.ref = "6Y9OPL87"
    item.author = "Margaret Mitchell"
    all_items = all_items + [item]

    return all_items


def display_menu():
    """Prints the menu of options.
    No parameters, no return.
    """
    print("Menu")
    print("====")
    print("1-List Inventory")
    print("2-Info Inventory")
    print("3-List of All Books")
    print("4-List of All Movies")
    print("5-Item Description")
    print("6-Remove Item")
    print("7-Add Item")
    print("0-Exit")

    # Implement all other functions listed below


def display(all_items, media="all"):
    """Prints all of the data for the MediaItems on the 
    all_items list passed in. The parameter media is used 
    to select for only "Book", "Movie", or, by default, "all". 
    """
    print("Reference/Media/Title/Price\n---------------------------")
    for item in all_items:
        if media == "Book" and item.media == "Book":                      # If "Book" argument, only books listed
            print(item.ref, item.media, item.title, "$%s" % item.price)
        elif media == "Movie" and item.media == "Movie":                  # If "Movie" argument, only movies listed
            print(item.ref, item.media, item.title, "$%s" % item.price)
        elif media == "all":                                              # If "all" or blank argument, all items listed
            print(item.ref, item.media, item.title, "$%s" % item.price)
    print("")


def info(all_items, sum_price=0, max_price=0, book_tally=0, movie_tally=0):
    """Calculates and prints a report of
    the total value of items in the all_items list passed in, 
    the most expensive item, and the total number of each media type. 
    """
    for item in all_items:
        sum_price = item.price + sum_price          # Recursively sets sum of elements' prices
        if item.price > max_price:
            max_price = item.price                  # Recursively sets maximum price within list
        if item.media == "Book":
            book_tally += 1                         # Recursively sets number of books within list
        if item.media == "Movie":
            movie_tally += 1                        # Recursively sets number of movies within list
    print("\nInventory is worth $%s" % sum_price)
    print("Most expensive item at $%s" % max_price)
    print("There are %s Book(s), and %s Movie(s)\n" % (book_tally, movie_tally))


def search_item(all_items, target_ref):
    """Searches the list of items in the all_items list passed in
    for a match on the reference field, target_ref. 
    Returns the MediaItem object if a match is found, otherwise it
    returns None.
    """
    for item in all_items:                 # Cross-references user-input target_ref w/ item.ref attributes
        if item.ref == target_ref:         # of elements in all_items list
            display_item(item)             # If target_ref == any item.ref value, that item is used as an arg. in
            return                         # display_item func.
    print("No such item found!\n")         # If cross-reference finds no match, error message displayed


def display_item(item):
    """Prints all of the data in the MediaItem object, item, passed in. 
    """
    if item.media == "Movie":
        print("Title: %s (Ref: %s, Price: $%s);\nMovie Director: %s; Lead Actor: %s\n" % (
            item.title, item.ref, item.price, item.director, item.lead_actor))
    else:
        print("Title: %s (Ref: %s, Price: $%s);\nAuthor: %s\n" % (
            item.title, item.ref, item.price, item.author))


def search_item_index(all_items, target_ref):
    """Searches the list all_items for a match on the reference
    field target_ref. Returns the index of the item that matches the target_ref,
    returns None if no match was found in the all_items.
    The index is zero-based.  
    """                                     # User-input target_ref is cross-referenced w/ .ref attribute of list items
    for item in all_items:                  # and returns index of that item if it exists
        if item.ref == target_ref:          # No "return None" statement needed b/c already narrowed down in
            return all_items.index(item)    # search_item func.


def create_item(media_type):
    """Creates a new MediaItem object and returns it.
    The argument media_type is either the string "Book" or "Movie".
    The function prompts the user for the data required for 
    the type of media specified by the parameter media_type.
    """
    if media_type != ("Book" or "Movie"):                    # Checks for valid user input
        print("Wrong input!")
        return
    item = MediaItem()                                       # New MediaItem object initialized
    item.media = media_type                                  # New item's attributes are populated by user input
    item.title = input("Enter %s Title:\n" % media_type)
    item.ref = input("Enter %s Reference:\n" % media_type)
    item.price = float(input("Enter %s Price:\n" % media_type))
    if media_type == "Book":
        item.author = input("Enter Author Name:\n")
    elif media_type == "Movie":
        item.director = input("Enter Director Name:\n")
        item.lead_actor = input("Enter Lead Actor Name:\n")
    return item                                              # Returns new item to be added to all_items in main code

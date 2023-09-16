# Initialize checklist
checklist = list()


def create(item: str) -> list:
    """
    Add an item to the checklist.
    :param str item: Clothing item to be added.
    :return list: Checklist with added item.
    """
    checklist.append(item)


def read(index: int) -> str:
    """
    Takes an index and returns the clothing item at that index.
    :param int index: Index of the item to retrieve.
    :return str: Clothing item at given index.
    """
    return checklist[index]


def update(index: int, item: str) -> None:
    """
    Update checklist at given index with specified clothing item.
    :param int index: The index where the item should be updated.
    :param str item: Clothing item to store in checklist.
    """
    checklist[index] = item


def destroy(index: int) -> list:
    """
    Remove a clothing item at a given index.
    :param int index: The index where the item should be removed.
    :return list: Updated checkist after removing item.
    """
    checklist.pop(index)


def list_all_items():
    """
    List all items in list
    """
    print(checklist)


def mark_completed(index):
    pass


def user_input(prompt):
    pass


def select(function_code):
    if function_code == "C":
        # Create item in checklist here
        create(item)

    elif function_code == "R":
        # Read item in checklist here
        pass

    elif function_code == "P":
        # Print all items here
        pass

    elif function_code == "Q":
        # This is where we want to stop our loop
        return False
    else:
        # Catch all
        print("Unknown Option")
    return True


def test():
    """
    Use this function to verify the correctness of the checklist functions by reviewing print results in the terminal.
    """
    create("purple sox")

    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    # print(read(1))


# Run Tests
test()

# running = True

# while running:
#     selection = user_input(
#         "Press C to add to list, R to Read from list, P to display list, and Q to quit"
#     )
#     running = select(selection)

# checklist = ['Blue', 'Orange']
# checklist[1] = 'Cats'
# print(checklist)

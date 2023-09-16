# Initialize checklist
checklist = list()


def create(item: str) -> list:
    """
    _summary_

    :param str item: _description_
    :return list: _description_
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


def destroy(index):
    pass


def list_all_items():
    """
    List all items in list
    """
    pass


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
    _summary_
    """
    create("purple sox")
    create("red cloak")
    print(f"checklist: {checklist}")

    print(read(0))
    print(read(1))

    update(0, "purple socks")

    destroy(1)

    print(read(0))

    list_all_items()


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

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
    :return str: Clothing item at given index or an error message if the index is out of range.
    """
    try:
        return checklist[index]
    except IndexError:
        return print("Index out of range. Please enter a valid index.")


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
    Iterates over each item in the checklist and prints the clothing item and its corresponding index position.
    """
    print("\n")
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1


def mark_completed(index: int) -> str:
    """
    Mark a clothing item as completed by adding a checkmark.
    :param int index: Index of the item to mark as completed.
    :return str: Checkmark with the clothing item.
    """
    return "√" + checklist[index]


def user_input(prompt) -> str:
    """
    Display a message in the terminal and wait for user input.
    :param _type_ prompt: Asks user which CRUD option is wanted.
    :return str: The user's input as a string.
    """
    # initial_user_input = input(prompt)
    # user_input = initial_user_input.strip()
    # return user_input
    user_input = input(prompt)
    return user_input


def select(function_code):
    # Create item
    if function_code == "C".lower():
        input_item = user_input("Input item: ")
        create(input_item)

    # Read item
    # Remember that item_index must actually exist or our program will crash.
    elif function_code == "R".lower():
        item_index = user_input("Index Number? ")

        try:
            item_index = int(item_index)
            result = read(item_index)
            if result is not None:
                print("\nItem at index {}: {}".format(item_index, result))
        except ValueError:
            print("\nInvalid index. Please enter a valid index.")

    # Update item
    elif function_code == "U".lower():
        item_index = user_input("Index Number to Update? ")
        try:
            item_index = int(item_index)
            new_item = user_input("New item value? ")
            update(item_index, new_item)
            print("\nItem at index {} updated to: {}".format(item_index, new_item))
        except ValueError:
            print("\nInvalid index. Please enter a valid index.")

    # Destroy item
    elif function_code == "D".lower():
        item_index = user_input("Index Number to Destroy? ")
        try:
            item_index = int(item_index)
            destroy(item_index)
            print("\nItem at index {} destroyed.".format(item_index))
        except ValueError:
            print("\nInvalid index. Please enter a valid index.")

    # Print all items
    elif function_code == "P".lower():
        list_all_items()

    # Catch all
    else:
        print("Unknown Option")


def test():
    """
    Use this function to verify the correctness of the checklist functions by reviewing print results in the terminal.
    """
    create("purple sox")
    create("red cloak")
    create("green hat")
    create("blue shirt")

    # print(read(0))
    # print(read(1))

    # update(0, "purple socks")
    # destroy(1)

    # print(read(0))
    # # print(read(1))
    # # Call your new function with the appropriate value
    # select("C")
    # # View the results
    # list_all_items()
    # # Call function with new value
    # select("R")
    # # View results
    # list_all_items()

    # # View the results
    # list_all_items()

    # # print(type(mark_completed(0)))
    # print(mark_completed(1))

    # # View results
    # list_all_items()

    # user_value = user_input("Please Enter a value: ")
    # print(user_value)


# Run Tests
test()

running = True

while running:
    selection = user_input(
        "\nPress\nC to add to list,\nR to Read from list,\nU to Update an item in list,\nD to Destroy (remove) an item,\nP to display list, and\nQ to quit: "
    ).lower()

    if selection == "q":
        running = False
    else:
        select(selection)

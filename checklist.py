# Initialize checklist
checklist = list()

def create(item):
    """
    What does this do?

    Args:
        item (_type_): _description_
    """

def read(index):
    """
    _summary_

    Args:
        index (_type_): _description_
    """

def update(index, item):
    """
    _summary_

    Args:
        index (_type_): _description_
        item (_type_): _description_
    """

def destroy(index):
    """
    _summary_

    Args:
        index (_type_): _description_
    """

def list_all_items():
    """
    List all items in list
    """

def mark_completed(index):
    pass

def user_input(prompt):
    pass

def select(function_code):

    if function_code == "C":
        #Create item in checklist here
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
        #Catch all
        print("Unknown Option")
    return True


def test():
    """
    _summary_
    """
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")

    destroy(1)

    print(read(0))

    list_all_items()

# Run Tests
test()

running = True

while running:
    selection = user_input(
        "Press C to add to list, R to Read from list, P to display list, and Q to quit"
    )
    running = select(selection)

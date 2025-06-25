def access_list_element(my_list, index):
    try:
        # Attempt to access the element at the given index
        element = my_list[index]
        print(f"Element at index {index}: {element}")
    except IndexError:
        # Handle the IndexError if the index is out of range
        print(f"Error: Index {index} is out of range for the list.")

# Example list
my_list = [10, 20, 30, 40, 50]

# Accessing valid and invalid indices
access_list_element(my_list, 2)  # Valid index
access_list_element(my_list, 10) # Invalid index
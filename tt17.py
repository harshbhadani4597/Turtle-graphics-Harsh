def access_dict_value(my_dict, key):
    try:
        # Attempt to access the value associated with the given key
        value = my_dict[key]
        print(f"Value for key '{key}': {value}")
    except KeyError:
        # Handle the KeyError if the key does not exist
        print(f"Error: Key '{key}' not found in the dictionary.")

# Example dictionary
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# Accessing valid and invalid keys
access_dict_value(my_dict, "name")  # Valid key
access_dict_value(my_dict, "country")  # Invalid key

def array_of_names(persons):
    # Create an array to hold full names
    full_names = []
    
    # Iterate through the dictionary
    for first_name, last_name in persons.items():
        # Capitalize the first letter of first and last names and create full name
        full_name = f"{first_name.capitalize()} {last_name.capitalize()}"
        # Append the full name to the array
        full_names.append(full_name)
    
    return full_names

# Example usage
if __name__ == "__main__":
    persons = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
      "fifi": "brindacier",
        "phuwish" : "prakobchit"
    }
    print(array_of_names(persons))
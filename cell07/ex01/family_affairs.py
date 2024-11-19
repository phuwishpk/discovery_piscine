def find_the_redheads(family):
    # Use filter to find red-haired individuals and convert to list
    redheads = list(filter(lambda name: family[name] == "red", family))
    return redheads

# Example usage
if __name__ == "__main__":
    dupont_family = {
        "florian": "red",
        "marie": "blond",
        "virginie": "brunette",
        "david": "red",
        "franck": "red"
    }
    print(find_the_redheads(dupont_family))
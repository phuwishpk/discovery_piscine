def average(scores):
    # Calculate the average of the scores
    if not scores:  # Check if the dictionary is empty
        return 0

    total_score = sum(scores.values())  # Sum all the scores
    count = len(scores)  # Count the number of students
    return total_score / count  # Return the average

# Example usage
if __name__ == "__main__":
    class_3B = {
        "marine": 18,
        "jean": 15,
        "coline": 8,
        "luc": 9
    }
    
    class_3C = {
        "quentin": 17,
        "julie": 15,
        "marc": 8,
        "stephanie": 13
    }
    
    print(f"Average for class 3B: {average(class_3B):.2f}.")
    print(f"Average for class 3C: {average(class_3C):.2f}.")
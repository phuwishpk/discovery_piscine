#!/usr/bin/env python3
import sys

# Check if exactly two parameters were passed (excluding the script name)
if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    search_string = sys.argv[2]
    
    # Count occurrences of the keyword in the search string
    count = search_string.count(keyword)
    
    # If the keyword does not appear, print "none"
    if count == 0:
        print("none")
    else:
        print(count)
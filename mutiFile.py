def find_keywords(file1, file2):
    with open(file2, 'r') as f2:
        keywords = f2.readline().rstrip().split()  # Read the first line from file2 and split keywords by spaces

    with open(file1, 'r') as f1:
        for line1 in f1:
            line1 = line1.rstrip()  # Remove trailing newline character
            matching_keywords = []

            for keyword in keywords:
                if keyword in line1:
                    matching_keywords.append(keyword)

            if len(matching_keywords) > 0:
                print(f"The following keywords from line in {file1} are found in {file2}:")
                for matching_keyword in matching_keywords:
                    print(matching_keyword+ " " + file1)
            # else:
                # print(f"No keywords from line  in {file1} found in {file2}.")

            # Read the next line from file2 if not at the end of the file
            if not f2.closed:
                next_line = f2.readline().rstrip()
                if next_line:
                    keywords = next_line.split()
                else:
                    f2.close()
                    break

# Example usage
file1 = "sample1.txt"  # Update with your file name
file2 = "sample2.txt"  # Update with your file name

find_keywords(file1, file2)
# # Example usage
# file1 = "sample1.txt"  # Update with your file name
# file2 = "sample2.txt"  # Update with your file name

# find_keywords(line1, line2)

def find_first_occurrence(my_list, num):
    """Searches for the first occurrence of an integer in a list and returns its index."""
    for i in range(len(my_list)):
        if my_list[i] == num:
            return i
    return -1

if __name__ == "__main__":
    my_list = [10,24,30,51,8,18,9]
    num = 8
    index = find_first_occurrence(my_list, num)
    if index != -1:
        print(f"The first occurrence of {num} in the list is at index {index}.")
    else:
        print(f"{num} is not in the list.")

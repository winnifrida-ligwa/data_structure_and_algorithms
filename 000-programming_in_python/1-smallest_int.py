def get_smallest_integer(my_list):
    """Returns the smallest integer in a list."""
    smallest = my_list[0]
    for number in my_list:
        if number < smallest:
            smallest = number
    return smallest

if __name__ == "__main__":
    my_list = [58, 37, 8, 19, 909, 25]
    smallest = get_smallest_integer(my_list)
    print(f"The smallest integer in the list is: {smallest}")

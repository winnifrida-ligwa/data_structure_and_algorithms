def sum_even_numbers(my_list):
    """Returns the sum of all the even numbers in a list of integers."""
    sum = 0
    for num in my_list:
        if num % 2 == 0:
            sum += num
    return sum

if __name__ == "__main__":
    my_list = [10,38,12,7,14,23,21,19]
    sum_even = sum_even_numbers(my_list)
    print(f"The sum of even numbers in {my_list} is: {sum_even}")

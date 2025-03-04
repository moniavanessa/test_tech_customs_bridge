import random

# generate list with random numbers
def get_random_list(length: int, min_val: int, max_val: int) -> list[int]:

    random_list = []

    # in case min_val is bigger than max_val
    if min_val > max_val:
        min_val, max_val = max_val, min_val

    for _ in range(length):
        random_list.append( random.randrange(min_val, max_val))

    return random_list

# sort list
def sort_list(random_list: list[int]) -> list[int]:
    random_list.sort()

    return random_list

# random nb to add
def get_number_to_insert(min_val: int, max_val: int) -> int:
    # in case min_val is bigger than max_val
    if min_val > max_val:
        min_val, max_val = max_val, min_val

    return random.randrange(min_val, max_val)

# find index
def dpmr(random_list: list[int], new_elem: int, left: int = 0, right: int = None) -> int:

    # boundaries set
    if right is None:
        right = len(random_list) - 1

    # the new element must be inserted on the left position
    if left > right:
        return left

    middle = (left + right) // 2

    # same value
    if new_elem == random_list[middle]:
        return middle
    elif new_elem < random_list[middle]:
        # search in left
        return dpmr(random_list, new_elem, left, middle - 1)
    else:
        # search in right
        return dpmr(random_list, new_elem, middle + 1, right)

# add new element into de sorted list
def add_new_element(random_list: list[int], index, new_element) -> list[int]:

    return random_list[:index] + [new_element] + random_list[index:]

def main():

    length = 10
    min_val = 1
    max_val = 100
    random_list = get_random_list(length, min_val, max_val)

    sorted_list = sort_list(random_list)
    print("Sorted list:", sorted_list)

    new_element = get_number_to_insert(min_val, max_val)
    print("Number to insert:", new_element)

    insert_index = dpmr(sorted_list, new_element)
    print(f"The index to insert {new_element} is {insert_index}")

    updated_list = add_new_element(sorted_list, insert_index, new_element)
    print("Updated list:", updated_list)


if __name__ == "__main__":
    main()
import random

# generate list with random numbers
def get_random_list(longueur: int, min: int, max: int) -> list[int]:

    list_randoms = []

    for i in range(longueur):
        list_randoms.append( random.randrange(min, max))

    return list_randoms

# sort list
def sort_list(list_randoms: list[int]) -> list[int]:

    list_randoms.sort()
    return list_randoms

# random nb to add
def get_number_to_insert(min: int, max: int) -> int:
    return random.randrange(min, max)

# find index
def dpmr(list_randoms: list[int], new_elem: int, left: int = 0, right: int = None) -> int:

    # boundaries set
    if right is None:
        right = len(list_randoms) - 1

    # the new element must be inserted on the left position
    if left > right:
        return left

    middle = (left + right) // 2

    # same value
    if new_elem == list_randoms[middle]:
        return middle
    elif new_elem < list_randoms[middle]:
        # search in left
        return dpmr(list_randoms, new_elem, left, middle - 1)
    else:
        # search in right
        return dpmr(list_randoms, new_elem, middle + 1, right)

# add new element into de sorted list
def add_new_element(list_randoms: list[int], index, new_element) -> list[int]:

    return list_randoms[:index] + [new_element] + list_randoms[index:]


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
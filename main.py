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
def dpmr(list_randoms: list[int], new_elem: int) -> int:

    index_to_compare = int(len(list_randoms)/2)
    middle_elem = list_randoms[index_to_compare]

    print(list_randoms)

    print("index_to_compare: ", index_to_compare)
    print("middle_elem: ", middle_elem)

    if len(list_randoms) == 1 :
        print()

        return

    elif middle_elem > new_elem :
        dpmr(list_randoms[:index_to_compare], new_elem)


    elif middle_elem < new_elem:
        dpmr(list_randoms[index_to_compare:], new_elem)





# insert random nb

if __name__ == "__main__":

    pass
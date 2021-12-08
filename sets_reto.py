## Eliminando los elementos repetidos de una lista

# [1,1,2,2,4] -> [1,2,4]

def remove_duplicates(some_list):
    with_duplicates = some_list 
    without_duplicates = set(with_duplicates)
    return without_duplicates

def run():
    random_list = [1,1,2,2,4]
    print(remove_duplicates(random_list))

if __name__ == '__main__':
    run()
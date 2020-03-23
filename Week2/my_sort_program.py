

def validate_values(iterable,ascending,key):
    if not (isinstance(iterable,list) or isinstance(iterable,tuple)):
        raise ValueError('First argument not passed')
    if not isinstance(ascending,bool):
        raise ValueError('Second argument is not bool')
    if not isinstance(key,str):
        raise ValueError('Third argument is not string')

def sort_list(iterable,ascending):
    if ascending:
        n = len(iterable)
 
        for i in range(n):
            for j in range(0, n-i-1):
                if iterable[j] > iterable[j+1] :
                    iterable[j], iterable[j+1] = iterable[j+1], iterable[j]

    elif not ascending:
        n = len(iterable)
 
        for i in range(n):
            for j in range(0, n-i-1):
                if iterable[j] <= iterable[j+1] :
                    iterable[j], iterable[j+1] = iterable[j+1], iterable[j]


def sort_tuple(iterable,ascending):
    newList = []
    for item in iterable:
        newList.append(item)
    sort_list(newList,ascending)
    iterable = tuple(newList)
    return iterable




def sort_dict(iterable,ascending,key):
    if ascending:
        n = len(iterable)
 
        # Traverse through all array elements
        for i in range(n):
     
            # Last i elements are already in place
            for j in range(0, n-i-1):
     
                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if iterable[j].get(key) > iterable[j+1].get(key) :
                    iterable[j], iterable[j+1] = iterable[j+1], iterable[j]

    elif not ascending:
        n = len(iterable)
 
        # Traverse through all array elements
        for i in range(n):
     
            # Last i elements are already in place
            for j in range(0, n-i-1):
     
                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if iterable[j].get(key) <= iterable[j+1].get(key) :
                    iterable[j], iterable[j+1] = iterable[j+1], iterable[j]

    return iterable

def my_sort(iterable=None,ascending=True,key=""):
    validate_values(iterable,ascending,key)
    if key:
        result = sort_dict(iterable,ascending,key)
    elif isinstance(iterable,tuple):
        result = sort_tuple(iterable,ascending)
    else:
        result = sort_list(iterable,ascending)
    #print(result)
    return result

def main():
    print(my_sort([]))
    print(my_sort((10,8,9,10,100)))
    print(my_sort([10,8,9,10,100],False))
    print(my_sort(iterable=[{'name': 'Marto', 'age': 24}, {'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25}], key='age'))

if __name__ == '__main__':
    main()
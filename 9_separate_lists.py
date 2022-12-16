# Given a heterogenous list, create separate lists for different types of data.

def separate_list(lst:list) -> dict:

    # All the datatypes that I can think of
    result = {
        "str": [],
        "int": [],
        "float": [],
        "complex": [],
        "list": [],
        "tuple": [],
        "dict": [],
        "set": [],
        "bool": [],
        "bytes": [],
        "NoneType": [],
    }
    
    for element in lst:

        try:
            result[type(element).__name__].append(element)

        except KeyError: 
            continue # ignore other datatypes

    return result

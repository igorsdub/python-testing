from numpy import iscomplex

def mean(num_list):
    if iscomplex(num_list).sum():
        return NotImplemented
    try:
        return sum(num_list)/len(num_list)
    except ZeroDivisionError as detail :
        msg = "The algebraic mean of an empty list is undefined."
        msg += "Please provide a list of numbers."
        raise ZeroDivisionError(detail.__str__() + "\n" +  msg)
    except TypeError as detail :
        msg = "The algebraic mean of an non-numerical list is undefined."
        msg += "Please provide a list of numbers."
        raise TypeError(detail.__str__() + "\n" +  msg)
    
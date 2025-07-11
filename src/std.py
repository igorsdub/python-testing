def std(vals):
    """Standard deviation of a list of values.

    Args:
        vals (float): A list of values to calculate the standard deviation for.

    Returns:
        float: The standard deviation of the values in the list.
    """
    if len(vals) == 0: # Special case the empty list.
        return 0.0
    else:
        size_ = len(vals)
        mean  = sum(vals) / size_
        diff_squared = [(x - mean) ** 2 for x in vals]
        variance = sum(diff_squared) / size_
        return variance ** 0.5
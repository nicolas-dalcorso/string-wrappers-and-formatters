#  stringWrappers.py :: v. 0.0.1
#  Implements functions over `str` objects for wrapping and formatting it's content

def setStringToWidth(string:str, width:int) -> str:
    """Given a `string` and a `width`, returns a string with max size `width`.

    Args:
        string (str): string to be formatted
        width (int): max width of formatted string

    Raises:
        ValueError: if the `string` parameter isn't of type `str`, or
                    if the `width` parameter isn't of type `int`,
                    raises Exception.

    Returns:
        str: string of maximum width `width`.
    """
    #   Consistency of types
    if(not(isinstance(string,str)) or not(isinstance(width,int))):
        raise ValueError;
    else:
        if(len(string) <= width):
            return string;
        else:
            string = string[0:(width)] + "...";
            return string;


def toUppercase(string: str, indices:list) -> str:
    """Given an `string` and a list of `indices`, uppercases each char pointed by
    a index in the list.

    Args:
        string (str): string whose chars pointed by `indices` will be uppercased.
        indices (list): list of indices.

    Raises:
        ValueError: if the `string` parameter isn't of type `str`, or
                    if the `indices` parameter isn't of type `list`,
                    raises Exception.

    Returns:
        str: string with uppercased chars pointed by the list parameter.
    """
    #   Consistency of types
    if(not(isinstance(string,str)) or not(isinstance(indices,list))):        
        raise ValueError;
    
    #   Splits the string to a list
    if(string):
        temp = list(string)
    else:
        raise ValueError;
    
    for index in indices:
        temp[index] = temp[index].upper();
        
    return "".join(temp);
  

# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(param1: int, param2: int)-> int:
    """
    Sum of 2 integers in the range of 0-100

    Args:
     parm1(int): first positive integer between 0-100
     param2(int): second positive integer between 0-100

     Returns:
      int: Sum of the 2 arguments provided
    """
    # Validate Input types
    if not isinstance(param1, int) or not isinstance(param2, int):
        raise ValueError("Both inputs must be of integer type")
    
    # validate the range
    if not (0 <= param1 <= 100) or not (0<= param2 <=100):
        raise ValueError("Both inputs must be between 0-100")
    
    return param1 + param2
    



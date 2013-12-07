def get_hours(seconds):
    """ (int) -> int
    Reutrn the number of hours elapsed since midnight.
    
    get_hours(3600)
    >>>1
    get_hours(7500)
    >>>2
    """
    return (seconds//3600) %24

def get_minutes(seconds):
    """ (int) -> int
    Return the number of minutes elapsed since midnight.
    get_minutes(3800)
    >>> 3
    get_minutes(3600)
    >>>0
"""
    return seconds//60 - (get_hours(seconds)*60)

def get_seconds(seconds):
    """(int) -> int
    Return the number of seconds elapsed since midnight.
    get_seconds(3800)
    >>>20
    get_seconds(7200)
    >>>0
    """
    return (seconds -(get_minutes(seconds)*60))%3600

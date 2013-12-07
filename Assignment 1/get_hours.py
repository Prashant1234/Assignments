def get_hours(seconds):
    ''' (int) -> (int)

    Returns number of hours elapsed since midnight
    Precondition: 0<= hours < 24

    get_hours(3800)
    >>> 1
    get_hours(7500)
    >>> 1
    '''
    return seconds//3600

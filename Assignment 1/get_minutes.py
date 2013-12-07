def to_24_hour_clock(hours):
    """ (number) -> number

    hours is a number of hours since midnight. Return the
    hour as seen on a 24-hour clock.

    Precondition: hours >= 0

    >>> to_24_hour_clock(24)
    0
    >>> to_24_hour_clock(48)
    0
    >>> to_24_hour_clock(25)
    1
    >>> to_24_hour_clock(4)
    4
    >>> to_24_hour_clock(28.5)
    4.5
    """

    return hours % 24

    def get_minutes(seconds):
        ''' (int) -> (int)

    Return the number of minutes elapsed since midnight.

    get_minutes(3800)
    >>> 3
    get_minutes(4500)
    >>> 0
    '''
        return ((seconds) - (to_24_hour_clock(seconds/3600)*60))//60

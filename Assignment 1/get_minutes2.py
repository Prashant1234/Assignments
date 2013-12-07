def get_minutes(seconds):
    """ (int) -> int
    Return the number of minutes elapsed since midnight.
    get_minutes(3800)
    >>> 3
    get_minutes(3600)
    0
"""
    return (seconds -((seconds*60)%24))//60

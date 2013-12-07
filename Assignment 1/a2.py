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

        def get_hours(seconds):
        ''' (int) -> int
         Return the number of hours that have elapsed since midnight.
         get_hours(3800)
         >>> 1
         get_hours(7500)
         >>> 2
        get_hours(9000)
        >>> 2
        '''
        return to_24_hour_clock(seconds/3600)

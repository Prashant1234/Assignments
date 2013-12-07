
def to_24_hour_clock(hours):
                """(number) -> number

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


def time_to_utc(utc_offset, time):
               """(number, float) -> float

        Return time at UTC+0, where utc_offset is the number of hours away from
        UTC+0.

        >>> time_to_utc(+0, 12.0)
        12.0
        >>> time_to_utc(+1, 12.0)
        11.0
        >>> time_to_utc(-1, 12.0)
        13.0
        >>> time_to_utc(-11, 18.0)
        5.0
        >>> time_to_utc(-1, 0.0)
        1.0
        >>> time_to_utc(-1, 23.0)
        0.0
        """
    return to_24_hour_clock(time-utc_offset)
    

def get_seconds(seconds):
            """(int) -> int
            Return the number of seconds elapsed since midnight.
            get_seconds(3800)
            >>> 20
                get_seconds(3600)
            >>> 0
            """
            return (seconds - get_minutes(seconds) - get_hours(seconds))

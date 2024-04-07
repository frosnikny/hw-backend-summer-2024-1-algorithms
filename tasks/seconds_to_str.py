__all__ = ("seconds_to_str",)


def seconds_to_str(seconds: int) -> str:
    """Реализует текстовое представление времени.

    Example:
        >> seconds_to_str(20)
        20s
        >> seconds_to_str(60)
        01m00s
        >> seconds_to_str(65)
        01m05s
        >> seconds_to_str(3700)
        01h01m40s
        >> seconds_to_str(93600)
        01d02h00m00s
    """
    s = "%02ds" % (seconds % 60)
    seconds = seconds // 60
    if seconds > 0:
        s = "%02dm" % (seconds % 60) + s
        seconds = seconds // 60
    if seconds > 0:
        s = "%02dh" % (seconds % 24) + s
        seconds = seconds // 24
    if seconds > 0:
        s = "%02dd" % seconds + s
    return s

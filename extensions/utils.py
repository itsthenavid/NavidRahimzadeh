from . import jalali

from django.utils.timezone import localtime


def get_jalali_datetime(datetime):
    """
    The task of this function is to convert the Gregorian date (and time) 
    to the Islamic Hijri Solar / Jalali date in Iran time.

    The input of this function must be from the ORM and its corresponding 
    data type.

    This function is made with jalali.py file dependency authored by 
    https://github.com/mjnaderi/.
    """

    # First, store the Solar Hijri months in a variable.
    jalali_months = (
        "فروردین",
        "اردیبهشت",
        "خرداد",
        "تیر",
        "مرداد",
        "شهریور",
        "مهر",
        "آبان",
        "آذر",
        "دی",
        "بهمن",
        "اسفند",
    )

    # We synchronize the given time and date with Iran time.
    datetime = localtime(datetime)

    # Refer to https://github.com/mjnaderi/Jalali.py/blob/master/jalali.py
    datetime_to_str = f"{datetime.year},{datetime.month},{datetime.day}"
    datetime_to_tuple = jalali.Gregorian(datetime_to_str).persian_tuple()
    datetime_to_list = list(datetime_to_tuple)

    # Counting and measuring months.
    for index, month in enumerate(jalali_months):
        if datetime_to_list[1] == index + 1:
            datetime_to_list[1] = month
            break
    
    # Saving desired output in a variable.
    output = "{} {} {}، ساعت {} و {} دقیقه".format(
        datetime_to_list[2],
        datetime_to_list[1],
        datetime_to_list[0],
        datetime.hour,
        datetime.minute        
    )

    return output

import arrow


def get_timestamp(time_obj):
    """
    :param time_obj:
    :return:
    """
    return arrow.get(time_obj).timestamp


def get_week_period():
    now = arrow.utcnow().to("local")
    return now.shift(weeks=-1).floor("day"), now.ceil("day")


def get_double_week_period():
    now = arrow.utcnow().to("local")
    return now.shift(weeks=-2).floor("day"), now.ceil("day")


def get_month_period():
    now = arrow.utcnow().to("local")
    return now.shift(months=-1).floor("day"), now.ceil("day")


def get_quarter_period():
    now = arrow.utcnow().to("local")
    return now.shift(quarters=-1).floor("day"), now.ceil("day")


def get_year_period():
    now = arrow.utcnow().to("local")
    return now.shift(years=-1).floor("day"), now.ceil("day")


PERIOD = {
    "week": get_week_period,
    "double_week": get_double_week_period,
    "month": get_month_period,
    "quarter": get_quarter_period,
    "year": get_year_period
}

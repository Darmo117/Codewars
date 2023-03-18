import datetime as dt


def check_coupon(entered_code: str, correct_code: str,
                 current_date: str, expiration_date: str) -> bool:
    # Don’t forget to check types in case an int and bool are passed…
    if type(entered_code) is not type(correct_code) or entered_code != correct_code:
        return False
    cur_date = dt.datetime.strptime(current_date, '%B %d, %Y')
    exp_date = dt.datetime.strptime(expiration_date, '%B %d, %Y')
    return cur_date <= exp_date

from datetime import date

import pandas as pd
from bizdays import Calendar


def show_yday(calendar_file):
    '''
    BLA-BLA-BLA

    '''
    f = open(calendar_file, 'r').read().split('\n')
    holidays = [d.date() for d in pd.to_datetime(f)]

    cal = Calendar(holidays, ['Sunday', 'Saturday'])

    today = date.today()
    ontem = cal.offset(today, -1)

    return ontem

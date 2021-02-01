import nsepy
import datetime
from datetime import timedelta


def get_data_for(nifty_eqts):
    all_signals = []
    start, end = get_start_end()
    stock_data = nsepy.get_history(nifty_eqts[0], start, end)
    if stock_data is not None and stock_data.iloc is not None:
        try:
            stock_data.iloc[1]
        except IndexError:
            start, end = get_start_end(-1)
    for eqt in nifty_eqts:
        all_signals.append(print_stock_signal(eqt, start, end))
    return all_signals


def print_stock_signal(eqt, start, end):
    stock_data = nsepy.get_history(eqt, start, end)
    # print(stock_data)

    return get_signals(stock_data)


def get_start_end(ind=0):
    begin_date = datetime.date.today()
    if ind < 0:
        begin_date = begin_date - timedelta(days=ind)
    strt_dt = begin_date - timedelta(days=2)
    end_dt = begin_date - timedelta(days=1)

    if end_dt.weekday() == 6:
        strt_dt = strt_dt - timedelta(days=2)
        end_dt = end_dt - timedelta(days=2)
    elif end_dt.weekday() == 5:
        strt_dt = strt_dt - timedelta(days=1)
        end_dt = end_dt - timedelta(days=1)
    elif end_dt.weekday() == 0:
        strt_dt = strt_dt - timedelta(days=3)
    return strt_dt, end_dt


def get_signals(stock_data):
        symb = stock_data.iloc[0]["Symbol"]
        close = stock_data.iloc[0]["Close"]
        vwap = stock_data.iloc[0]["VWAP"]
        volume = stock_data.iloc[0]["Volume"]
        prevolume = stock_data.iloc[1]["Volume"]
        sign = None
        if ((volume - prevolume) / prevolume) > 0.1:
            if vwap < close:
                sign = "Buy"
            else:
                sign = "Sell"
        else:
            sign = "WAIT"
        print(symb + "--->" + sign)
        return {'name': symb, 'signal': sign}



# if __name__ == '__main__':
#     get_data_for(4)

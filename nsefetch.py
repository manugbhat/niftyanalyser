import nsepy
import datetime
from datetime import timedelta


def get_data_for(nifty_eqts):
    all_signals = []
    for eqt in nifty_eqts:
        all_signals.append(print_stock_signal(eqt))
    return all_signals


def print_stock_signal(eqt):
    strtDt = datetime.date.today() - timedelta(days=2)
    endDt = datetime.date.today() - timedelta(days=1)

    if endDt.weekday() == 6:
        strtDt = strtDt - timedelta(days=1)
        endDt = endDt - timedelta(days=1)
    elif endDt.weekday() == 0:
        strtDt = strtDt - timedelta(days=2)
        endDt = endDt - timedelta(days=2)
    return get_signals(eqt, strtDt, endDt)


def get_signals(eqt, strtDt, endDt):
    stock_data = nsepy.get_history(eqt, strtDt, endDt)
    # print(stock_data)
    symb = stock_data.iloc[0]["Symbol"]
    close = stock_data.iloc[0]["Close"]
    vwap = stock_data.iloc[0]["VWAP"]
    volume = stock_data.iloc[0]["Volume"]
    prevolume = stock_data.iloc[1]["Volume"]
    sign = None
    if ((volume - prevolume) / prevolume) > 0.1:
        if vwap < close:
            sign = "Buy"
            print(symb + "--->" + sign)
        else:
            sign = "Sell"
            print(symb + "--->" + sign)
    else:
        sign = "WAIT"
        print(symb + "--->" + "WAIT")
    return {'name': symb, 'signal': sign}



# if __name__ == '__main__':
#     get_data_for(4)

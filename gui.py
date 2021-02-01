import sys
import nsefetch
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QTableWidget
nifty_eqts = ["MARUTI", "TECHM", "WIPRO", "UPL", "INFY", "EICHERMOT", "ULTRACEMCO", "POWERGRID", "HEROMOTOCO",
              "NTPC", "HCLTECH", "SHREECEM", "M&M", "SUNPHARMA", "TCS", "LT", "BAJAJ-AUTO", "ONGC", "COALINDIA",
              "SBILIFE", "BPCL", "BAJAJFINSV", "ASIANPAINT", "IOC", "HDFCLIFE", "DRREDDY", "DIVISLAB", "RELIANCE",
              "HDFCBANK", "CIPLA", "HINDUNILVR", "NESTLEIND", "KOTAKBANK", "GRASIM", "BRITANNIA", "TATAMOTORS",
              "ADANIPORTS", "TITAN", "AXISBANK", "ICICIBANK", "BAJFINANCE", "HDFC", "ITC", "SBIN", "JSWSTEEL",
              "GAIL", "BHARTIARTL", "TATASTEEL", "INDUSINDBK", "HINDALCO"]
nifty_eqts.sort()

page_size = 5

main_layout = None


def get_stock():
    if (page_size * current_page) == len(nifty_eqts):
        return []
    if current_page == 0:
        ret_eqt = nifty_eqts[current_page:page_size]
        return ret_eqt
    else:
        start = page_size * current_page
        end = (page_size * (current_page + 1))
        return nifty_eqts[start:end]


def open_window():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("PyQt5 App")
    window.setGeometry(800, 800, 280, 80)
    window.move(100, 100)
    window.resize(500, 500)
    global main_layout
    main_layout = QVBoxLayout()
    hello_msg = QLabel("<h1>Buy Sell Signals</h1>", parent=window)
    main_layout.addWidget(hello_msg, 0)
    tableView = QTableWidget()
    tableView.setEnabled(True)
    tableView.setAlternatingRowColors(True)
    tableView.setRowCount(5)
    tableView.setColumnCount(2)
    next_btn = QPushButton('Next')
    next_btn.clicked.connect(lambda: get_next(tableView))
    main_layout.addWidget(next_btn, 0)
    get_next(tableView)
    main_layout.addWidget(tableView)
    window.setLayout(main_layout)
    window.show()

    # 5. Run your application's event loop (or main loop)
    sys.exit(app.exec_())


current_page = 0


def get_next(layout):

    stocks = get_stock()
    if len(stocks) > 0:
        add_stock_to_table(stocks, layout)
        global current_page
        current_page += 1
    else:
        current_page = 0
        stocks = get_stock()
        add_stock_to_table(stocks, layout)
        current_page += 1


def add_stock_to_table(stocks, layout):
    counter = 0
    for eq in nsefetch.get_data_for(stocks):
        signal = eq.get("signal")
        layout.setItem(counter, 0, get_colored_item(signal, eq.get("name")))
        layout.setItem(counter, 1, get_colored_item(signal, eq.get("signal")))
        counter += 1


def get_colored_item(signal, wid_label):
    color = QtGui.QColor(251, 251, 251)
    if signal == "Buy":
        color = QtGui.QColor(0, 204, 0)
    elif signal == "Sell":
        color = QtGui.QColor(255, 0, 0)
    eq_t_w = QTableWidgetItem(wid_label)
    eq_t_w.setBackground(color)
    return eq_t_w


if __name__ == "__main__":
    open_window()

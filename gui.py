import sys
import nsefetch
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QScrollArea
from PyQt5.QtWidgets import QHBoxLayout

nifty_eqts = ["MARUTI", "TECHM", "WIPRO", "UPL", "INFY", "EICHERMOT", "ULTRACEMCO", "POWERGRID", "HEROMOTOCO",
              "NTPC", "HCLTECH", "SHREECEM", "M&M", "SUNPHARMA", "TCS", "LT", "BAJAJ-AUTO", "ONGC", "COALINDIA",
              "SBILIFE", "BPCL", "BAJAJFINSV", "ASIANPAINT", "IOC", "HDFCLIFE", "DRREDDY", "DIVISLAB", "RELIANCE",
              "HDFCBANK", "CIPLA", "HINDUNILVR", "NESTLEIND", "KOTAKBANK", "GRASIM", "BRITANNIA", "TATAMOTORS",
              "ADANIPORTS", "TITAN", "AXISBANK", "ICICIBANK", "BAJFINANCE", "HDFC", "ITC", "SBIN", "JSWSTEEL",
              "GAIL", "BHARTIARTL", "TATASTEEL", "INDUSINDBK", "HINDALCO"]

page_size = 5


def get_stock():
    if (page_size * current_page) == len(nifty_eqts):
        return []
    if current_page == 0:
        ret_eqt = nifty_eqts[current_page:page_size - 1]
        return ret_eqt
    else:
        start = page_size * current_page
        end = (page_size * (current_page + 1)) -1
        return nifty_eqts[start:end]


def open_window():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("PyQt5 App")
    window.setGeometry(800, 800, 280, 80)
    window.move(100, 100)
    window.resize(500, 500)
    main_layout = QHBoxLayout()
    scrollArea = QScrollArea()
    scrollArea.setWidgetResizable(True)
    helloMsg = QLabel("<h1>Buy Sell Signals</h1>", parent=window)
    scrollContents = QWidget()
    layout = QGridLayout(scrollContents)
    layout.addWidget(helloMsg, 0, 1)
    next_btn = QPushButton('Next');
    next_btn.clicked.connect(lambda: get_next(layout))
    layout.addWidget(next_btn, 1, 1)
    scrollArea.setWidget(scrollContents)
    main_layout.addWidget(scrollArea)
    get_next(layout)
    window.setLayout(main_layout)
    window.show()

    # 5. Run your application's event loop (or main loop)
    sys.exit(app.exec_())


current_page = 0


def get_next(layout):
    counter = layout.rowCount()
    counter += 1

    for eq in nsefetch.get_data_for(get_stock()):
        layout.addWidget(QLabel(eq.get("name")), counter, 1)
        layout.addWidget(QLabel(eq.get("signal")), counter, 2)
        counter += 1
    global current_page
    current_page += 1


if __name__ == "__main__":
    open_window()

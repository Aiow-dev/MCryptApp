from PyQt5 import QtCore

from src.components import colors
from src.helpers import tables


class TableAnimation:
    def __init__(self, tbl_wgt, call_time):
        self.__current_row = 0
        self.__current_column = 0
        self.__tbl_wgt = tbl_wgt
        self.__max_row, self.__max_column = tables.table_size(tbl_wgt)
        self.__call_time = call_time
        self.__item_color = colors.Palette.gray.value.to_rgb_q()
        self.__select_color = colors.Palette.select_purple.value.to_rgb_q()
        self.__timer = QtCore.QTimer()
        self.__timer.setInterval(self.__call_time)

    def update_timer(self):
        self.__timer.start()

    def write_column_symbols(self, text_obj):
        chars = text_obj.text()
        self.__timer.timeout.connect(lambda: self._timeout_column_symbols(chars))
        self.__timer.start()

    def read_row_symbols(self, text_obj):
        self.__timer.timeout.connect(lambda: self._timeout_row_symbols(text_obj))
        self.__timer.start()

    def _timeout_column_symbols(self, chars):
        if 0 < self.__current_row < self.__max_row:
            prev_item = self.__tbl_wgt.item(self.__current_row - 1, self.__current_column)
            prev_item.setBackground(self.__item_color)
        if self.__current_row > self.__max_row - 1:
            self.__current_column += 1
            if self.__current_column > self.__max_column - 1:
                item = self.__tbl_wgt.item(self.__current_row - 1, self.__current_column - 1)
                item.setBackground(self.__item_color)
                self.__current_row = 0
                self.__current_column = 0
                self.__timer.stop()
                return
            prev_item = self.__tbl_wgt.item(self.__current_row - 1, self.__current_column - 1)
            prev_item.setBackground(self.__item_color)
            self.__current_row = 0
        item = self.__tbl_wgt.item(self.__current_row, self.__current_column)
        char_index = self.__current_column * self.__max_row + self.__current_row
        item.setBackground(self.__select_color)
        item.setText(chars[char_index])
        self.__current_row += 1

    def _timeout_row_symbols(self, text_obj):
        if 0 < self.__current_column < self.__max_column:
            prev_item = self.__tbl_wgt.item(self.__current_row, self.__current_column - 1)
            prev_item.setBackground(self.__item_color)
        if self.__current_column > self.__max_column - 1:
            self.__current_row += 1
            if self.__current_row > self.__max_row - 1:
                item = self.__tbl_wgt.item(self.__current_row - 1, self.__current_column - 1)
                item.setBackground(self.__item_color)
                self.__current_row = 0
                self.__current_column = 0
                self.__timer.stop()
                return
            prev_item = self.__tbl_wgt.item(self.__current_row - 1, self.__current_column - 1)
            prev_item.setBackground(self.__item_color)
            self.__current_column = 0
        item = self.__tbl_wgt.item(self.__current_row, self.__current_column)
        char = item.text()
        current_text = text_obj.text()
        text_obj.setText(f'{current_text}{char}')
        item.setBackground(self.__select_color)
        self.__current_column += 1


class TimerAnimation:
    def __init__(self, tbl_wgt, call_time):
        self.__row = 0
        self.__column = 0
        self.__tbl_wgt = tbl_wgt
        self.__color = colors.Palette.select_purple.value.to_rgb_q()
        self.__call_time = call_time
        self.__timer = QtCore.QTimer()
        self.__timer.setInterval(self.__call_time)

    def select_columns(self):
        self.__timer.timeout.connect(lambda: self._timeout_columns())
        self.__timer.start()

    def _timeout_columns(self):
        if self.__row > 3:
            self.__row = 0
            self.__column += 1
        if self.__column > 5:
            self.__row = 0
            self.__column = 0
            self.__timer.stop()
        self.__tbl_wgt.item(self.__row, self.__column).setBackground(self.__color)
        self.__row += 1

    def update(self):
        self.__timer.start()

    def _timeout(self):
        print(self.__row, self.__column)
        if self.__row < 4 and self.__column < 6:
            self.__tbl_wgt.item(self.__row, self.__column).setBackground(self.__color)
            self.__row += 1
            self.__column += 1

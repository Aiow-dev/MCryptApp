from PyQt5 import QtCore

from src.components import scheme_colors
from src.helpers import tables


class TableAnimation:
    def __init__(self, tbl_wgt, call_time, after_action):
        self.__current_row = 0
        self.__current_column = 0
        self.__tbl_wgt = tbl_wgt
        self.__after_action = after_action
        self.__max_row, self.__max_column = tables.table_size(tbl_wgt)
        self.__call_time = call_time
        self.__item_bg_color = scheme_colors.tbl_item_bg_default
        self.__item_fg_color = scheme_colors.tbl_item_fg_default
        self.__item_bg_select_color = scheme_colors.tbl_item_bg_select
        self.__item_fg_select_color = scheme_colors.tbl_item_fg_select
        self.__timer = QtCore.QTimer()
        self.__timer.setInterval(self.__call_time)

    def update_timer(self):
        self.__timer.start()

    def write_row_symbols(self, text_obj):
        chars = text_obj.text()
        text_obj.setFocus()
        self.__timer.timeout.connect(lambda: self._timeout_write_row(text_obj, chars))
        self.__timer.start()

    def write_column_symbols(self, text_obj):
        chars = text_obj.text()
        text_obj.setFocus()
        self.__timer.timeout.connect(lambda: self._timeout_write_column(text_obj, chars))
        self.__timer.start()

    def read_row_symbols(self, text_obj):
        text_obj.setFocus()
        self.__timer.timeout.connect(lambda: self._timeout_read_row(text_obj))
        self.__timer.start()

    def read_column_symbols(self, text_obj):
        text_obj.setFocus()
        self.__timer.timeout.connect(lambda: self._timeout_read_column(text_obj))
        self.__timer.start()

    def _timeout_write_row(self, text_obj, chars):
        if 0 < self.__current_column < self.__max_column:
            prev_item = self.__tbl_wgt.item(self.__current_row, self.__current_column - 1)
            prev_item.setBackground(self.__item_bg_color)
            prev_item.setForeground(self.__item_fg_color)
        if self.__current_column > self.__max_column - 1:
            self.__current_row += 1
            if self.__current_row > self.__max_row - 1:
                item = self.__tbl_wgt.item(self.__current_row - 1, self.__current_column - 1)
                item.setBackground(self.__item_bg_color)
                item.setForeground(self.__item_fg_color)
                self.__current_row = 0
                self.__current_column = 0
                text_obj.deselect()
                self.__timer.stop()
                self.__after_action()
                return
            prev_item = self.__tbl_wgt.item(self.__current_row - 1, self.__current_column - 1)
            prev_item.setBackground(self.__item_bg_color)
            prev_item.setForeground(self.__item_fg_color)
            self.__current_column = 0
        item = self.__tbl_wgt.item(self.__current_row, self.__current_column)
        char_index = self.__current_row * self.__max_column + self.__current_column
        text_obj.setSelection(char_index, 1)
        item.setBackground(self.__item_bg_select_color)
        item.setForeground(self.__item_fg_select_color)
        item.setText(chars[char_index])
        self.__current_column += 1

    def _timeout_write_column(self, text_obj, chars):
        if 0 < self.__current_row < self.__max_row:
            prev_item = self.__tbl_wgt.item(self.__current_row - 1, self.__current_column)
            prev_item.setBackground(self.__item_bg_color)
            prev_item.setForeground(self.__item_fg_color)
        if self.__current_row > self.__max_row - 1:
            self.__current_column += 1
            if self.__current_column > self.__max_column - 1:
                item = self.__tbl_wgt.item(self.__current_row - 1, self.__current_column - 1)
                item.setBackground(self.__item_bg_color)
                item.setForeground(self.__item_fg_color)
                self.__current_row = 0
                self.__current_column = 0
                text_obj.deselect()
                self.__timer.stop()
                self.__after_action()
                return
            prev_item = self.__tbl_wgt.item(self.__current_row - 1, self.__current_column - 1)
            prev_item.setBackground(self.__item_bg_color)
            prev_item.setForeground(self.__item_fg_color)
            self.__current_row = 0
        item = self.__tbl_wgt.item(self.__current_row, self.__current_column)
        char_index = self.__current_column * self.__max_row + self.__current_row
        text_obj.setSelection(char_index, 1)
        item.setBackground(self.__item_bg_select_color)
        item.setForeground(self.__item_fg_select_color)
        item.setText(chars[char_index])
        self.__current_row += 1

    def _timeout_read_row(self, text_obj):
        if 0 < self.__current_column < self.__max_column:
            prev_item = self.__tbl_wgt.item(self.__current_row, self.__current_column - 1)
            prev_item.setBackground(self.__item_bg_color)
            prev_item.setForeground(self.__item_fg_color)
        if self.__current_column > self.__max_column - 1:
            self.__current_row += 1
            if self.__current_row > self.__max_row - 1:
                item = self.__tbl_wgt.item(self.__current_row - 1, self.__current_column - 1)
                item.setBackground(self.__item_bg_color)
                item.setForeground(self.__item_fg_color)
                self.__current_row = 0
                self.__current_column = 0
                text_obj.deselect()
                self.__timer.stop()
                self.__after_action()
                return
            prev_item = self.__tbl_wgt.item(self.__current_row - 1, self.__current_column - 1)
            prev_item.setBackground(self.__item_bg_color)
            prev_item.setForeground(self.__item_fg_color)
            self.__current_column = 0
        item = self.__tbl_wgt.item(self.__current_row, self.__current_column)
        char = item.text()
        char_index = self.__current_row * self.__max_column + self.__current_column
        current_text = text_obj.text()
        text_obj.setText(f'{current_text}{char}')
        text_obj.setSelection(char_index, 1)
        item.setBackground(self.__item_bg_select_color)
        item.setForeground(self.__item_fg_select_color)
        self.__current_column += 1

    def _timeout_read_column(self, text_obj):
        if 0 < self.__current_row < self.__max_row:
            prev_item = self.__tbl_wgt.item(self.__current_row - 1, self.__current_column)
            prev_item.setBackground(self.__item_bg_color)
            prev_item.setForeground(self.__item_fg_color)
        if self.__current_row > self.__max_row - 1:
            self.__current_column += 1
            if self.__current_column > self.__max_column - 1:
                item = self.__tbl_wgt.item(self.__current_row - 1, self.__current_column - 1)
                item.setBackground(self.__item_bg_color)
                item.setForeground(self.__item_fg_color)
                self.__current_row = 0
                self.__current_column = 0
                text_obj.deselect()
                self.__timer.stop()
                self.__after_action()
                return
            prev_item = self.__tbl_wgt.item(self.__current_row - 1, self.__current_column - 1)
            prev_item.setBackground(self.__item_bg_color)
            prev_item.setForeground(self.__item_fg_color)
            self.__current_row = 0
        item = self.__tbl_wgt.item(self.__current_row, self.__current_column)
        char_index = self.__current_column * self.__max_row + self.__current_row
        char = item.text()
        current_text = text_obj.text()
        text_obj.setText(f'{current_text}{char}')
        text_obj.setSelection(char_index, 1)
        item.setBackground(self.__item_bg_select_color)
        item.setForeground(self.__item_fg_select_color)
        self.__current_row += 1

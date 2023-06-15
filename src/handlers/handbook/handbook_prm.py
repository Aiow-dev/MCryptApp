from PyQt5 import QtWidgets


from src.helpers import items, tables, text, time
from src.components import dialogs, enc_tables
from src.handlers import messages
from src.events import animation


def proc_handbook_row_smp(form):
    try:
        msg = form['msg_input'].text().replace(' ', '').upper()
        len_msg = len(msg)
        if len_msg > 0:
            if multipliers := items.get_multipliers(len_msg):
                form['msg_input'].setText(msg)
                rows, columns = items.couple_multipliers(multipliers)
                time.block_element_time(form['btn_row_input'], 500 * (rows * columns + 1))
                time.block_element_time(form['btn_clm_input'], 500 * (rows * columns + 1))
                form['rows_input'].setText(str(rows))
                form['columns_input'].setText(str(columns))
                form['tbl_row_wgt'].setRowCount(rows)
                form['tbl_row_wgt'].setColumnCount(columns)
                form['tbl_clm_wgt'].setRowCount(rows)
                form['tbl_clm_wgt'].setColumnCount(columns)
                tables.set_table_empty_items(form['tbl_row_wgt'])
                tables.set_table_empty_items(form['tbl_clm_wgt'])

                timer = animation.TableAnimation(form['tbl_row_wgt'], 500)
                timer.write_column_symbols(form['msg_input'])
                msg_blocks = text.get_text_blocks(msg, rows, columns)
                if len(msg_blocks) > 0:
                    tables.table(msg_blocks, enc_tables.table_column, form['tbl_clm_wgt'])
            else:
                dialogs.show_err_msg(messages.MSG_MULTIPLICATION_LEN_ERR, 'Ошибка')
        else:
            dialogs.show_err_msg('Сообщение не заполнено!', 'Ошибка')
    except AttributeError as attribute_error:
        dialogs.show_err_msg('Не удалось выполнить операцию!', 'Ошибка')


def proc_handbook_clm_smp(form):
    try:
        form['msg_input'].setText('')
        if not items.is_empty_table_text(form['tbl_wgt']):
            rows, columns = tables.table_size(form['tbl_wgt'])
            time.block_element_time(form['btn_clm_input'], 500 * (rows * columns + 1))
            time.block_element_time(form['btn_row_input'], 500 * (rows * columns + 1))
            timer = animation.TableAnimation(form['tbl_wgt'], 500)
            timer.read_row_symbols(form['msg_input'])
        else:
            dialogs.show_err_msg('Ошибка. Таблица перестановок не заполнена. Убедитесь, что вы выполнили шаг 1!', 'Ошибка')
    except AttributeError as attribute_error:
        dialogs.show_err_msg('Не удалось выполнить операцию!', 'Ошибка')

from src.helpers import items, tables, text
from src.components import dialogs, enc_tables
from src.handlers import messages
from src.events import animation
from src.scripts.encryption import prm


def enable_buttons(form):
    form['btn_write'].setDisabled(False)
    form['btn_read'].setDisabled(False)


def disable_buttons(form):
    form['btn_write'].setEnabled(False)
    form['btn_read'].setEnabled(False)


def proc_handbook_write_smp(form, animation_function, read_function):
    try:
        msg = form['in_input'].text().replace(' ', '').upper()
        rows = int(form['rows_input'].text())
        columns = int(form['columns_input'].text())
        if err_msg := prm.check_simple_prm(msg, rows, columns).get('err_msg'):
            dialogs.show_err_msg(err_msg, 'Ошибка')
            return

        form['in_input'].setText(msg)
        form['rows_input'].setText(str(rows))
        form['columns_input'].setText(str(columns))
        form['tbl_write_wgt'].setRowCount(rows)
        form['tbl_write_wgt'].setColumnCount(columns)
        form['tbl_read_wgt'].setRowCount(rows)
        form['tbl_read_wgt'].setColumnCount(columns)
        tables.set_table_empty_items(form['tbl_write_wgt'])
        tables.set_table_empty_items(form['tbl_read_wgt'])
        disable_buttons(form)

        animation_function()
        read_function()
    except ValueError as value_error:
        dialogs.show_err_msg('Параметры шифрования не соответствуют требуемым!', 'Ошибка')
    except AttributeError as attribute_error:
        dialogs.show_err_msg('Не удалось выполнить операцию!', 'Ошибка')


def after_enc_read_smp(form):
    enable_buttons(form)
    form['dec_in_input'].setText(form['out_input'].text())
    form['dec_rows_input'].setText(form['rows_input'].text())
    form['dec_columns_input'].setText(form['columns_input'].text())


def write_column_animation(form):
    timer = animation.TableAnimation(form['tbl_write_wgt'], 500, lambda: enable_buttons(form))
    timer.write_column_symbols(form['in_input'])


def write_row_animation(form):
    timer = animation.TableAnimation(form['tbl_write_wgt'], 500, lambda: enable_buttons(form))
    timer.write_row_symbols(form['in_input'])


def read_row_animation(form):
    timer = animation.TableAnimation(form['tbl_read_wgt'], 500, lambda: after_enc_read_smp(form))
    timer.read_row_symbols(form['out_input'])


def read_column_animation(form):
    timer = animation.TableAnimation(form['tbl_read_wgt'], 500, lambda: enable_buttons(form))
    timer.read_column_symbols(form['out_input'])


def proc_handbook_enc_write_smp(form):
    proc_handbook_write_smp(form, lambda: write_column_animation(form), lambda: handbook_enc_read_smp(form))


def handbook_enc_read_smp(form):
    msg = form['in_input'].text()
    rows = int(form['rows_input'].text())
    columns = int(form['columns_input'].text())
    msg_blocks = text.get_text_blocks(msg, rows, columns)
    if len(msg_blocks) > 0:
        tables.table(msg_blocks, enc_tables.table_column, form['tbl_read_wgt'])
    else:
        dialogs.show_err_msg(messages.MSG_MULTIPLICATION_LEN_ERR, 'Ошибка')


def proc_handbook_dec_write_smp(form):
    proc_handbook_write_smp(form, lambda: write_row_animation(form), lambda: handbook_dec_read_smp(form))


def handbook_dec_read_smp(form):
    msg = form['in_input'].text()
    rows = int(form['rows_input'].text())
    columns = int(form['columns_input'].text())
    msg_blocks = text.get_text_blocks(msg, columns, rows)
    if len(msg_blocks) > 0:
        tables.table(msg_blocks, enc_tables.table_row, form['tbl_read_wgt'])
    else:
        dialogs.show_err_msg(messages.MSG_MULTIPLICATION_LEN_ERR, 'Ошибка')


def proc_handbook_read_smp(form, animation_function):
    try:
        form['out_input'].setText('')
        if not items.is_empty_table_text(form['tbl_read_wgt']):
            disable_buttons(form)
            animation_function()


        else:
            dialogs.show_err_msg('Ошибка. Таблица перестановок не заполнена. Убедитесь, что вы выполнили шаг 1!', 'Ошибка')
    except AttributeError as attribute_error:
        dialogs.show_err_msg('Не удалось выполнить операцию!', 'Ошибка')


def proc_handbook_enc_read_smp(form):
    proc_handbook_read_smp(form, lambda: read_row_animation(form))


def proc_handbook_dec_read_smp(form):
    proc_handbook_read_smp(form, lambda: read_column_animation(form))

from src.components import dialogs


def show_program_info():
    txt = 'MCrypt 1.9.1 Preview\nMCryptTeam, 2023, все права защищены'
    dialogs.show_info_msg(txt, 'Информация о программе')

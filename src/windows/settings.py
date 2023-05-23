from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from src.views import settings_win_dark, settings_win_light
from src.components import visual, setting, win_palette
from src.controllers import (
    set_app_controllers,
    menu_line_controllers,
    program_info_controllers,
    quick_panel_controllers,
    tab_controllers,
    color_style_controllers
)
from src.helpers import time, win


class SettingsWindow(QtWidgets.QWidget):
    def __init__(self, func_single, parent, flags):
        self.__func_single = func_single
        super().__init__(parent, flags)

    def show(self):
        if self.__func_single.is_call():
            super().show()

    def closeEvent(self, event):
        self.__func_single.reset()
        super().closeEvent(event)


def switch_settings_page(ui, index):
    return lambda: ui.section_widget.setCurrentIndex(index)


def init_settings_styles(ui):
    accent = win_palette.win_accent_converted()
    complementary = win_palette.win_complementary_converted(accent)
    win_palette.accent_color = accent.to_rgb_str()
    win_palette.complementary_color = complementary.to_rgb_str()
    visual.frame_compl_color_style_sys(ui.compl_light_win_color)
    visual.frame_compl_color_style_sys(ui.compl_dark_win_color)
    visual.frame_color_style_sys(ui.accent_light_win_color)
    visual.frame_color_style_sys(ui.accent_dark_win_color)


def init_push_btn_sys_styles(ui):
    push_btn_list = [ui.ext_info_btn, ui.light_btn, ui.dark_btn,
                     ui.win_btn, ui.time_color_btn, ui.btn_restart,
                     ui.btn_quit, ui.menu_style_btn, ui.menu_color_style_btn,
                     ui.tab_corner_btn, ui.tab_radius_btn, ui.tab_top_radius_btn,
                     ui.tab_corner_radius_btn, ui.help_open_btn]
    for push_btn in push_btn_list:
        visual.push_btn_sys(push_btn)


def init_panel_sys_styles(is_light, ui):
    push_btn_list = [ui.btn_program_info, ui.btn_color_style, ui.btn_app_set,
                     ui.btn_line_menu, ui.btn_quick_panel, ui.btn_tab,
                     ui.btn_help_set, ui.btn_privacy_policy]
    visual_function = visual.panel_push_btn_light_sys if is_light else visual.panel_push_btn_dark_sys
    for push_btn in push_btn_list:
        visual_function(push_btn)


def init_label_back_sys_styles(is_light, ui):
    visual_function = visual.label_back_light_sys if is_light else visual.label_back_dark_sys
    visual_function(ui.menu_bar_style_lbl)
    visual_function(ui.menu_bar_style_lbl_2)


def init_settings_win_styles(is_light, ui):
    accent = win_palette.win_accent_converted()
    complementary = win_palette.win_complementary_converted(accent)
    win_palette.accent_color = accent.to_rgb_str()
    win_palette.complementary_color = complementary.to_rgb_str()

    init_panel_sys_styles(is_light, ui)
    init_label_back_sys_styles(is_light, ui)
    init_push_btn_sys_styles(ui)
    visual.frame_bottom_color_sys(ui.menu_bar_color_style_frame)

    if is_light:
        visual.check_box_light_sys(ui.confirm_quit_chk)
        visual.check_box_light_sys(ui.menu_line_chk)
        visual.check_box_light_sys(ui.quick_panel_chk)
        visual.tab_set_light_sys(ui.tab_corner_wgt)
        visual.tab_set_light_sys_rad(ui.tab_radius_wgt)
        visual.tab_set_light_sys_top_rad(ui.tab_top_radius_wgt)
        visual.tab_set_light_sys_corn_rad(ui.tab_corner_radius_wgt)
        visual.frame_bottom_sys(ui.menu_bar_style_frame)
    else:
        visual.tab_set_dark_sys(ui.tab_corner_wgt)
        visual.tab_set_dark_sys_rad(ui.tab_radius_wgt)
        visual.tab_set_dark_sys_top_rad(ui.tab_top_radius_wgt)
        visual.tab_set_dark_sys_corn_rad(ui.tab_corner_radius_wgt)


def active_color_style_win(ui):
    ui.light_style_frame.setVisible(False)
    ui.dark_style_frame.setVisible(False)
    ui.time_color_style_frame.setVisible(False)
    ui.system_style_frame.setVisible(True)


def active_color_style_time(ui):
    ui.light_style_frame.setVisible(False)
    ui.dark_style_frame.setVisible(False)
    ui.system_style_frame.setVisible(False)
    ui.time_color_style_frame.setVisible(True)


def active_color_style(theme_window, ui):
    if theme_window == 'light':
        ui.dark_style_frame.setVisible(False)
    else:
        ui.light_style_frame.setVisible(False)
    ui.system_style_frame.setVisible(False)
    ui.time_color_style_frame.setVisible(False)


def active_tab_style(tab_style, ui):
    if tab_style == 'corner':
        ui.tab_radius_frame.setVisible(False)
        ui.tab_top_radius_frame.setVisible(False)
        ui.tab_corner_radius_frame.setVisible(False)
    elif tab_style == 'radius':
        ui.tab_corner_frame.setVisible(False)
        ui.tab_top_radius_frame.setVisible(False)
        ui.tab_corner_radius_frame.setVisible(False)
    elif tab_style == 'top-radius':
        ui.tab_corner_frame.setVisible(False)
        ui.tab_radius_frame.setVisible(False)
        ui.tab_corner_radius_frame.setVisible(False)
    else:
        ui.tab_corner_frame.setVisible(False)
        ui.tab_radius_frame.setVisible(False)
        ui.tab_top_radius_frame.setVisible(False)


def active_menu_style(menu_style, ui):
    if menu_style == 'transparent':
        ui.menu_color_style_frame.setVisible(False)
    else:
        ui.menu_style_frame.setVisible(False)


def init_settings_panel(ui):
    ui.btn_program_info.clicked.connect(switch_settings_page(ui, 0))
    ui.btn_color_style.clicked.connect(switch_settings_page(ui, 1))
    ui.btn_app_set.clicked.connect(switch_settings_page(ui, 2))
    ui.btn_line_menu.clicked.connect(switch_settings_page(ui, 3))
    ui.btn_quick_panel.clicked.connect(switch_settings_page(ui, 4))
    ui.btn_tab.clicked.connect(switch_settings_page(ui, 5))
    ui.btn_help_set.clicked.connect(switch_settings_page(ui, 6))
    ui.btn_privacy_policy.clicked.connect(switch_settings_page(ui, 7))


def init_settings_pages(parent, ui):
    color_style_controllers.init_color_styles(ui)
    set_app_controllers.init_confirm_quit(parent, ui)
    quick_panel_controllers.init_quick_panel(ui)
    menu_line_controllers.init_menu_line(parent, ui)
    program_info_controllers.init_program_info(parent, ui)
    tab_controllers.init_tab_style(ui)


def show_settings_window(func_single, parent):
    form = SettingsWindow(func_single, parent, Qt.Window)
    form.setFixedSize(1060, 780)
    theme = setting.get_parameter('theme')
    if theme == 'system':
        is_light = win.is_light_win_theme()
        ui = settings_win_dark.Ui_settings_form()
        if is_light:
            ui = settings_win_light.Ui_settings_form()
        ui.setupUi(form)
        init_settings_win_styles(is_light, ui)
        active_color_style_win(ui)
    elif theme == 'time':
        current_hour = time.get_current_hour()
        ui = settings_win_dark.Ui_settings_form()
        if 5 < current_hour < 18:
            ui = settings_win_light.Ui_settings_form()
        ui.setupUi(form)
        active_color_style_time(ui)
    else:
        ui = settings_win_dark.Ui_settings_form()
        if theme == 'light':
            ui = settings_win_light.Ui_settings_form()
        ui.setupUi(form)
        active_color_style(theme, ui)
    tab_style = setting.get_parameter('tab-style')
    active_tab_style(tab_style, ui)
    menu_style = setting.get_parameter('menu-style')
    active_menu_style(menu_style, ui)
    init_settings_styles(ui)
    init_settings_panel(ui)
    init_settings_pages(form, ui)
    form.show()

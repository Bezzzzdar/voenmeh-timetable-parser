# main.py - main file of timetable-parser application
# Copyright (C) 2024 Ivan Rastegaev
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

from parser import parse_timetable
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QPushButton,QWidget, QLineEdit, QSpacerItem, QSizePolicy, QComboBox 
from PyQt5.QtCore import Qt, QSettings

from icons import _get_icon_from_base64, base64_update_button_icon_white, base64_edit_button_icon_white, base64_app_icon

import json
import os
from pathlib import Path
import datetime

from timetable_widgets import EvenWeekTimetableScrollArea, OddWeekTimetableScrollArea, LessonWidget, _is_even_week, semester_start_date

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.settings = QSettings("Company", "TimetableApp")
        self.__initUI()
    def __initUI(self):
        """ Initialazing main window"""

        self.setWindowTitle("BSTU Voenmeh Timetable")
        window_icon, _, = _get_icon_from_base64(base64_app_icon, 64, 64)
        self.setWindowIcon(window_icon)
        self.setFixedSize(500, 700)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #293133;
            }
        """)
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.top_layout = QHBoxLayout()

        # button for update timetable
        self.update_timetable_button = QPushButton("", self)
        update_timetable_button_icon, update_timetable_button_icon_size = _get_icon_from_base64(base64_update_button_icon_white, 40, 40)
        self.update_timetable_button.setIcon(update_timetable_button_icon)
        self.update_timetable_button.setIconSize(update_timetable_button_icon_size)
        self.update_timetable_button.setStyleSheet("""
            QPushButton {
                background-color: #293133;
                height: 20px;
                width: 20px;
                border: none;
                padding: 10px;
                border-radius: 20px;
            }
            QPushButton:hover {
                background-color:  #4E5754;
            }
        """)
        self.update_timetable_button.clicked.connect(self.update_timetable)
        self.top_layout.addWidget(self.update_timetable_button)

        # text field for group number
        self.group_number_input = QLineEdit(self)
        self.group_number_input.setPlaceholderText("Номер группы")
        self.group_number_input.setStyleSheet("""
            QLineEdit {
                font-size: 16px;
                color: white;
                height: 18px;
                width: 200px;
                background-color: #4E5754;
                border: 1px solid #4C514A;
                border-radius: 5px;
                padding: 10px;
            }
        """)
        self.top_layout.addWidget(self.group_number_input)
        
        # combo box for select weekcode
        self.week_combo_box = QComboBox(self)
        self.week_combo_box.addItem("Чётная неделя")
        self.week_combo_box.addItem("Нечётная неделя")
        self.week_combo_box.currentIndexChanged.connect(self.week_changed)
        self.week_combo_box.setStyleSheet("""
            QComboBox {
                font-size: 16px;
                color: white;
                height: 18px;
                width: 200px;
                background-color: #4E5754;
                border: 1px solid #4C514A;
                border-radius: 5px;
                padding: 10px;
            }
            QComboBox::drop-down {
                border-radius: 2px solid #4C514A;
                background-color: #4E5754;
            }
            QComboBox QAbstractItemView {
                border-radius: 2px solid #4C514A;
                selection-background-color: #4E5754;
                background-color: #4E5754;
                color: white;
            }
            QComboBox QAbstractItemView::item {
                padding: 5px;
            }
        """)
        self.top_layout.addWidget(self.week_combo_box)

        # button for editting timetable
        self.edit_timetable_button = QPushButton("", self)
        edit_timetable_button_icon, edit_timetable_button_icon_size = _get_icon_from_base64(base64_edit_button_icon_white, 35, 35)
        self.edit_timetable_button.setIcon(edit_timetable_button_icon)
        self.edit_timetable_button.setIconSize(edit_timetable_button_icon_size)
        self.edit_timetable_button.setStyleSheet("""
            QPushButton {
                background-color: #293133;
                height: 20px;
                width: 20px;
                border: none;
                padding: 10px;
                border-radius: 20px;
            }
            QPushButton:hover {
                background-color:  #4E5754;
            }
        """)
        # self.edit_timetable_button.clicked.connect(self.update_timetable)
        self.top_layout.addWidget(self.edit_timetable_button)

        self.top_layout.setAlignment(Qt.AlignTop)
        self.layout.addLayout(self.top_layout)

        try:
            self.group_number = self.settings.value('last_group_number')
            self.group_number_input.setText(self.group_number)

            if self.group_number == '':
                return
            
            if not os.path.exists(Path(f'./app/saved_timetables/{self.group_number}_timetable.json')):
                parse_timetable(self.group_number)

            with open(Path(f'./app/saved_timetables/{self.group_number}_timetable.json'), 'r', encoding='utf-8') as json_file:
                self.timetable = json.load(json_file)

            self.timetable_widget_even = EvenWeekTimetableScrollArea(self, self.timetable)
            self.timetable_widget_odd = OddWeekTimetableScrollArea(self, self.timetable)
            self.set_current_week()

            self.layout.addWidget(self.timetable_widget_even)
            self.layout.addWidget(self.timetable_widget_odd)
        except:
            pass

    def set_current_week(self):
        is_even = _is_even_week(semester_start_date)
        if is_even:
            self.timetable_widget_odd.hide()
            self.week_combo_box.setCurrentText('Чётная неделя')
        else:
            self.timetable_widget_even.hide()
            self.week_combo_box.setCurrentText('Нечётная неделя')
    
    def week_changed(self):
        selected_week = self.week_combo_box.currentText()
        if selected_week == "Чётная неделя":
            self.timetable_widget_odd.hide()
            self.timetable_widget_even.show()
        elif selected_week == "Нечётная неделя":
            self.timetable_widget_even.hide()
            self.timetable_widget_odd.show()


    def update_timetable(self):
        try:
            self.timetable_widget_even.hide()
            self.timetable_widget_odd.hide()

            self.timetable_widget_even.destroy()
            self.timetable_widget_odd.destroy()
        except:
            pass

        self.group_number = self.group_number_input.text()
        if self.group_number == '':
            return

        if not os.path.exists(Path(f'./app/saved_timetables/{self.group_number}_timetable.json')):
            parse_timetable(self.group_number)

        with open(Path(f'./app/saved_timetables/{self.group_number}_timetable.json'), 'r', encoding='utf-8') as json_file:
            self.timetable = json.load(json_file)

        self.timetable_widget_even = EvenWeekTimetableScrollArea(self, self.timetable)
        self.timetable_widget_odd = OddWeekTimetableScrollArea(self, self.timetable)

        self.set_current_week()

        self.layout.addWidget(self.timetable_widget_even)
        self.layout.addWidget(self.timetable_widget_odd)

    def closeEvent(self, event):
        self.settings.setValue('last_group_number', f'{self.group_number}')
        super().closeEvent(event)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

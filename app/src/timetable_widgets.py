# timetable_widgets.py - widgets with timetable and lessons
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

from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QSpacerItem, QSizePolicy,QScrollArea, QLabel, QFrame, QDialog
from PyQt5.QtCore import Qt
import datetime

class LessonWidget(QDialog):
    def __init__(self, parent, name, type, lecturer, classroom, weekcode, day_of_week, start_time, end_time):
        super().__init__(parent)
        self.name = name
        self.type = type
        if self.type == "Лекция":
            self.vline_color = 'red'
        elif self.type == "Практика":
            self.vline_color = 'green'
        elif self.type == "Лабораторная":
            self.vline_color = 'blue'
        self.lecturer = lecturer
        self.classroom = classroom
        self.weekcode = weekcode
        self.day_of_week = day_of_week
        self.start_time = start_time
        self.end_time = end_time
        self.__initUI()
    
    def __initUI(self):
        self.setFixedSize(440, 60)
        self.setStyleSheet("""
            QDialog {
                background-color: #434B4D;
                border-radius: 5px;
            }
        """)
        self.layout = QHBoxLayout()

        self.time_label = QLabel(f'{self.start_time}\n{self.end_time}', self)
        self.time_label.setStyleSheet("""
            QLabel {
                font-size: 14px;
                text-align: center;
                color: white;
                background-color: #434B4D;
            }
        """)
        self.layout.addWidget(self.time_label)

        self.vline = QFrame()
        self.vline.setFrameShape(QFrame.VLine)
        self.vline.setFrameShadow(QFrame.Sunken)
        self.vline.setStyleSheet(f"background-color: {self.vline_color};")
        self.layout.addWidget(self.vline)

        self.lesson_label = QLabel(f'{self.name}\n{self.classroom}, {self.type}', self)
        self.lesson_label.setStyleSheet("""
            QLabel {
                font-size: 14px;
                color: white;
                background-color: #434B4D;
            }
        """)
        self.lesson_label.setFixedSize(150, 40)
        self.layout.addWidget(self.lesson_label)

        separator = QSpacerItem(50, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.layout.addItem(separator)

        self.lecturer_label = QLabel(f'{self.lecturer}', self)
        self.lecturer_label.setStyleSheet("""
            QLabel {
                font-size: 14px;
                color: white;
                background-color: #434B4D;
            }
        """)
        self.layout.addWidget(self.lecturer_label)
        self.setLayout(self.layout)

class EvenWeekTimetableScrollArea(QScrollArea):
    def __init__(self, parent, timetable):
        super().__init__(parent)
        self.__initUI(timetable)

    def __initUI(self, timetable):
        self.setStyleSheet("""
            QWidget {
                background-color: #293133;
                border: none;
            }
        """)
        self.content_widget = QWidget()
        self.layout = QVBoxLayout()

        days_of_week = []
        current_week, _ = _get_week_dates()
        
        self.monday_layout = QVBoxLayout()
        self.monday_selection = QLabel(f'Понедельник, {current_week[0]}', self)
        self.monday_selection.setStyleSheet("""
            QLabel {
                font-size: 16px;
                color: white;
            }
        """)
        self.monday_layout.addWidget(self.monday_selection)
        days_of_week.append(self.monday_layout)

        self.tuesday_layout = QVBoxLayout()
        self.tuesday_selection = QLabel(f'Вторник, {current_week[0] + datetime.timedelta(days=1)}', self)
        self.tuesday_selection.setStyleSheet("""
            QLabel {
                font-size: 16px;
                color: white;
            }
        """)
        self.tuesday_layout.addWidget(self.tuesday_selection)
        days_of_week.append(self.tuesday_layout)

        self.wednesday_layout = QVBoxLayout()
        self.wednesday_selection = QLabel(f'Среда, {current_week[0] + datetime.timedelta(days=2)}', self)
        self.wednesday_selection.setStyleSheet("""
            QLabel {
                font-size: 16px;
                color: white;
            }
        """)
        self.wednesday_layout.addWidget(self.wednesday_selection)
        days_of_week.append(self.wednesday_layout)

        self.thursday_layout = QVBoxLayout()
        self.thursday_selection = QLabel(f'Четверг, {current_week[0] + datetime.timedelta(days=3)}', self)
        self.thursday_selection.setStyleSheet("""
            QLabel {
                font-size: 16px;
                color: white;
            }
        """)
        self.thursday_layout.addWidget(self.thursday_selection)
        days_of_week.append(self.thursday_layout)

        self.friday_layout = QVBoxLayout()
        self.friday_selection = QLabel(f'Пятница, {current_week[0] + datetime.timedelta(days=4)}', self)
        self.friday_selection.setStyleSheet("""
            QLabel {
                font-size: 16px;
                color: white;
            }
        """)
        self.friday_layout.addWidget(self.friday_selection)
        days_of_week.append(self.friday_layout)

        self.saturday_layout = QVBoxLayout()
        self.saturday_selection = QLabel(f'Суббота, {current_week[0] + datetime.timedelta(days=5)}', self)
        self.saturday_selection.setStyleSheet("""
            QLabel {
                font-size: 16px;
                color: white;
            }
        """)
        self.saturday_layout.addWidget(self.saturday_selection)
        days_of_week.append(self.saturday_layout)

        self.layout.addLayout(self.monday_layout)
        self.layout.addLayout(self.tuesday_layout)
        self.layout.addLayout(self.wednesday_layout)
        self.layout.addLayout(self.thursday_layout)
        self.layout.addLayout(self.friday_layout)
        self.layout.addLayout(self.saturday_layout)

        for day, lessons in timetable.items():
            for lesson_info in lessons:
                for lesson_name, details in lesson_info['lesson'].items():
                    for detail in details:
                        self.lesson_widget = LessonWidget(
                        parent=self,
                        name=lesson_name,
                        type=detail['discipline_type'],
                        lecturer=detail['lecturer'],
                        classroom=detail['classroom'],
                        weekcode=detail['week_code'],
                        day_of_week=detail['day_of_week'],
                        start_time=detail['start_time'],
                        end_time=detail['end_time']
                    )
                    if self.lesson_widget.weekcode == 2:
                        if self.lesson_widget.day_of_week == 'Понедельник':
                            days_of_week[0].addWidget(self.lesson_widget)
                        if self.lesson_widget.day_of_week == 'Вторник':
                            days_of_week[1].addWidget(self.lesson_widget)
                        if self.lesson_widget.day_of_week == 'Среда':
                            days_of_week[2].addWidget(self.lesson_widget)
                        if self.lesson_widget.day_of_week == 'Четверг':
                            days_of_week[3].addWidget(self.lesson_widget)
                        if self.lesson_widget.day_of_week == 'Пятница':
                            days_of_week[4].addWidget(self.lesson_widget)
                        if self.lesson_widget.day_of_week == 'Суббота':
                            days_of_week[5].addWidget(self.lesson_widget)

        self.content_widget.setLayout(self.layout)
        self.setWidget(self.content_widget)
        self.setWidgetResizable(True)

class OddWeekTimetableScrollArea(QScrollArea):
    def __init__(self, parent, timetable):
        super().__init__(parent)
        self.__initUI(timetable)

    def __initUI(self, timetable):
        self.setStyleSheet("""
            QWidget {
                background-color: #293133;
                border: none;
            }
        """)
        self.content_widget = QWidget()
        self.layout = QVBoxLayout()

        days_of_week = []
        _, next_week = _get_week_dates()
        
        self.monday_layout = QVBoxLayout()
        self.monday_selection = QLabel(f'Понедельник, {next_week[0]}', self)
        self.monday_selection.setStyleSheet("""
            QLabel {
                font-size: 16px;
                color: white;
            }
        """)
        self.monday_layout.addWidget(self.monday_selection)
        days_of_week.append(self.monday_layout)

        self.tuesday_layout = QVBoxLayout()
        self.tuesday_selection = QLabel(f'Вторник, {next_week[0] + datetime.timedelta(days=1)}', self)
        self.tuesday_selection.setStyleSheet("""
            QLabel {
                font-size: 16px;
                color: white;
            }
        """)
        self.tuesday_layout.addWidget(self.tuesday_selection)
        days_of_week.append(self.tuesday_layout)

        self.wednesday_layout = QVBoxLayout()
        self.wednesday_selection = QLabel(f'Среда, {next_week[0] + datetime.timedelta(days=2)}', self)
        self.wednesday_selection.setStyleSheet("""
            QLabel {
                font-size: 16px;
                color: white;
            }
        """)
        self.wednesday_layout.addWidget(self.wednesday_selection)
        days_of_week.append(self.wednesday_layout)

        self.thursday_layout = QVBoxLayout()
        self.thursday_selection = QLabel(f'Четверг, {next_week[0] + datetime.timedelta(days=3)}', self)
        self.thursday_selection.setStyleSheet("""
            QLabel {
                font-size: 16px;
                color: white;
            }
        """)
        self.thursday_layout.addWidget(self.thursday_selection)
        days_of_week.append(self.thursday_layout)

        self.friday_layout = QVBoxLayout()
        self.friday_selection = QLabel(f'Пятница, {next_week[0] + datetime.timedelta(days=4)}', self)
        self.friday_selection.setStyleSheet("""
            QLabel {
                font-size: 16px;
                color: white;
            }
        """)
        self.friday_layout.addWidget(self.friday_selection)
        days_of_week.append(self.friday_layout)

        self.saturday_layout = QVBoxLayout()
        self.saturday_selection = QLabel(f'Суббота, {next_week[0] + datetime.timedelta(days=5)}', self)
        self.saturday_selection.setStyleSheet("""
            QLabel {
                font-size: 16px;
                color: white;
            }
        """)
        self.saturday_layout.addWidget(self.saturday_selection)
        days_of_week.append(self.saturday_layout)

        self.layout.addLayout(self.monday_layout)
        self.layout.addLayout(self.tuesday_layout)
        self.layout.addLayout(self.wednesday_layout)
        self.layout.addLayout(self.thursday_layout)
        self.layout.addLayout(self.friday_layout)
        self.layout.addLayout(self.saturday_layout)

        for day, lessons in timetable.items():
            for lesson_info in lessons:
                for lesson_name, details in lesson_info['lesson'].items():
                    for detail in details:
                        self.lesson_widget = LessonWidget(
                        parent=self,
                        name=lesson_name,
                        type=detail['discipline_type'],
                        lecturer=detail['lecturer'],
                        classroom=detail['classroom'],
                        weekcode=detail['week_code'],
                        day_of_week=detail['day_of_week'],
                        start_time=detail['start_time'],
                        end_time=detail['end_time']
                    )
                    if self.lesson_widget.weekcode == 1:
                        if self.lesson_widget.day_of_week == 'Понедельник':
                            days_of_week[0].addWidget(self.lesson_widget)
                        if self.lesson_widget.day_of_week == 'Вторник':
                            days_of_week[1].addWidget(self.lesson_widget)
                        if self.lesson_widget.day_of_week == 'Среда':
                            days_of_week[2].addWidget(self.lesson_widget)
                        if self.lesson_widget.day_of_week == 'Четверг':
                            days_of_week[3].addWidget(self.lesson_widget)
                        if self.lesson_widget.day_of_week == 'Пятница':
                            days_of_week[4].addWidget(self.lesson_widget)
                        if self.lesson_widget.day_of_week == 'Суббота':
                            days_of_week[5].addWidget(self.lesson_widget)

        self.content_widget.setLayout(self.layout)
        self.setWidget(self.content_widget)
        self.setWidgetResizable(True)

def _get_week_dates(reference_date=None):
    if reference_date is None:
        reference_date = datetime.date.today()

    # Определяем день недели для reference_date (0 = понедельник, 6 = воскресенье)
    current_weekday = reference_date.weekday()

    # Определяем начало и конец текущей недели
    start_of_current_week = reference_date - datetime.timedelta(days=current_weekday)
    end_of_current_week = start_of_current_week + datetime.timedelta(days=6)

    # Определяем начало и конец следующей недели
    start_of_next_week = start_of_current_week + datetime.timedelta(days=7)
    end_of_next_week = start_of_next_week + datetime.timedelta(days=6)

    current_week = [start_of_current_week, end_of_current_week]
    next_week = [start_of_next_week, end_of_next_week]

    return current_week, next_week

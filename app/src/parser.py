# parser.py - parser for timetable from Voenmeh's official site
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

import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import re
import json
from pathlib import Path

class Lesson():
    def __init__(self, name: str, type: str, lecturer: str, classroom: str, weekcode: int, day_of_week: list[str], start_time: timedelta) -> None:
        self.name = name
        if type == "лек":
            self.color = "red"
            self.type = "Лекция"
        elif type == "пр":
            self.color = "green"
            self.type = "Практика"
        elif type == "лаб":
            self.color = "blue"
            self.type = "Лабораторная"
        else:
            raise TypeError(f'{type} - not supported lesson type')
        
        self.lecturer = lecturer
        self.classroom = classroom

        if weekcode == 1 or weekcode == 2:
            self.weekcode = weekcode # may be 1 or 2
        else:
            raise ValueError(f'{weekcode} - not supported weekcode (must be 1 or 2)')

        self.day_of_week = day_of_week
        
        self.start_time = start_time
        self.end_time = self.start_time + timedelta(hours=1, minutes=30)

        self.start_time = str(self.start_time)[:-3]
        self.end_time = str(self.end_time)[:-3]
    
    def __str__(self) -> str:
        return f'name = {self.name}, type = {self.type}, lecturer = {self.lecturer}, classroom = {self.classroom}, weekcode = {self.weekcode}, day of week = {self.day_of_week}, start time = {self.start_time}, end time = {self.end_time}, color = {self.color}'

    def to_dict(self):
        return {
            'lesson': {
                f'{self.name}' : [
                    {
                        'discipline_type': self.type,
                        'lecturer': self.lecturer,
                        'classroom': self.classroom,
                        'week_code': self.weekcode,
                        'day_of_week': self.day_of_week,
                        'start_time': str(self.start_time),
                        'end_time': str(self.end_time)
                    }
                ]
            }      
        }

def parse_timetable(group_name: str):
    xml_url = "https://voenmeh.ru/wp-content/themes/Avada-Child-Theme-Voenmeh/_voenmeh_grafics/TimetableGroup50.xml"
    response = requests.get(xml_url)

    # Проверка успешности запроса
    if response.status_code == 200:
        response.encoding = 'utf-16'
        content = response.text
        

        # Парсим XML с помощью BeautifulSoup
        soup = BeautifulSoup(content, 'lxml-xml')

        group = soup.find('Group', {'Number': f'{group_name}'})
        timetable = {}
        if group:
            # Проходим по дням недели
            days = group.find_all('Day')
            for day in days:
                day_title = day['Title']
                
                # Проходим по занятиям в этот день
                lessons = day.find_all('Lesson')
                for lesson in lessons:
                    time = lesson.find('Time').text if lesson.find('Time') else "Не указано"
                    result_time = ' '.join(time.split()[:1])
                    time_obj = datetime.strptime(result_time, '%H:%M').time()
                    # Переводим время в timedelta
                    time_delta = timedelta(hours=time_obj.hour, minutes=time_obj.minute)

                    discipline = lesson.find('Discipline').text if lesson.find('Discipline') else "Не указано"
                    match = re.match(r'(\w+)\s+(.+)', discipline)
                    if match:
                        discipline_type = match.group(1) 
                        discipline_name = match.group(2)
                    
                    # Проверяем наличие Lecturers и ShortName
                    lecturer_element = lesson.find('Lecturer')
                    lecturer = lecturer_element.find('ShortName').text if lecturer_element and lecturer_element.find('ShortName') else "не указан"
                    
                    classroom = lesson.find('Classroom').text.strip()
                    if classroom == "":
                        classroom = "не указана"
                    else:
                        classroom = classroom[:-1]
                    week_code = lesson.find('WeekCode').text if lesson.find('WeekCode') else "Не указано"
                    
                    lesson_class = Lesson(discipline_name, discipline_type, lecturer, classroom, int(week_code), day_title, time_delta)
                    
                    if day_title not in timetable:
                        timetable[day_title] = []
                    timetable[day_title].append(lesson_class.to_dict())

        else:
            print(f"Группа {group_name} не найдена.")
        
        with open(Path(f'./app/saved_timetables/{group_name}_timetable.json'), 'w', encoding='utf-8') as json_file:
            json.dump(timetable, json_file, ensure_ascii=False, indent=8)

        print(f"Данные успешно сохранены в {group_name}_timetable.json")
    else:
        print(f"Ошибка при получении XML файла: {response.status_code}")




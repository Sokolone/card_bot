help_message = \
    """Я умею:
/help или /помощь - узнать, что я умею
/about или /о_себе - расскажу о себе
/portfolio или /портфолио - покажу мои работы
/contacts или /контакты - покажу, как со мной связаться
/projects - список костюмов
А если напишешь название проекта - расскажу о нём подробнее"""

information = {
    "Имя": "Степан Сокольчик",
    "Возраст": "14",
    "Хобби": "Собирать конструктор Lego",
    "Интересы": "Математика",
    "Навыки": "Ум"
}

about = '''Учусь в 8 классе на 4 и 5. Увлекаюсь математикой и Python. Есть верный друг Михаил.'''

portfolio = ''

contacts = '+7 888 888-88-88'

text = 'Я пока не умею отвечать на вопросы. Введите команду /help'

projects = {
    'Папа': {
        "name": "Леонид",
        "description": '50 лет, рост 180 см',
        "link": ""
    },
    'Мама': {
        "name": "Варвара",
        "description": '46 лет, 170 см',
        "link": ""
    },
    'Брат': {
        "name": "Арсений",
        "description": "24 года, 190 см",
        "link": ""
    }
}

start_message = '''Спасибо что включили меня!
Чтобы узнать, что я умею, напишите /help'''


def show_info(projects=projects):
    number = 1
    equipment = 'Моя семья!\n'
    for name, equip in projects.items():
        equipment += f"{number}. {name}: {equip['description']}\n"
        number += 1
    return equipment


def describe_project(project_name=None, projects=projects):
    if project_name in projects:
        description = f"<b>{project_name}</b>\n{projects[project_name]['description']}\n"
        description += f"<b>Ссылка на проект</b>: {projects[project_name]['link']}\n"
        return description
    else:
        return "Нет такого проекта. Вызови /projects, чтобы увидеть список проектов."

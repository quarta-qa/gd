from locators import *
from elements import HTMLInput, HTMLButton, HTMLLink, HTMLCheckbox, HTMLDate


class LoginPage(Browser):

    username = HTMLInput(id='UserName')
    password = HTMLInput(id='Password')
    submit = HTMLButton(xpath="//*[@value='Войти']")


class MainPage(Browser):

    main = HTMLLink(partial_link_text='Портал кадровой службы')

    # Ведение должностных регламентов
    regulation_formation = HTMLLink(partial_link_text='Формирование должностных регламентов')
    regulation_coordination = HTMLLink(partial_link_text='Согласование должностных регламентов')
    archive = HTMLLink(partial_link_text='Архив')
    filling_control = HTMLLink(partial_link_text='Настройка заполнения должностных регламентов')

    # Дополнительное профессиональное образование
    actions = HTMLLink(partial_link_text='Мероприятия по профессиональному развитию ')
    information = HTMLLink(partial_link_text='Информация о профессиональном развитии ')
    candidates = HTMLLink(partial_link_text='Кандидаты на обучение ')
    planning = HTMLLink(partial_link_text='Планирование профессионального развития ')
    execution_dpo = HTMLLink(partial_link_text='Исполнение заказа на дополнительное профессиональное образование')

    # Практика и стажировка студентов
    letters = HTMLLink(partial_link_text='Письма в подразделения о стажировке и практике студентов ')
    requests = HTMLLink(partial_link_text='Заявки от структурных подразделений')
    students = HTMLLink(partial_link_text='Студенты')
    training_plan = HTMLLink(partial_link_text='План прохождения стажировки и практики ')
    practical_training = HTMLLink(partial_link_text='Прохождение стажировки и практики ')

    # Отчеты
    reports = HTMLLink(partial_link_text='Отчетные формы')


class StudentsPage(Browser):

    # Кнопки
    filter = HTMLButton(xpath="//*[.='Фильтр']")
    add = HTMLButton(xpath="//*[.='Добавить']")
    delete = HTMLButton(xpath="//*[.='Удалить']")
    delete_ok = HTMLButton(xpath="//*[.='Да']")
    delete_cancel = HTMLButton(xpath="//*[.='Отмена']")

    # Фильтр
    student = HTMLInput(xpath="//*[@ng-model='ngModel.value']")
    date_from = HTMLDate(xpath="//*[@ng-model='ngModel.value1']//input")
    date_to = HTMLDate(xpath="//*[@ng-model='ngModel.value2']//input")
    accept = HTMLButton(xpath="//*[.='Применить']")
    cancel = HTMLButton(xpath="//*[.='Отмена']")
    clear = HTMLButton(xpath="//*[.='Очистить']")

    def select_students(self, student):
        self.set_checkboxes((By.XPATH, "//tr[contains(., '%s')]//div[@role='checkbox']" % student))


class StudentsCardPage(Browser):

    last_name = HTMLInput(name='lastName')
    first_name = HTMLInput(name='firstName')
    middle_name = HTMLInput(name='middleName')
    birthday = HTMLInput(xpath='//*[@data-ng-model="model.birthDate"]//input')

    submit = HTMLButton(xpath="//*[.='Сохранить']")
    cancel = HTMLButton(xpath="//*[.='Отмена']")

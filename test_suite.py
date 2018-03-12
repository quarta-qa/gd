from pages import *
from links import Links


class TestSuite:

    driver = webdriver.Chrome("driver\\chromedriver.exe")

    @classmethod
    def setup_class(cls):
        cls.driver.maximize_window()
        cls.driver.get(Links.main_page)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_login(self):
        """
        Авторизация на портале
        """
        page = LoginPage(self.driver)
        page.username = "StepinaYA"
        page.password = "123123/"
        page.submit.click()

        page = MainPage(self.driver)
        page.students.click()

        page = StudentsPage(self.driver)
        page.add.click()

        page = StudentsCardPage(self.driver)
        page.last_name = "Иванов"
        page.first_name = "Иван"
        page.middle_name = "Иванович"
        page.birthday = "04.04.1970"
        page.submit.click()

        page = StudentsPage(self.driver)
        page.select_students("Иванов Иван Иванович")
        page.delete.click()
        page.delete_ok.click()
        page.filter.click()
        page.student = "Пугачев Сергей Витальевич"
        page.date_from = ""
        page.date_to = ""
        page.accept.click()

        sleep(5)

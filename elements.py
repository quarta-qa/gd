from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


_LOCATOR_MAP = {
    'xpath': By.XPATH,
    'class': By.CLASS_NAME,
    'name': By.NAME,
    'link_text': By.LINK_TEXT,
    'partial_link_text': By.PARTIAL_LINK_TEXT,
    'id': By.ID,
    'css': By.CSS_SELECTOR,
    'tag_name': By.TAG_NAME
}

_EXPECTED_COND_MAP = {
    'presence': expected_conditions.presence_of_element_located,
    'visible': expected_conditions.visibility_of_element_located,
    'invisible': expected_conditions.invisibility_of_element_located,
    'clickable': expected_conditions.element_to_be_clickable
}


class Element(object):

    _locator = None
    _timeout = 10
    _expected_condition = 'visible'
    _ec = _EXPECTED_COND_MAP

    def __init__(self, **kwargs):
        if not kwargs:
            raise ValueError('Please specify a locator')

        len_kwargs = len(kwargs)
        if len_kwargs > 2:
            raise ValueError('Element only takes 3 arguments, but %d given' % len_kwargs)

        for key, value in list(kwargs.items()):
            if key in _LOCATOR_MAP:
                self._locator = (_LOCATOR_MAP[key], value)
            elif key == 'expected_condition':
                self._expected_condition = value
                if value not in self._ec:
                    raise ValueError('Invalid expected condition %s' % value)
            elif key == 'timeout':
                self._timeout = value
                if value < 0:
                    raise ValueError('Invalid timeout value %s' % value)
            else:
                raise ValueError('Invalid input: %s' % key)

        if self._locator is None:
            raise ValueError('Please specify a locator')

    def find(self, driver):
        # waiting for loading screen
        WebDriverWait(driver, self._timeout).until_not(
            self._ec['visible']((_LOCATOR_MAP['class'], 'bg'))
        )
        return WebDriverWait(driver, self._timeout).until(
            self._ec[self._expected_condition](self._locator),
            "Didn't find element by %s: <%s>" % self._locator
        )

    def __set__(self, instance, value):
        if value is not None:
            element = self.__get__(instance, instance.__class__)
            value = str(value)
            if len(value) > 0:
                element.clear()
                element.send_keys(value)
                return True
        return False

    def __get__(self, instance, owner):
        driver = instance.driver
        return self.find(driver)


class HTMLButton(Element):
    _expected_condition = 'clickable'


class HTMLInput(Element):
    pass


class HTMLSelect(Element):
    pass


class HTMLLink(Element):
    _expected_condition = 'clickable'


class HTMLCheckbox(Element):
    _expected_condition = 'clickable'


class HTMLDate(Element):

    def __set__(self, instance, value):
        if value is not None:
            element = self.__get__(instance, instance.__class__)
            value = str(value)
            if len(value) > 0:
                element.clear()
                element.send_keys(value + Keys.TAB)
                return True
        return False

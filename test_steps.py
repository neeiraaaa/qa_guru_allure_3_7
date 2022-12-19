import allure
from allure_commons.types import Severity, AttachmentType
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


#Тест на чистом Selene (без шагов)

@allure.tag('web')
@allure.label('owner', 'neeiraaaa')
@allure.severity(Severity.CRITICAL)
@allure.feature('Проверка названия Issue в репозитории через Web-интерфейс')
@allure.story('Чистый Selene (без шагов)')
@allure.link('https://github.com', name='Тестирование')
def test_github_issue():
    browser.config.window_height = 1920
    browser.config.window_width = 1620
    browser.open('https://github.com/')
    browser.element('.header-search-input').click()
    browser.element('.header-search-input').type('eroshenkoam/allure-example')
    browser.element('.header-search-input').press_enter()
    browser.element(by.link_text('eroshenkoam/allure-example')).click()
    browser.element('#issues-tab').click()
    browser.element(by.partial_text('#76')).should(be.visible)
    browser.quit()


#Лямбда шаги через with allure.step

@allure.tag('web')
@allure.label('owner', 'neeiraaaa')
@allure.severity(Severity.NORMAL)
@allure.feature('Проверка названия Issue в репозитории через Web-интерфейс')
@allure.story('Лямбда шаги через with allure.step')
@allure.link('https://github.com', name='Тестирование')
def test_github_issue():
    with allure.step('Открыть главную страницу'):
        browser.config.window_height = 1920
        browser.config.window_width = 1620
        browser.open('https://github.com/')
    with allure.step('Найти репозиторий'):
        browser.element('.header-search-input').click()
        browser.element('.header-search-input').type('eroshenkoam/allure-example')
        browser.element('.header-search-input').press_enter()
    with allure.step('Открыть репозиторий'):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()
    with allure.step('Открыть таб issues'):
        browser.element('#issues-tab').click()
    with allure.step('Проверить наличие issue с номером 76'):
        browser.element(by.partial_text('#76')).should(be.visible)
        browser.quit()


#Пример теста с лямбда шагами

@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "neeiraaaa")
@allure.feature("Проверка названия Issue в репозитории через Web-интерфейс")
@allure.story("Пример теста с лямбда шагами")
@allure.link("https://github.com", name="Testing")
def test_dynamic_steps():
    with allure.step("Открываем главную страницу"):
        browser.config.window_height = 1920
        browser.config.window_width = 1620
        browser.open("https://github.com")
    with allure.step("Ищем репозиторий"):
        s(".header-search-input").click()
        s(".header-search-input").send_keys("eroshenkoam/allure-example")
        s(".header-search-input").submit()
    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text("eroshenkoam/allure-example")).click()
    with allure.step("Открываем таб Issues"):
        s("#issues-tab").click()
    with allure.step("Проверяем наличие Issue с номером 76"):
        s(by.partial_text("#76")).should(be.visible)
    with allure.step("Делаем финальный скриншот"):
        allure.attach(browser.driver.get_screenshot_as_png(), name="Happypath", attachment_type=AttachmentType.PNG)


#Шаги с декоратором @allure.step

@allure.tag("web")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "neeiraaaa")
@allure.feature("Проверка названия Issue в репозитории через Web-интерфейс")
@allure.story("Пример теста с декоратором")
@allure.link("https://github.com", name="Testing")
def test_decorator_steps():
    browser.config.window_height = 1920
    browser.config.window_width = 1620
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    should_see_issue_with_number("#76")


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Ищем репозиторий {repo}")
def search_for_repository(repo):
    s(".header-search-input").click()
    s(".header-search-input").send_keys(repo)
    s(".header-search-input").submit()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Проверяем наличие Issue с номером {number}")
def should_see_issue_with_number(number):
    s(by.partial_text(number)).click()
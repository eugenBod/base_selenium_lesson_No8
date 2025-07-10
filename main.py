# Импортируем WebDriver для управления браузером
from selenium import webdriver

# Для настройки запуска Chrome (установка драйвера)
from selenium.webdriver.chrome.service import Service as ChromeService

# Для поиска элементов по типам (By.ID и т.д.)
from selenium.webdriver.common.by import By

# Автоматическая загрузка драйвера Chrome
from webdriver_manager.chrome import ChromeDriverManager


# Создаем настройки браузера
options = webdriver.ChromeOptions()

# Предотвращаем закрытие браузера после выполнения скрипта
options.add_experimental_option("detach", True)

# Запуск браузера в фоновом режиме (без графического интерфейса)
#options.add_argument("--headless")

# Запускаем Chrome с автоматически установленным драйвером и заданными опциями
driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

# Базовые данные
base_url = "http://www.saucedemo.com/"
valid_username = "performance_glitch_user"
incorrect_password = "sauce_secret"
expecting_error_message = "Epic sadface: Username and password do not match any user in this service"

# Переход на страницу авторизации  и разворачивание окна на весь экран
driver.get(base_url)
driver.maximize_window()

# Ввод логина
driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(valid_username)
print("Input login")

# Ввод неверного пароля
driver.find_element(By.XPATH, "//input[@id='password']").send_keys(incorrect_password)
print("Input incorrect password")

# Клик по кнопке "Login"
driver.find_element(By.XPATH, "//input[@id='login-button']").click()
print("Click login button")

# Получаем текст сообщения об ошибке с страницы
error_text = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
print(f"Error text: {error_text}")

# Проверяем, что текст ошибки соответствует ожидаемому
assert error_text == expecting_error_message, (
    f"Error text does not match. Expected: {expecting_error_message}, got {error_text}"
)
print("Error text correct")

# Клик по кнопке, которая скрывает предупреждающее сообщение
driver.find_element(By.XPATH, "//button[@class='error-button']").click()
print("Click error button")
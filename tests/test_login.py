from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities import login

# Validación: Login automatizado con espera explícita y verificación de URL, título y encabezado
def test_login_validation(login_in_driver):
    driver = login_in_driver

    # Paso 1: Ejecuta la función login definida en utilities.py
    login(driver)

    # Paso 2: Espera explícita a que la URL contenga '/inventory.html'
    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory.html")
    )

    # Paso 3: Verifica que la URL sea la esperada
    assert "inventory.html" in driver.current_url, "No se redirigió a la página de inventario"

    # Paso 4: Verifica que el título de la página sea 'Swag Labs'
    assert driver.title == "Swag Labs", "El título de la página no es 'Swag Labs'"

    # Paso 5: Verifica que el encabezado 'Products' esté presente en la página
    encabezado = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "title"))
    )
    assert encabezado.text == "Products", "El encabezado de la página no es 'Products'"

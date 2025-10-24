from selenium.webdriver.common.by import By

# Validación 1: Verifica que el título de la página sea el esperado
def test_titulo_pagina(login_in_driver):
    driver = login_in_driver
    # Se espera que el título sea "Swag Labs" al ingresar correctamente
    assert driver.title == "Swag Labs", "El título de la página no es el esperado"

# Validación 2: Comprueba que haya al menos un producto visible en la página
def test_productos_visibles(login_in_driver):
    driver = login_in_driver
    # Busca todos los elementos con clase 'inventory_item' que representan productos
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    # Se espera que haya al menos uno visible
    assert len(productos) > 0, "No hay productos visibles en la página"

# Validación 3: Extrae y valida el nombre y precio del primer producto
def test_datos_primer_producto(login_in_driver):
    driver = login_in_driver
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0, "No se encontró ningún producto para validar"

    # Obtiene el nombre y precio del primer producto
    nombre = productos[0].find_element(By.CLASS_NAME, "inventory_item_name").text
    precio = productos[0].find_element(By.CLASS_NAME, "inventory_item_price").text

    # Imprime los datos para facilitar la revisión manual
    print(f"Primer producto: {nombre} - Precio: {precio}")

    # Valida que el nombre no esté vacío y que el precio tenga formato correcto
    assert nombre != "", "El nombre del primer producto está vacío"
    assert precio.startswith("$"), "El precio del primer producto no tiene el formato esperado"

# Validación 4: Verifica que elementos clave de la interfaz estén presentes
def test_elementos_interfaz(login_in_driver):
    driver = login_in_driver
    # Busca el botón de menú lateral y el filtro de ordenamiento
    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")

    # Valida que ambos estén visibles en la interfaz
    assert menu.is_displayed(), "El botón de menú no está visible"
    assert filtro.is_displayed(), "El filtro de productos no está visible"

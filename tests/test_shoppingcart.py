from selenium.webdriver.common.by import By

# Validación 1: Añadir un producto al carrito haciendo clic en el botón correspondiente
def test_agregar_producto_al_carrito(login_in_driver):
    driver = login_in_driver

    # Se selecciona el primer botón "Add to cart"
    boton_agregar = driver.find_element(By.CLASS_NAME, "btn_inventory")
    boton_agregar.click()

    # Se vuelve a buscar el botón actualizado (ahora debería decir "Remove")
    boton_actualizado = driver.find_element(By.CLASS_NAME, "btn_inventory")
    assert boton_actualizado.text == "Remove", "El producto no fue añadido correctamente al carrito"

# Validación 2: Verificar que el contador del carrito se incremente correctamente
def test_contador_carrito(login_in_driver):
    driver = login_in_driver

    # Se añade un producto al carrito
    driver.find_element(By.CLASS_NAME, "btn_inventory").click()

    # Se busca el ícono del carrito y se verifica que el contador muestre "1"
    contador = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert contador == "1", f"El contador del carrito debería ser 1, pero muestra: {contador}"

# Validación 3: Navegar al carrito de compras
def test_navegar_al_carrito(login_in_driver):
    driver = login_in_driver

    # Se hace clic en el ícono del carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Se verifica que la URL cambie a la vista del carrito
    assert "cart.html" in driver.current_url, "No se redirigió correctamente al carrito de compras"

# Validación 4: Comprobar que el producto añadido aparezca correctamente en el carrito
def test_producto_en_carrito(login_in_driver):
    driver = login_in_driver

    # Se añade un producto y se navega al carrito
    driver.find_element(By.CLASS_NAME, "btn_inventory").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Se verifica que el producto esté listado en el carrito
    producto_en_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(producto_en_carrito) > 0, "No se encontró ningún producto en el carrito"

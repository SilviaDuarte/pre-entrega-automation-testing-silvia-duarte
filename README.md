# Proyecto de Automatización de Pruebas - Saucedemo 🧪

Este proyecto forma parte del curso de Automation Testing y tiene como objetivo automatizar pruebas funcionales sobre la página de demostración [saucedemo.com](https://www.saucedemo.com/), utilizando herramientas modernas como **Python**, **Pytest** y **Selenium WebDriver**.

---

## 🚀 Propósito del proyecto

Validar funcionalidades clave de una aplicación web de e-commerce mediante pruebas automatizadas. Se simulan acciones como login, navegación por inventario, interacción con el carrito de compras y verificación de elementos de interfaz.

---

## 🛠️ Tecnologías utilizadas

- **Python 3.13.7**
- **Selenium WebDriver**
- **Pytest**
- **pytest-html** (para generación de reportes)
- **Visual Studio Code** (como entorno de desarrollo)

---

## 📁 Estructura del proyecto

pre-entrega-automation-testing-silvia-duarte/
├── README.md               # Documentación principal del proyecto
├── run_tests.py            # Script para ejecutar todas las pruebas
├── conftest.py             # Fixture para inicializar y cerrar el navegador (modo incógnito)
├── utilities.py            # Funciones auxiliares reutilizables (ej. login automatizado)
├── report.html             # Reporte HTML generado por Pytest con resultados detallados
├── assets/                 # Carpeta para recursos adicionales
└── tests/                  # Carpeta principal de pruebas
    ├── test_login.py       # Prueba de login con validaciones de URL, título y encabezado
    ├── test_inventory.py   # Validaciones sobre productos, interfaz y estructura de inventario
    └── test_shoppingcart.py# Pruebas de interacción con el carrito de compras

## 🧪 Ejecución de pruebas
Para ejecutar todas las pruebas y generar el reporte HTML se debe correr el archivo run_tests.py.
El archivo report.html se generará automáticamente en la raiz del prooyecto y puede abrirse encualquier navegador
Comando para ejecutar pruebas: python run_tests.py

## 📬 Contacto

Este código fue desarrollado por:  
**Silvia Duarte Jardine**  
📧 silvidujar@gmail.com
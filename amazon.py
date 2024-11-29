from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def obtener_titulo_producto_amazon(url):
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get(url)
        time.sleep(3)
        titulo_elemento = driver.find_element(By.ID, "productTitle")
        titulo = titulo_elemento.text.strip() if titulo_elemento else "No se encontró el título del producto"
        print(titulo)
        return titulo
    except Exception as e:
        return f"Error al obtener el producto: {e}"
    finally:
        driver.quit()

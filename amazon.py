from selenium import webdriver
from database import insertar_log
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def obtener_titulo_producto_amazon(url):
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get(url)
        time.sleep(3)

        manejar_captcha(driver)

        titulo_elemento = driver.find_element(By.ID, "productTitle")
        titulo = titulo_elemento.text.strip() if titulo_elemento else "No se encontró el título del producto"
        print(titulo)

        insertar_log('success', f'Título obtenido exitosamente: "{titulo}" para la URL: {url}')
        return titulo
    except Exception as e:
        insertar_log('error', 'Error al obtener el título del producto', details=str(e))
        return f"Error al obtener el producto: {e}"
    finally:
        driver.quit()



def manejar_captcha(driver):
    """Función para manejar el captcha en Amazon"""
    try:
        # Espera a que el botón "Try different image" sea visible y clickeable
        retry_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Try different image')]"))
        )
        retry_button.click()
        print("Captcha: Se hizo clic en 'Probar una imagen diferente'.")
    except TimeoutException:
        # Si no se encuentra el botón dentro del tiempo esperado, refresca la página
        print("Captcha: No se encontró el botón en el tiempo esperado. Refrescando la página...")
        driver.refresh()
        time.sleep(2)  # Agregar una pausa breve después de refrescar
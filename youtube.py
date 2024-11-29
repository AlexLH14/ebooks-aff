import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from database import cargar_registro, guardar_registro, insertar_comentario

CHROME_PROFILE_PATH = "C:/Users/alex2/AppData/Local/Google/Chrome/User Data/Profile 2"

def search_and_play_youtube_video(search_query, comment_text, producto_id, categoria_id, link_producto ):
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-data-dir={CHROME_PROFILE_PATH}")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    time.sleep(5)

    video_log = cargar_registro()

    try:
        driver.get("https://www.youtube.com")
        time.sleep(3)

        search_box = driver.find_element(By.NAME, "search_query")
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)
        time.sleep(5)

        video_tab = driver.find_element(By.XPATH, "//yt-chip-cloud-chip-renderer[.//yt-formatted-string[text()='Vídeos']]")
        video_tab.click()

        filter_button = driver.find_element(By.ID, 'filter-button')
        filter_button.click()
        time.sleep(5)

        filtro_relevancia = driver.find_element(By.XPATH, "//ytd-search-filter-group-renderer[.//yt-formatted-string[text()='Ordenar por']]//ytd-search-filter-renderer[.//yt-formatted-string[text()='Relevancia']]")
        filtro_relevancia.click()

        body = driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.ESCAPE)
        time.sleep(15)

        videos = driver.find_elements(By.XPATH, "(//a[contains(@href, 'watch') and @id='video-title'])")
        for video in videos:
            video_url = video.get_attribute("href")
            video_id = video_url.split("v=")[-1].split("&")[0]

            if video_id not in video_log:
                video.click()
                time.sleep(5)

                # Concatenar el enlace al comentario para publicarlo en YouTube
                comentario_youtube = f"{comment_text}\n\nEnlace del producto: {link_producto}"

                if leave_comment(driver, comentario_youtube):
                    video_log_id = guardar_registro(video_id)
                    insertar_comentario(comment_text, producto_id, video_log_id, categoria_id) #----------------------------
                    return
                return
        print("No se encontraron videos nuevos para comentar.")

    finally:
        driver.quit()

def leave_comment(driver, comment_text):
    try:
        actions = ActionChains(driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)

        comment_box = driver.find_element(By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")
        comment_box.click()
        time.sleep(2)

        input_box = driver.find_element(By.ID, "contenteditable-root")
        input_box.send_keys(comment_text)
        time.sleep(10)

        submit_button = driver.find_element(By.XPATH, "//ytd-button-renderer[@id='submit-button']")
        submit_button.click()
        time.sleep(3)

        print("Comentario publicado exitosamente.")
        return True
    except Exception as e:
        print(f"Error al intentar comentar: {e}")
        return False

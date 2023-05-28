from selenium import webdriver

def contar_apariciones(url, palabras):
    # Inicializar el controlador de Selenium
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Ejecutar Chrome en modo sin cabeza
    driver = webdriver.Chrome(options=options)  # Asegúrate de tener Chrome WebDriver instalado y en el PATH
    
    try:
        # Cargar la página web
        driver.get(url)
        contenido = driver.page_source.lower()  # Obtener el contenido completo de la página en minúsculas
        
        # Contar las apariciones de cada palabra
        conteo = {}
        for palabra in palabras:
            apariciones = contenido.count(palabra.lower())  # Convertir la palabra a minúsculas para buscar sin distinción de mayúsculas
            conteo[palabra] = apariciones
        
        return conteo
    finally:
        # Cerrar el controlador de Selenium
        driver.quit()

# Ejemplo de uso
#url = "https://programa.masmadrid.org/#Comunidad%20de%20Madrid"
url= "https://podemos.info/wp-content/uploads/2023/05/Podemos_programa_marco_28M_interactivo.pdf"
palabras = ["educación", "sanidad", "alquiler", "condiciones laborales", "corrupción", "españa"]
resultado = contar_apariciones(url, palabras)

# Imprimir el resultado
print(f"La concurriencia para el programa de {url}")

for palabra, apariciones in resultado.items():
    print(f"{palabra}: {apariciones}")

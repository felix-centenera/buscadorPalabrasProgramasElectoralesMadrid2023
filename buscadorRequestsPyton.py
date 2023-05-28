import requests

def contar_apariciones(url, palabras):
    try:
        # Obtener el contenido de la página web
        respuesta = requests.get(url)
        contenido = respuesta.text.lower()  # Convertir a minúsculas para realizar una búsqueda sin distinción de mayúsculas
        
        # Contar las apariciones de cada palabra
        conteo = {}
        for palabra in palabras:
            apariciones = contenido.count(palabra.lower())  # Convertir la palabra a minúsculas para buscar sin distinción de mayúsculas
            conteo[palabra] = apariciones
        
        return conteo
    except requests.exceptions.RequestException:
        print("Error al acceder a la URL.")

# Ejemplo de uso
url = "https://programa.masmadrid.org/#Comunidad%20de%20Madrid"
palabras = ["colegios", "sanidad", "lgtbi"]
resultado = contar_apariciones(url, palabras)

# Imprimir el resultado
for palabra, apariciones in resultado.items():
    print(f"{palabra}: {apariciones}")

import requests
import PyPDF2

def contar_apariciones_pdf_en_url(url, palabras):
    conteo = {}
    
    # Descargar el archivo PDF desde la URL
    response = requests.get(url)
    with open('archivo.pdf', 'wb') as archivo_pdf:
        archivo_pdf.write(response.content)
    
    # Leer el archivo PDF y contar las apariciones de palabras
    with open('archivo.pdf', 'rb') as archivo:
        lector_pdf = PyPDF2.PdfReader(archivo)
        
        for pagina in lector_pdf.pages:
            contenido = pagina.extract_text().lower()
            
            for palabra in palabras:
                apariciones = contenido.count(palabra.lower())
                if palabra in conteo:
                    conteo[palabra] += apariciones
                else:
                    conteo[palabra] = apariciones
    
    return conteo


url_pdf_list = ["https://www.newtral.es/wp-content/uploads/2019/04/Programa-electoral-VOX.pdf?x24211","https://ppasamblea.es/Docs/PROGRAMA_NUEVAS_MEDIDAS.pdf","https://www.psoemadrid.es/wp-content/uploads/ProgLecturaFacilx20_PSOEM.pdf","https://podemos.info/wp-content/uploads/2023/05/Podemos_programa_marco_28M_interactivo.pdf","https://programa.masmadrid.org/pdf/Comunidad%20de%20Madrid/Programa%20Más%20Madrid%20-%20CM%202023.pdf"]


for url_pdf in url_pdf_list:
    palabras = ["educación", "sanidad", "alquiler","vivienda","público","laboral","condiciones laborales", "corrupción", "españa", "españoles","inmigración","concertada","concertado","lgtbi","adoctrinamiento","igualdad","social","energía","naturaleza","animal","animales","ciencia","industria","cultura","juventud","mayores","economía","iglesia","religión","transporte","machismo"]
    resultado = contar_apariciones_pdf_en_url(url_pdf, palabras)
    # Imprimir el resultado
    print(f"---------------------------------------------------------------------------------------------------")
    print(f"Número de menciones a terminos en el programa de {url_pdf} :\n")
    for palabra, apariciones in resultado.items():
        print(f"{palabra}: {apariciones}")
    print(f"##############################################################################################\n\n\n")
import requests

# Obtener una clave de API de Microsoft
api_key = "your_api_key_here"

# URL de la API de Microsoft Store para buscar juegos de PC
url = "https://displaycatalog.mp.microsoft.com/v7.0/products?bigIds=Games_PC&market=US&languages=en-US&MS-CV=1.0&fieldsTemplate=StoreSDKFields"

# Enviar solicitud HTTP a la API
response = requests.get(url, headers={"X-WindowsPhone-Store-Client-Name": "Windows Store", "X-WindowsPhone-Store-Client-Version": "11810"})

# Analizar la respuesta JSON
data = response.json()

# Imprimir los nombres de los juegos de PC encontrados
for product in data["Products"]:
    print(product["LocalizedProperties"][0]["ProductTitle"])

import requests

# Función que consulta trivia de un número usando la Numbers API
def trivia_fetch(num: int) -> dict:
    """
    Toma un número como input y devuelve un diccionario
    con trivia sobre ese número desde la Numbers API.
    """
    url = f"http://numbersapi.com/{num}?json"

    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        data = resp.json()  # La API devuelve JSON directamente
    except requests.exceptions.RequestException as e:
        return {"number": num, "found": False, "error": str(e)}

    return data
#Función principal del programa
def main():
 print(" Bienvenidos al Quiz de Números ")
 num = int(input("Elige un número para descubrir trivia: "))

 trivia = trivia_fetch(num)

 if trivia.get("found"):
        print(f"\nDato curioso sobre {num}:")
        print(trivia["text"])
 else:
        print(f"No encontré trivia para {num}. :c")
if __name__=="__main__":
  main()
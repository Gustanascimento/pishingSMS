import requests
import threading

#Código para quando um sistema de verificação de validade de cartão de crédito é utilizado

url = '' #Verificar no console do Chrome qual a URL de destino

dados = {
    'cc':'',
    'cvv':'',
    'exp':'',
}

def fazer_request():
    while True:
        resposta = requests.post(url, data=dados).text
        print(resposta)

threads = []

for x in range(50):
    t = threading.Thread(target=fazer_request)
    t.daemon=True
    threads.append(t)

for x in range(50):
    threads[x].start()

for x in range(50):
    threads[x].join()
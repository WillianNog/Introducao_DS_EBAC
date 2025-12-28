import requests
import json


def enviar_arquivos():
    #Caminho do arquivo para upload
    caminho = r"B:\Estudos\Estudos EBAC\codigo\produtos_informatica.xlsx"

    #Enviar arquivo
    requisicao = requests.post('https://upload.gofile.io/uploadFile', files={'file': open(caminho,'rb')})
    saida_requisicao = requisicao.json()

    print(json.dumps(saida_requisicao, indent= 4, ensure_ascii=False))
    url = saida_requisicao['data']['downloadPage']
    print("Arquivo enviado. Link para acesso: ", url)


def receber_arquivos(file_url):
    #Receber o arquivo
    requisicao = requests.get(file_url)

    # Salvar o arquivo
    if requisicao.ok:
        with open('arquivo_baixado.xlsx', 'wb') as file:
            file.write(requisicao.content)
        print("Arquivo baixado com sucesso!")

    else:
        print("Erro ao baixar o arquivo", requisicao.json())



def enviar_aquivo_chave():
    caminho = r"B:\Estudos\Estudos EBAC\codigo\produtos_informatica.xlsx"
    chave_acesso = "iQItQFBydXWRYIKYeDJMAUniutSE6D7P"

    # Enviar o arquivo
    requisicao = requests.post(
        'https://upload.gofile.io/uploadFile',
        files={'file': open(caminho,'rb')},
        headers={'Authorization': chave_acesso}
    )
    saida_requisicao = requisicao.json()
    print(json.dumps(saida_requisicao, indent= 4, ensure_ascii=False))
    url = saida_requisicao['data']['downloadPage']
    print("Arquivo enviado com chave. Link para acesso: ", url)




# enviar_arquivos()
# enviar_aquivo_chave()
receber_arquivos("https://gofile.io/d/TiTbBh")

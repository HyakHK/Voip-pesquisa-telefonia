import requests
import os
from dotenv import load_dotenv

#carregar variaveis
load_dotenv()


#informações para acesso
#colocar as credenciais em um arquivo separado por questões de segurança

url= "https://suap.ifrn.edu.br/api/token/pair"
url_boletim= "https://suap.ifrn.edu.br/api/ensino/meu-boletim/2025/1"

credenciais = {
    "username" : os.getenv("username"),
    "password" : os.getenv("password")
}

#inicio da conexão
try:
    conn= requests.post(url, json=credenciais, timeout=10)

    resposta= conn.json()

    #separação das chaves adiquiridas
    key_refresh= resposta.get("refresh")
    key_access= resposta.get("access")

    #Pegar boletim
    try:

        header= {
            'Authorization' : f'Bearer {key_access}'
        }

        conn_boletim= requests.get(url_boletim,headers= header, timeout=10)
        #Para uso posterior, definição para status da requisição da url
        conn_boletim.raise_for_status()

        resposta_boletim= conn_boletim.json()
        #conexão realizada
        #tratamento de cada disciplina para exemplificação(vai ser especificado mais tarde)

        disciplinas= resposta_boletim.get("results", [])

        for disciplina in disciplinas:
            #nome da disciplina
            nome_dis= disciplina.get("disciplina", "Nome indisponivel")

            #Neste exemplo esta pegando da etapa um, porem n para futuro input field
            notaN= disciplina.get("nota_etapa_1", {})
            nota= notaN.get("nota")
            falta= notaN.get("faltas")

            #Os prints
            print(f"Nota: {nome_dis}")
            print(f"Nota: {nota}")
            print(f"Nota: {falta}")
            print("-" *10)



    except requests.exceptions.RequestException as err:
        print(err)


    
except requests.exceptions.RequestException as err:
    #adicionar erros especificos da coneção abaixo
    print(err)


import requests

class SuapClient:
    def __init__(self, enrolment, responsible_code):
        self.url = 'https://suap.ifrn.edu.br'
        self.credentials = {
            'matricula': enrolment,
            'chave': responsible_code   
        }

        self.responsible_authentication_endpoint = '/api/ensino/autenticacao/acesso-responsaveis/'
        self.get_boletim_endpoint = '/api/ensino/meu-boletim/2025/1/?page=1'
       
    def get_student_token(self):
        try:
            r = requests.post(
                url= self.url + self.responsible_authentication_endpoint,
                headers= {'accept': 'application/json'},
                params= self.credentials
        
            ).json()
        
            return r.get('token')

        except Exception as e:
            raise Exception("falha ao obter token:", e)
    
    def get_boletim(self):
        if not self.__check_con():
            raise Exception("Erro: sem conexão com suap.")
        
        token = self.get_student_token()
        
        r = requests.get(
            url= self.url + self.get_boletim_endpoint,
            headers= {'Authorization': f'Bearer {token}'}
        )           

        return r.json()
    
    def __check_con(self):
        try:
            r = requests.get(self.url, timeout=10, stream=True)
            r.raise_for_status()
            return True
        
        except:
            return False


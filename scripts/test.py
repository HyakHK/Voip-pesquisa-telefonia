import requests
import getpass

# URL's OFICIAIS da API v2 do SUAP
URL_AUTH = "https://suap.ifrn.edu.br/api/v2/autenticacao/token/"

def autenticar_suap():
    """Autentica no SUAP e retorna o token"""
    print("Autenticação no SUAP IFRN")
    print("=" * 50)
    
    username = input("Digite sua matrícula: ").strip()
    password = getpass.getpass("Digite sua senha: ")
    
    credenciais = {
        "username": username,
        "password": password
    }
    
    try:
        print("\n🔄 Autenticando...")
        response = requests.post(URL_AUTH, json=credenciais)
        
        if response.status_code == 200:
            data = response.json()
            token = data.get('access')
            print("✅ AUTENTICAÇÃO BEM-SUCEDIDA!")
            return token
        else:
            print(f"❌ Falha na autenticação: {response.status_code}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro de conexão: {e}")
        return None

def obter_boletim_detalhado(token, ano, periodo):
    """Obtém boletim detalhado"""
    print(f"\n BUSCANDO BOLETIM {ano}/{periodo}...")
    
    url_boletim = f"https://suap.ifrn.edu.br/api/v2/minhas-informacoes/boletim/{ano}/{periodo}/"
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(url_boletim, headers=headers)
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            boletim = response.json()
            print("✅ BOLETIM OBTIDO COM SUCESSO!")
            return boletim
        else:
            print(f"❌ Erro ao obter boletim: {response.status_code}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro de conexão: {e}")
        return None

def formatar_valor(valor):
    """Formata valores None para exibição amigável"""
    if valor is None or valor == 'None':
        return "N/A"
    return valor

def mostrar_informacoes_organizadas(boletim, ano, periodo):
    """Mostra apenas as informações solicitadas de forma organizada"""
    if not boletim:
        print("❌ Nenhum dado de boletim disponível.")
        return
    
    print(f"\n BOLETIM {ano}/{periodo} - INFORMAÇÕES SOLICITADAS")
    print("=" * 70)
    
    if isinstance(boletim, list):
        print(f"Total de disciplinas: {len(boletim)}\n")
        
        for i, disciplina in enumerate(boletim, 1):
            nome = formatar_valor(disciplina.get('disciplina'))
            codigo = formatar_valor(disciplina.get('codigo_diario'))
            situacao = formatar_valor(disciplina.get('situacao'))
            media_final = formatar_valor(disciplina.get('media_final_disciplina'))
            percentual_freq = formatar_valor(disciplina.get('percentual_carga_horaria_frequentada'))
            carga_horaria = formatar_valor(disciplina.get('carga_horaria'))
            carga_horaria_cumprida = formatar_valor(disciplina.get('carga_horaria_cumprida'))
            faltas = formatar_valor(disciplina.get('numero_faltas'))
            
            print(f"{i}. {nome}")
            print(f"   Código: {codigo}")
            print(f"   Situação: {situacao}")
            print(f"   Média Final: {media_final}")
            print(f"   Frequência: {percentual_freq}%")
            print(f"   Carga Horária: {carga_horaria_cumprida}/{carga_horaria}h")
            print(f"   Faltas: {faltas}")
            print()

def mostrar_resumo_estatisticas(boletim):
    """Mostra um resumo estatístico do período"""
    if not boletim or not isinstance(boletim, list):
        return

# Execução principal
if __name__ == "__main__":
    print("🎓 SISTEMA DE CONSULTA ACADÊMICA - SUAP IFRN")
    print("=" * 60)
    
    # Autenticar
    token = autenticar_suap()
    
    if not token:
        print("❌ Encerrando...")
        exit()
    
    # Solicitar período específico
    print("\n Digite o período desejado:")
    ano = input("Ano (ex: 2024): ").strip()
    periodo = input("Período (1 ou 2): ").strip()
    
    # Obter boletim
    boletim = obter_boletim_detalhado(token, ano, periodo)
    
    if boletim:
        # Mostra informações organizadas
        mostrar_informacoes_organizadas(boletim, ano, periodo)
          
    print("\n Consulta concluída!")

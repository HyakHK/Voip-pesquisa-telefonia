# Sistema de Atendimento Telefônico Automático – Issabel 4 + SUAP

Este projeto consiste em um sistema de atendimento telefônico automatizado desenvolvido na plataforma Issabel 4, integrado à API do SUAP (IFRN).  

O sistema permite que pais e responsáveis obtenham informações sobre notas e faltas dos alunos por meio de uma ligação telefônica. As chamadas são atendidas automaticamente pelo Issabel, que consulta os dados no SUAP e reproduz as informações em áudio, tornando o acesso rápido e simples, sem necessidade de internet ou aplicativos adicionais.

# Testbed

- Python 2.7.5
- PHP 5.4.16
- [issabel4 ver. 20200102](https://sourceforge.net/projects/issabelpbx/files/Issabel%204/issabel4-USB-DVD-x86_64-20200102.iso/download)
  - Versão não estavel [issabel5 ver. 20240430.iso](https://sourceforge.net/projects/issabelpbx/files/Issabel%205/issabel5-USB-DVD-x86_64-20240430.iso/download) 
- VirtualBox-7.2.4-170995-Win.exe
### Andamento do projeto
- [x] Apresentação e arpovação da proposta
- [x] estudo sobre issabel e api do suap, e documentação do processo
- [x] Testes com a versão Issabel 5 (Atualmente instavel para uso, problemas tendo enfase na comunicação com o asterisk)
- [x] Downgrade para a versão estavel Issabel 4, com o inicio dos testes de ramais com AGI
- [x] Scrip python basico, utilizando da API do Suap para requisição de informações
- [ ] Realizar checagem de erro melhorada e definição de funções para o tratamento das informações
- [ ] Atualizar Testbed
- [ ] Documentar e revisar ao supervisor para os proximos passos


# Requisitos para o Script

OBS: É recomendado o uso de um /venv para isolar dependencias

**Passos na máquina alvo(linux):**

1.  Crie o ambiente virtual:
    ```bash
    python3 -m venv venv_asterisk
    ```
2.  Ative o ambiente (necessário apenas para a instalação):
    ```bash
    source venv_asterisk/bin/activate
    ```
3.  Instale as dependências usando o arquivo `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Crie o arquivo .venv:** Copie o arquivo exemplo para as credenciais
    ```bash
    cp .env.example .env
    ```



### 1. Dependências Python

As seguintes bibliotecas são necessárias. Caso queira instalar manualmente
- certifi==2025.10.5
- charset-normalizer==3.4.4
- idna==3.11
- python-dotenv==1.2.1
- requests==2.32.5
- urllib3==2.5.0

# Sistema de Atendimento Telefônico Automático – Issabel 4 + SUAP

Este projeto consiste em um sistema de atendimento telefônico automatizado desenvolvido na plataforma Issabel 4, integrado à API do SUAP (IFRN).  

O sistema permite que pais e responsáveis obtenham informações sobre notas e faltas dos alunos por meio de uma ligação telefônica. As chamadas são atendidas automaticamente pelo Issabel, que consulta os dados no SUAP e reproduz as informações em áudio, tornando o acesso rápido e simples, sem necessidade de internet ou aplicativos adicionais.

# Testbed

- Python 2.7.5
- PHP 5.4.16
- [issabel4 ver. 20200102](https://sourceforge.net/projects/issabelpbx/files/Issabel%204/issabel4-USB-DVD-x86_64-20200102.iso/download)
  - Versão não estavel [issabel5 ver. 20240430.iso](https://sourceforge.net/projects/issabelpbx/files/Issabel%205/issabel5-USB-DVD-x86_64-20240430.iso/download) 
- VirtualBox-7.2.4-170995-Win.exe
- Filezilla(ou qualquer FTP)
### Andamento do projeto
- [x] Apresentação e arpovação da proposta
- [x] estudo sobre issabel e api do suap, e documentação do processo
- [x] Testes com a versão Issabel 5 (Atualmente instavel para uso, problemas tendo enfase na comunicação com o asterisk)
- [x] Downgrade para a versão estavel Issabel 4, com o inicio dos testes de ramais com AGI
- [x] Scrip python basico, utilizando da API do Suap para requisição de informações
- [x] Realizar checagem de erro melhorada e definição de funções para o tratamento das informações
- [ ] Atualizar Testbed
- [x] Testar APIs de texto para voz
- [ ] testar possivel uso de voz para acesso
- [ ] Documentar e revisar ao supervisor para os proximos passos

# Requisitos para atualizar o sistema e instalar pacotes
1. Corrigir repositórios principais do CentOS 7 (Vault)

Como o CentOS 7 foi descontinuado, os repositórios originais não funcionam mais.
A solução é utilizar repositórios Vault.

Projeto utilizado:
https://github.com/cloudspinx/centos7-vault-repositories

Passos
```bash
cd /root
git clone https://github.com/cloudspinx/centos7-vault-repositories.git
cd centos7-vault-repositories
./install.sh
```
Isso irá atualizar os arquivos .repo em /etc/yum.repos.d/ e restaurar o funcionamento básico do yum


2. Restaurar repositórios oficiais do Issabel 4

Alguns sistemas Issabel dependem do repositório oficial para instalar módulos adicionais.

Criar ou editar o arquivo:
/etc/yum.repos.d/Issabel.repo

Substituir todo o conteúdo por:
```
[issabel-base]
name=Base RPM Repository for Issabel 
mirrorlist=http://mirror.issabel.org/?release=4&arch=$basearch&repo=base
#baseurl=http://repo.issabel.org/issabel/4/base/$basearch/
gpgcheck=1
enabled=1
gpgkey=http://repo.issabel.org/issabel/RPM-GPG-KEY-Issabel

[issabel-updates]
name=Updates RPM Repository for Issabel 
mirrorlist=http://mirror.issabel.org/?release=4&arch=$basearch&repo=updates
#baseurl=http://repo.issabel.org/issabel/4/updates/$basearch/
gpgcheck=1
enabled=1
gpgkey=http://repo.issabel.org/issabel/RPM-GPG-KEY-Issabel

[issabel-beta]
name=Beta RPM Repository for Issabel 
mirrorlist=http://mirror.issabel.org/?release=4&arch=$basearch&repo=beta
#baseurl=http://repo.issabel.org/issabel/4/beta/$basearch/
gpgcheck=1
enabled=0
gpgkey=http://repo.issabel.org/issabel/RPM-GPG-KEY-Issabel

[issabel-extras]
name=Extras RPM Repository for Issabel 
mirrorlist=http://mirror.issabel.org/?release=4&arch=$basearch&repo=extras
#baseurl=http://repo.issabel.org/issabel/4/extras/$basearch/
gpgcheck=1
enabled=1
gpgkey=http://repo.issabel.org/issabel/RPM-GPG-KEY-Issabel
```
3. Limpar cache e reconstruir os metadados

Após ajustar os arquivos:
```bash
yum clean all
yum makecache
```
Conferir os repos disponíveis:
```bash
yum repolist
```

# Requisitos para o Script

1.  Trocar os repositórios
    ```bash
    sudo sed -i 's|mirrorlist=|#mirrorlist=|g' /etc/yum.repos.d/CentOS-Base.repo
    sudo sed -i 's|#baseurl=http://mirror.centos.org/centos/|baseurl=http://vault.centos.org/centos/|g' /etc/yum.repos.d/CentOS-Base.repo
    sudo yum clean all
    sudo yum makecache
    ```

OBS: É recomendado o uso de um /venv para isolar dependencias

**Passos na máquina alvo(linux):**

1.  Crie o ambiente virtual:
    ```bash
    python -m venv venv_asterisk
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

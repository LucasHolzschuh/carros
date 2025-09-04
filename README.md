# Sistema de Gerenciamento de Veículos com IA

![Django](https://img.shields.io/badge/Django-4.2-092E20?style=for-the-badge&logo=django&logoColor=white) ![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white) ![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white) ![AWS](https://img.shields.io/badge/AWS-EC2-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)

### Um sistema web completo para cadastro e gerenciamento de veículos, com descrições de venda geradas dinamicamente por Inteligência Artificial.

**[➡️ Acesse a demonstração ao vivo aqui!](http://3.220.137.74)**

*(Nota: A aplicação está hospedada em uma instância EC2 da AWS e pode ser desativada periodicamente para otimização de custos.)*

---

## 🚀 Sobre o Projeto

Este projeto foi concebido como uma demonstração prática do ciclo de vida completo de uma aplicação web, desde o desenvolvimento back-end e front-end até a implantação em um ambiente de produção na nuvem.

O sistema simula um inventário de concessionária, onde usuários podem cadastrar veículos. A funcionalidade principal e inovadora é a integração com a **API do Google Gemini**, que gera automaticamente descrições de marketing únicas e atraentes para cada carro, demonstrando uma aplicação real e moderna de IA em um sistema web.

## ✨ Funcionalidades

- **CRUD Completo de Veículos:** Crie, visualize, atualize e delete registros de carros.
- **Geração de Conteúdo por IA:** Utiliza a API do Google Gemini para criar descrições de venda otimizadas.
- **Sistema de Autenticação de Usuários:** Funcionalidades completas de registro e login.
- **Upload de Imagens:** Suporte para upload de fotos para cada veículo.
- **Ambiente de Produção Profissional:** A aplicação foi implantada em um servidor Linux (Ubuntu na AWS EC2), utilizando **Nginx** como proxy reverso e **uWSGI** como servidor de aplicação.

## 🛠️ Stack Tecnológica

- **Back-end:** Python, Django
- **Front-end:** HTML, CSS (Pode adicionar o framework que usou, ex: Bootstrap)
- **Banco de Dados:** PostgreSQL
- **Inteligência Artificial:** Google Gemini API
- **Servidor de Aplicação:** uWSGI
- **Servidor Web / Proxy Reverso:** Nginx
- **Cloud / Hospedagem:** AWS EC2

## ⚙️ Configuração Local

Para executar este projeto em seu ambiente local, siga os passos abaixo:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/LucasHolzschuh/carros.git](https://github.com/LucasHolzschuh/carros.git)
    cd carros
    ```
2.  **Crie e ative um ambiente virtual:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```
3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configure as variáveis de ambiente:**
    - Crie um arquivo `.env` na raiz do projeto.
    - Adicione as seguintes chaves com seus respectivos valores:
      ```
      SECRET_KEY='sua_secret_key'
      DEBUG=True
      GOOGLE_API_KEY='sua_chave_da_api_gemini'
      DB_NAME='nome_do_banco'
      DB_USER='usuario_do_banco'
      DB_PASSWORD='senha_do_banco'
      ```
5.  **Execute as migrações do banco de dados:**
    ```bash
    python3 manage.py migrate
    ```
6.  **Inicie o servidor de desenvolvimento:**
    ```bash
    python3 manage.py runserver
    ```

## 🔗 Contato

**[Lucas Holzschuh dos Santos]**

- LinkedIn: **[Meu Perfil no LinkedIn](https://linkedin.com/in/lucas-santos-2747bb2a2)**
- Email: **lucassantos12386614@gmail.com**
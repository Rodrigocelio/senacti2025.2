# 🪒 BarberBack - Sistema de Gestão de Barbearia

<div align="center">
   <img src="https://senac.ct.ws/default_logo.png" alt="BarberBack" width="180" style="display: block; margin: 0 auto; max-width: 180px; height: auto;">
</div>
Sistema completo de cadastro de clientes e agendamento de serviços para barbearias, com integração automática via webhook para envio de emails de confirmação.

---

## 📋 Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Integração com Webhook](#integração-com-webhook)
- [Templates de Email](#templates-de-email)
- [Serviços Disponíveis](#serviços-disponíveis)
- [Contribuindo](#contribuindo)
- [Licença](#licença)
- [Contato](#contato)

---

## 🎯 Sobre o Projeto

O **BarberBack** é um sistema de gestão desenvolvido para barbearias modernas que buscam automatizar o processo de cadastro de clientes e agendamento de serviços. O sistema envia automaticamente emails profissionais de boas-vindas e confirmação de agendamento através de integração com webhook.

### Identidade Visual

O projeto segue uma identidade visual **premium e sofisticada**:
- **Paleta de cores**: Ouro (#C39900) e Bordô (#8B0000) sobre fundo escuro
- **Tipografia**: Inter (Google Fonts)
- **Estilo**: Alto contraste, dramático e moderno

---

## ⚡ Funcionalidades

### 📝 Gestão de Clientes
- ✅ Cadastro completo de clientes (nome, telefone, email)
- ✅ Listagem de todos os clientes cadastrados
- ✅ Email automático de boas-vindas ao cadastro

### 📅 Sistema de Agendamentos
- ✅ Agendamento de serviços com data e hora
- ✅ Seleção de profissional (Joao, Abraao, Rodrigo, Paulo)
- ✅ 4 tipos de serviços com preços e descrições
- ✅ Validação de data e horário
- ✅ Email automático de confirmação com todos os detalhes

### 📧 Automação de Emails
- ✅ Email de boas-vindas ao cadastro
- ✅ Email de confirmação de agendamento com:
  - Informações do cliente e serviço
  - Data, hora e profissional
  - Localização com link para Google Maps
  - Botão de adicionar ao calendário
  - Link direto para WhatsApp
  - Informações importantes e políticas

### 🔗 Integração
- ✅ Envio automático de dados via webhook
- ✅ Processamento assíncrono de emails

---

## 🛠️ Tecnologias Utilizadas

### Backend
- **Python 3.x** - Linguagem principal do sistema.
- **`urllib`** - Utilizado para realizar requisições HTTP POST para o webhook, enviando dados para automação de emails.
- **`json`** - Responsável pela serialização de dados Python para o formato JSON, usado no envio de informações via webhook.
- **`datetime`** - Empregado para manipulação de datas e horas, incluindo a validação de agendamentos e formatação para o webhook.
- **`pandas`** - Biblioteca essencial para a manipulação e persistência de dados em arquivos Excel, atuando como o "banco de dados" do sistema.
- **`Flask`** - Microframework web utilizado para criar o servidor local que renderiza templates HTML e exibe relatórios e gráficos.
- **`rich`** - Usado para enriquecer a experiência do usuário no terminal, proporcionando uma interface de linha de comando mais atraente e informativa.
- **`matplotlib` e `seaborn`** - Bibliotecas de visualização de dados empregadas para gerar gráficos e relatórios visuais no sistema.
- **`cryptography`** - Utilizada para implementar funcionalidades de segurança, como criptografia de dados sensíveis.
- **`pyfiglet`** - Gera arte ASCII para estilizar elementos visuais no console.
- **`webbrowser`** - Permite abrir links diretamente no navegador padrão do usuário, facilitando o acesso a URLs importantes.
- **`threading`** - Utilizado para executar tarefas assíncronas, como o envio de emails via webhook, sem bloquear a interface do usuário.
- **`io`** - Fornece ferramentas para manipulação de fluxos de dados em memória, útil para operações de leitura e escrita de arquivos temporários.
- **`os`** - Usado para interações com o sistema operacional, como manipulação de arquivos e diretórios.
- **`base64`** - Implementa codificação e decodificação de dados em base64, útil para transmissão segura de informações.
- **`re`** - Biblioteca de expressões regulares para validação e manipulação de strings, como validação de emails e telefones.
- **`getpass`** - Utilizada para entrada segura de senhas no console, ocultando a digitação do usuário.
- **`time`** - Fornece funcionalidades relacionadas ao tempo, como pausas e delays em operações.
- **`seaborn`** - Biblioteca de visualização de dados baseada em Matplotlib, usada para criar gráficos estatísticos atraentes.
- **`fernet`** - Biblioteca para criptografia simétrica, garantindo a segurança dos dados sensíveis.


### Frontend (Templates)
- **HTML5** - Usado para a estruturação básica dos templates de email e de relatórios HTML gerados pelo sistema.
- **CSS3 (Internal Stylesheet)** - Estilização dos templates HTML, com estilos definidos em blocos `<style>` dentro dos arquivos.

### Automação
- **Webhook** - Mecanismo de integração para o envio automático e assíncrono de emails de boas-vindas e confirmação de agendamento.

---

## 📦 Pré-requisitos

- **Python 3.7 ou superior**
- **Conexão com internet** (para envio via webhook)

### Dependências Externas

As seguintes bibliotecas Python devem ser instaladas:

```
pandas>=1.3.0
Flask>=2.0.0
rich>=10.0.0
matplotlib>=3.4.0
seaborn>=0.11.0
cryptography>=3.4.0
pyfiglet>=0.8.0
```

---

## 🚀 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/barberback.git
cd cadastro_salao
```

### 2. Verifique a versão do Python

```bash
python --version
# ou
python3 --version
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
# ou
pip3 install -r requirements.txt
```

Alternativamente, instale manualmente:

```bash
pip install pandas Flask rich matplotlib seaborn cryptography pyfiglet
```

### 4. Configure o Webhook

Edite o arquivo `utils/supplementation.py` e substitua a URL do webhook:

```python
WEBHOOK_URL = "SUA_URL_DO_WEBHOOK_AQUI"
```

### 5. Execute o sistema

```bash
python main.py
# ou
python3 main.py
```

---

## 💻 Como Usar

### Menu Principal

Ao executar o sistema, você verá o seguinte menu:

```
=== Sistema de Cadastro de Clientes - Barbearia ===
1. Cadastrar cliente
2. Listar clientes
3. Fazer agendamento
4. Listar agendamentos
0. Sair
```

### 1️⃣ Cadastrar Cliente

```
Digite o nome do cliente: João Silva
Digite o telefone do cliente: (85) 98765-4321
Digite o email do cliente: joao@email.com

✅ Cliente João Silva cadastrado com sucesso!
✅ Dados enviados com sucesso ao webhook!
```

**Ação automática**: Email de boas-vindas é enviado.

### 2️⃣ Listar Clientes

Exibe todos os clientes cadastrados:

```
Lista de clientes cadastrados:
1. Nome: João Silva, Telefone: (85) 98765-4321, Email: joao@email.com
```

### 3️⃣ Fazer Agendamento

**Passo a passo:**

1. Selecione o cliente da lista
2. Escolha o profissional (1-3)
3. Escolha o serviço (1-4)
4. Informe a data (DD/MM/YYYY)
5. Informe o horário (HH:MM, formato 24h)

```
Escolha o número do cliente: 1

Profissionais disponíveis:
1. Joao
2. Abraao
3. Rodrigo
4. Paulo
Escolha um profissional pelo número: 1

Serviços disponíveis:
1. Corte de cabelo - R$30.00
   ↳ Corte moderno com acabamento na navalha.
2. Barba - R$25.00
   ↳ Barba desenhada e hidratação com toalha quente.
3. Printura - R$15.00
   ↳ Printura de cabelo com tinta temporária.
4. Pacote Completo - R$60.00
   ↳ Cabelo + Barba + Printura com desconto especial.

Escolha um serviço para agendar: 1
Digite a data do agendamento (DD/MM/YYYY): 25/10/2025
Digite o horário do agendamento (HH:MM, 24h): 14:30

✅ Agendamento confirmado para João Silva: Corte de cabelo - R$30.00
🧔 Profissional: Joao
📅 Data: 25/10/2025 às 14:30
📝 Descrição: Corte moderno com acabamento na navalha.
✅ Dados enviados com sucesso ao webhook!
```

**Ação automática**: Email de confirmação é enviado.

### 4️⃣ Listar Agendamentos

```
📅 Agendamentos atuais:
1. Cliente: João Silva | Serviço: Corte de cabelo | Profissional: Joao | Valor: R$30.00 | Data: 25/10/2025 14:30
```

---

## 📁 Estrutura do Projeto

```
cadastro_salao/
├── main.py                         # Ponto de entrada da aplicação
├── README.md                       # Este arquivo
├── core/
│   ├── app.py                      # Lógica principal da aplicação
│   ├── data_handler.py             # Manipulação dos dados (Excel)
│   ├── graphics.py                 # Funções de interface gráfica/console
│   ├── web_integration.py          # Integração com webhook
│   └── templates/
│       └── index.html              # Template base para emails
├── data/
│   ├── agendamentos.xlsx           # Banco de dados de agendamentos
│   ├── clientes_db.xlsx            # Banco de dados de clientes
│   ├── profissionais.xlsx          # Banco de dados de profissionais
│   └── servicos.xlsx               # Banco de dados de serviços
├── executable/
│   ├── Linux/
│   │   └── BarberBack              # Executável para Linux
│   └── Windows/
│       └── BarberBack.exe          # Executável para Windows
└── utils/
    ├── console_tools.py            # Ferramentas de console
    ├── security.py                 # Funções de segurança
    └── supplementation.py          # Funções suplementares
```

---


### Estrutura de Dados Enviados

#### Cadastro de Cliente

```json
{
  "nome": "João Silva",
  "telefone": "(85) 98765-4321",
  "email": "joao@email.com",
  "tag": "cadastro"
}
```

#### Agendamento

```json
{
  "nome": "João Silva",
  "email": "joao@email.com",
  "telefone": "(85) 98765-4321",
  "servico": "Corte de cabelo",
  "descricao_servico": "Corte moderno com acabamento na navalha.",
  "valor_servico": 30.00,
  "profissional": "Joao",
  "data": "25/10/2025",
  "hora": "14:30",
  "datetime": "2025-10-25T14:30:00",
  "tag": "agendamento"
}
```

### Variáveis dos Templates

Os templates de email usam as seguintes variáveis:

**Email de Confirmação:**
- `[NOME_CLIENTE]`
- `[DD/MM/AAAA]`
- `[HH:MM]`
- `[NOME_SERVICO]`
- `[DESCRICAO_SERVICO]`
- `[NOME_BARBEIRO]`
- `[DURACAO]`
- `[VALOR]`

---

## 💈 Serviços Disponíveis

| ID | Serviço | Descrição | Valor |
|----|---------|-----------|-------|
| 1 | Corte de cabelo | Corte moderno com acabamento na navalha | R$ 30,00 |
| 2 | Barba | Barba desenhada e hidratação com toalha quente | R$ 25,00 |
| 3 | Printura | Printura de cabelo com tinta temporária | R$ 15,00 |
| 4 | Pacote Completo | Cabelo + Barba + Printura com desconto especial | R$ 60,00 |

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

## 📞 Contato

**BarberBack - Barbearia Premium**

- 📍 Endereço: Av. Des. Moreira, 1301 - Aldeota, Fortaleza - CE
- 📧 Email: contato@barberback.com.br
- 📱 Telefone: (85) 98765-4321
- 💬 WhatsApp: [Clique aqui](https://wa.me/5585987654321)

---

## 🎯 Roadmap

### Próximas Funcionalidades

- [ ] Persistência de dados (SQLite/PostgreSQL)
- [ ] Interface web (Flask/Django)
- [ ] Dashboard administrativo
- [ ] Sistema de lembretes (24h antes)
- [ ] Histórico de serviços por cliente
- [ ] Programa de fidelidade
- [ ] Integração com pagamentos (PIX)
- [ ] App mobile (React Native)
- [ ] Sistema de avaliações
- [ ] Relatórios e analytics

---

## 🌟 Agradecimentos

- Agradecimento a todos o colaboradores da Equipe "Turma do Back" (Abraao, João, Paulo e Rodrigo)

---

<div align="center">

**Desenvolvido com ☕ e ✂️ para a comunidade barbeira**

 <img src="https://senac.ct.ws/dark_logo.png" alt="BarberBack" width="180" style="display: block; margin: 0 auto; max-width: 180px; height: auto;">


[⬆ Voltar ao topo](#-barberback---sistema-de-gestão-de-barbearia)

</div>

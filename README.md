# 🪒 BarberBack - Sistema de Gestão de Barbearia

![BarberBack](https://senac.ct.ws/white_logo.png)

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
- **Python 3.x** - Linguagem principal
- **urllib** - Requisições HTTP
- **json** - Manipulação de dados
- **datetime** - Validação de datas

### Frontend (Templates)
- **HTML5** - Estrutura dos emails
- **CSS3 Inline** - Estilização
- **Tailwind CSS** - Guia de estilo interativo

### Automação
- **Webhook** - Integração para envio de emails

---

## 📦 Pré-requisitos

- Python 3.7 ou superior
- Conexão com internet (para envio via webhook)

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

### 3. Configure o Webhook

Edite o arquivo `barbearia.py` e substitua a URL do webhook na linha 13:

```python
webhook_url = "SUA_URL_DO_WEBHOOK_AQUI"
```

### 4. Execute o sistema

```bash
python barbearia.py
# ou
python3 barbearia.py
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
barberback/
├── barbearia.py                    # Sistema principal
├── README.md                       # Este arquivo
├── emails/
│   ├── boas-vindas.html           # Template de boas-vindas
│   └── confirmacao-agendamento.html # Template de confirmação
├── assets/
│   ├── white_logo.png             # Logo branca (fundo escuro)
│   ├── dark_logo.png              # Logo escura (fundo claro)
│   ├── header_image.png           # Imagem hero
│   └── interior_barbearia.png     # Foto da barbearia
└── style-guide/
    └── guia-estilo.html           # Guia de estilo interativo
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

- Design inspirado em barbearias premium modernas
- Tipografia: [Google Fonts - Inter](https://fonts.google.com/specimen/Inter)

---

<div align="center">

**Desenvolvido com ☕ e ✂️ para a comunidade barbeira**

![BarberBack](https://senac.ct.ws/white_logo.png)

[⬆ Voltar ao topo](#-barberback---sistema-de-gestão-de-barbearia)

</div>

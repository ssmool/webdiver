# 🌐 Web Diver

**Web Diver** é uma ferramenta simples e poderosa de *web crawling* e automação de buscas na **World Wide Web**, desenvolvida em Python. O objetivo principal do Web Diver é realizar a leitura e arquivamento de conteúdos de URLs específicas, salvando os dados de forma estruturada em um banco de dados SQLite local.

---

## 🚀 Instalação

Antes de tudo, certifique-se de estar utilizando **Python 3.6+** e ter o `pip` atualizado.

### Instale via pip:
```bash
pip install webdiver_v1

pip install requests beautifulsoup4 pandas

⚙️ Funcionalidades Básicas
set_task_uri(url: str)
Define a URL que será utilizada na tarefa de leitura e busca de conteúdo na web.

Exemplo:

set_task_uri("https://example.com")

www_diver()
Executa a leitura da URL definida com set_task_uri() e armazena as informações extraídas no banco de dados SQLite.

Exemplo:

www_diver()

sql_setup(db_name: str)
Cria e configura um arquivo .db para manter os registros das pesquisas realizadas pelo Web Diver.

Exemplo:

sql_setup("webdiver_archive.db")

set_task(uri: str, hour: int, minute: int)
Agenda uma nova tarefa de web crawling para um horário específico, definindo a URL, a hora e o minuto da execução automática.

Exemplo:

set_task("https://example.com/news", 14, 30)

💡 Exemplos de Uso

from webdiver import set_task_uri, www_diver, sql_setup, set_task

sql_setup("mydata.db")
set_task_uri("https://example.com")
www_diver()

# Agendamento de tarefa
set_task("https://example.com", 12, 45)

🗃️ Banco de Dados
Os dados capturados são armazenados automaticamente em um banco SQLite com informações como:

URL acessada

Conteúdo HTML simplificado

Timestamp da coleta

👨‍💻 Desenvolvido por
#asytrick
Projeto disponível em: github.com/ssmool/webdiver

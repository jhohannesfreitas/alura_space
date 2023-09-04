"""
AULA 1 e 2

#Django:

1- Instalar o pacote Django: pip install Django. Sempre que instalar um pacote novo, lembrar de inseri-lo no pip freeze > requirements.txt
2- Criar um projeto: django-admin startproject nome_projeto. Coloque o nome como 'setup .' ou 'config .'
3- Use o comando 'python manage.py runserver' para subir o projeot na porta 8000.
4- Se quiser alterar a porta, passe o comando no terminal: python nomedoprojeto\manage.py runserver 8080
5- Você pode visualizar todos os comandos do Django: 'django-admin help'
6- Você pode alterar idioma e fuso horário no arquivo 'settings.py', linha 106
7- Você deve criar variáveis de ambiente para as SECRET_KEY, 'settings.py' na linha 23. O Github não aceitará projetos com essa secret_key visível para o usuário.
8- Para isso, instale o pacote no terminal 'pip install python-dotenv'. Sempre que instalar um pacote novo, lembrar de inseri-lo no pip freeze > requirements.txt
9- Criar um arquivo na raiz do projeto '.env' e cola a secret_key nele, sem ''.
10- Deixa a 'secret_key' como uma string vazia no arquivo 'settings.py'
11- Importa o OS no arquivo settings.py
12- inserir 'from dotenv import load_dotenv' no arquivo settings.py
12- chamar o método 'load_dotenv()' no arquivo settings.py
13- Alterar a variável secret_key no arquivo settings.py, chamando a variável criada no arquivo .env
14- A variável no arquivo secret_key deve ficar assim: SECRET_KEY = str(os.getenv('SECRET_KEY')).
15- Execute novamente o projeto no terminal 'python manage.py runserver'
16- O arquivo .env não será enviado para o github.
17- Crie o repositório no seu github
18- Crie um arquivo chamado '.gitignore' e informe os arquivos a serem ignorados. Pesquise no google por 'gitignore.io'
19- Dentro do site, pesquisa por 'Django', copia e cola todos os comandos no arquivo '.gitignore'
20- Pare o servidor com CTRL+BREAK
21- Insira no terminal 'git init' para iniciar um repositório local
22- Insira no terminal 'git add .' para ele copiar tudo que precisa do repositório local
23- Os arquivos que não serão enviados ao Github serão exibidos na cor cinza na barra de exibição lateral.
24- Vamos realizar o commit com git commit -m "projeto alura space". Depois disso o commit será criado.
25- Vamos acessar o repositório que criamos no Github. Nele, na seção "...or create a new repository on the command line", copiaremos a linha que traz, além de git remote add origin, o link do repositório.
No caso do instrutor, o comando era git remote add origin https://github.com/guilhermeonrails/alura_space.git, mas o link será diferente para cada repositório.
26- Vamos copiar esse comando e executá-lo no terminal. Depois, executaremos git push origin master. Depois disso, o código será enviado para o Github.
Atualizando o repositório, vamos acessar "setup > setting.py". Veremos que a Secret Key, e os outros objetos confidenciais, não foram enviados.

"""

"""
Ativando/Desativando o env

venv/Scripts/activate

deactivate

"""

"""
Aula - 3

Criamos nosso app usando: 'python manage.py startapp galeria'
Views e URLs -> Criamos a primeira página personalizada na web configurando rotas dentro dos arquivos views.py e urls.py;
Isolar URLs -> Aprendemos a boa prática de criação de um arquivo urls.py para cada app;
Templates -> Isolamos o template da app galeria, criando uma nova pasta chamada templates e reconfigurando o settings.py.
    - settings.py -> informar toda a parte visual da aplicação
    - cria uma pasta chamada templates e passa o caminho dela no 'DIRS' dentro de settings.py/TEMPLATES.
    - o caminho no 'DIRS': os.path.join(BASE_DIR, 'templates')
    - criar uma pasta dentro de templates com nome 'index.html' e configure sua página.
    - Diga para a view renderizar a página. Vá em galeria/views
    - Altero a minha função colocando o return render(request, 'index.html')


"""
"""
Aula 4
- criar uma pasta galeria dentro de templates e mover o arquivo index.html para dentro. Lembre de alterar o caminho do index dentro da views.py
- Ajustar os arquivos estáticos dentro de settings.py, linha 122.
- crie uma pasta dentro de setup, chamada stati
- Abaixo da linha 122 no settings.py, crie duas variáveis:
    #Onde todos os arquivos estáticos estão
    STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'setup/static')
]
    #caminho absoluto para o diretório onde o o python vai coletar esses arquivos estáticos para que ele faça a implantação/manipulação dos arquivos estáticos.
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
- Baixa os arquivos do projeto(assets, styles) no github e cola dentro da pasta 'static'
- Colete os arquivos estáticos usando o comando: python manage.py collectstatic
- carrega os arquivos estáticos dentro do index.html na linha 1: {% load static %}
- carrega os arquivos estáticos dentro do index.html que faz referência ao static/styles/style.css. Procura o caminho do css, linha 13.
- Na linha 13, inseri o código em python no html(indedando): href="{% static '/styles/style.css' %}"
- Para ajustar as imagens, vamos precisar inserir o "{% static 'caminho' %}" em todos os caminhos src de imagens dentro arquivo index.html. Pra facilitar, use o alt
para selecionar onde quer colar.
- cria um novo arquivo html dentro de templates/galeria, chamado imagem.html
- copia os códigos do arquivo imagem.html que você baixou no githut e cola nesse novo arquivo criado. Ajuste o arquivo inserindo os {% load static %} e {% static 'caminho' %}
- no galeria/views.py criar um novo método:
    def imagem(request):
    return render(request, 'galeria/imagem.html')

AULA 5

- Em galeria/urls.py precisa criar o caminho das imagens.
- Lembre de importar: from galeria.views import index, imagem
    urlpatterns = [
    path('', index),
    path('imagem/', imagem, name='imagem')
    ]

- Dentro do arquivo index.html, ajuste em href="imagem.html" por "{% url 'imagem' %}"
- ajuste também o path do index no arquivo urls.py
    path('', index, name='index'),
- no arquivo imagem.html, aponde onde estiver "index.html" para "{% url 'index' %}"

- DRY (Don't Repeat Yourself - Não se repita, numa tradução livre
    vamos criar um novo arquivo chamado dentro de templates/galeria/base.html
    cole tudo que for repetido do imagem.html e index.html neste arquivo base.html
    nos arquivos imagem.html e index.html será necessário vincular ao base.html colocando o comando na linha 1:
        {% extends 'galeria/base.html' %}
- Precisamos definir no body do base.html o {% block content %}{% endblock %}. Nos arquivos index.html e imagem.html
será necessário informar o ínício(block content) e o fim (endblock).
-criar uma nova pasta dentro de templates/galerias/partials. Crie uma arquivo chamado _footer.html, copie e cole o footer do index.html ou imagem.html
- No arquivo _footer.html, insira o {% load static %}
- incluir o _footer no meu arquivo base.html
    {% include 'galeria/partials/_footer.html' %}

"""
"""
ORM -> Busca as querys sql. 
    -Não precisa investir muito tempo em querys sql.
    -Django
    - SqlAlchemy
"""



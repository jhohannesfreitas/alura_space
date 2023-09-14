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
Sobre o ambiente virtual (.env):

Criando um novo ambiente virtual -> python -m virtualenv .venv

Ativando o env-> venv/Scripts/activate

Desativando o env-> deactivate

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

# ___________________________________________________________
"""
Curso: Django persistência de dados e Admin

Aula 1

Sobre o Github

Clonar projetos -> git clone 'caminho git hub'

Para instalar todos os pacotes que estão no requirements.txt: pip install -r requirements.txt

AULA 2

Banco de dados:
- Responsável: models.py
- Dentro de galeria/models.py criamos a class com os dados do banco
- ORM -> ponte entre o BD e o python
- Cada atributo no model representa um campo no banco de dados
    -class Person(models.Model):
    first_name = models.CharField(max_length=30)
    -No banco de dados ficaria assim:
    CREATE TABLE myapp_person (
    "id" serial NOT NULL PRIMARY KEY,
    "first_name" varchar(30) NOT NULL,
- Todo model é uma class Python, subclasse de django.db.models.Model
- Comando para traduzir o django que existem tabelas para o banco: python manage.py makemigrations
- Ele criará um documento chamado 0001
- Comando para importar a class e criar as tabelas no banco: python manage.py migrate
- Instale a extenção SQLite View no vscode para poder visualizar as tabelas.
- Adicionando novos itens na minha tabela:
    python manage.py shell
    from galeria.models import Fotografia
    foto = Fotografia(nome="Nebulosa de Carina", legenda="webbtelecope.org / NASA / James Webb", foto="carina-nebula.png")
    foto.save()
    Fotografia.objects.all()

- No settings.py, em INSTALLED_APPS, inserir o caminho do arquivo de galeria/apps.py -> 'galeria.apps.GaleriaConfig'
- Deixamos as imagens mais dinâmicas atribuindo variáveis e parâmetros. 
- Ajustamos o galeria/urls.py e galeria/views.py 


Acesso ao Django Admin
    -http://127.0.0.1:8000/admin
    -criar o super usuário: python manage.py createsuperuser
        - jhohannes.freitas / 123456
        - teste / sSBN8830#
    -CRUD Admin
    -no arquivo galeria/admin.py fazemos todas as configurações
        - from galeria.models import Fotografia
        - class ListandoFotografia(admin.ModelAdmin):
            list_display = ("id", "nome", "legenda")
            list_display_links = ("id", "nome")
            search_fields = ("nome",)
        admin.site.register(Fotografia, ListandoFotografia)
        
    - A partir dai dentro do próprio admin, podemos adicionar, modificar a nossa Fotografia.
    - Podemos cadastrar novos usuários e inserir permissões de acesso
    - Podemos inserir grupos de usuários com conjuntos de permissões e delegar quais usuários/utilizadores fazem parte desse grupo.
    

Voltamos para o model para ajustar as categorias
    -OPCOES_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta"),
    ]
    -categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    -Depois de qualquer ajuste no model, precisa chamar novamente as migrations
    -python manage.py makemigrations (cria novas migrações com base nas alterações detectadas nos modelos)
    -python manage.py migrate (sincroniza o estado do banco de dados com o conjunto atual de modelos e migrações)
    
O que aprendemos na AULA 2:
Aprendemos como fazer alterações nos templates para acessar as referências do banco de dados utilizando {{}} e {%%};
Criamos um superuser no terminal para permitir o acesso ao Django Admin;
Incluímos a tabela Fotografia no Django Admin, possibilitando o acesso, deleção, inclusão e alteração de itens na tabela do banco de dados através de uma rota na web;
Personalizamos o Django Admin para melhorar a usabilidade do administrador do nosso site.
    

AULA 3
- Inserindo um filtro por categoria no meu painel admin
    list_filter = ("categoria",)
- Inserindo uma paginação no meu painel admin
    list_per_page = 10

- Voltando para o galeria/models.py, se deixa a imagem visível ou não para o usuário.
    -publicada = models.BooleanField(default=False)
    -python manage.py makemigrations (cria novas migrações com base nas alterações detectadas nos modelos)
    -python manage.py migrate (sincroniza o estado do banco de dados com o conjunto atual de modelos e migrações)
    
- Voltando para o galeria/views.py, inserindo a lógica para filtrar somente os que estão publicados
    -fotografias = Fotografia.objects.filter(publicada=True)
    -Depois disso, será necessário ir no painel admin e ajustar as imagens marcando o campo 'Publicada'(True).
- Voltando no galeria/admin.py, vamos ajustar para que o 'Publicada' apareça no painel.
    -list_display = ("id", "nome", "legenda", "publicada")
    -Alterando um dado ali mesmo no display:
        - list_editable = ("publicada",)
        
- Inserindo um novo campo data no banco pelo galeria/models.py
    -from datetime import datetime
    -data_fotografia = models.DateTimeField(default=datetime.now, blank=False)
    -python manage.py makemigrations (cria novas migrações com base nas alterações detectadas nos modelos)
    -python manage.py migrate (sincroniza o estado do banco de dados com o conjunto atual de modelos e migrações)

- Ordenando qual imagem aparece primeiro na galeria/views.py
    -fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True) ->invertida
    -fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

O que aprendemos na AULA 3?

Adicionamos dois novos campos no model Fotografia. Um deles guarda informações de data e o outro se trata de um campo booleano;
Através dos novos campos, adicionamos a funcionalidade de publicação e a funcionalidade de sempre mostrar as fotografias mais recentes na página principal.



AULA 4:

- Alterar o campo de anexar foto
    - vai no settings.py para criar um diretório específico para os arquivos de mídia. 
    - semelhante ao que foi feito para os arquivos estáticos.
    -MEDIA_ROOT = os.path.join(BASE_DIR, "media")
    -MEDIA_URL = "/media/"
    -Depois precisamos ir no setup/urls.py e referenciar
        from django.conf import settings
        from django.conf.urls.static import static
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    - volta no galeria/models.py e ajusta o campo foto
        -foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
        -python manage.py makemigrations (cria novas migrações com base nas alterações detectadas nos modelos)
        -python manage.py migrate (sincroniza o estado do banco de dados com o conjunto atual de modelos e migrações)
        -depois disso basta inserir a nova imagem no painel admin. Precisei baixar a imagem do google antes.
        -Perceba que depois de inserir a nova imagem, a pasta media é criada conforme configuramos com subpastas de ano/mês/dia, porque pode ter arquivos com mesmo nome.
        -ao abrir a nossa página web, a imagem nova não aparece. Vamos ajustar?
            - Baixe uma imagem not-found e insira na pasta setup\static\assets\imagens\galeria. Também coloquei aqui a imagem nova que inseri.
            - Volte no arquivo templates/index.html e coloque uma condição depois do href de <li>:
                {% if fotografia.foto == "" or fotografia.foto == null %}
                <img class="card__imagem" src="{% static '/assets/imagens/galeria/not-found.png'%}" alt="foto">
                {% else %}
                <img class="card__imagem" src="{{ fotografia.foto.url }}" alt="foto">
                {% endif %}
            - Por fim, importe novamente as imagens das outras fotos que já estavam no projeto, pois elas irão sumir.
        - É necessário ajustar o arquivo templates/imagem.html também
            -depois de <div class="imagem__conteudo">
            {% if fotografia.foto == "" or fotografia.foto == null %}
            <img class="imagem__imagem" src="{% static '/assets/imagens/galeria/not-found.png'%}">
            {% else %}
            <img class="imagem__imagem" src="{{ fotografia.foto.url }}">
            {% endif %}
        - Altere a referência do nome quando inserir uma foto nova dentro de galeria/models.py
                def __str__(self):
                    return self.nome

osb:
- Podemos buscar todos os objetos em galeria/views.py, por exemplo: Fotografia.objects.all().
- Podemos adicionar mais de um filtro em galeria/views.py, por exemplo: 
    Fotografia.objects.order_by('-data_fotografia').filter(publicada=True).filter(categoria=nebulosa)


O que aprendemos nesta aula:

-Aprendemos a criar referências globais para armazenamento de arquivos de mídia no settings.py;
-Inserimos um campo ImageField no model Fotografia que irá permitir o upload de novas imagens no website;
-Criamos um novo diretório designado apenas para o armazenamento das fotografias do website.


AULA 5

-Fazer o botão de busca funcionar
    -galeria/urls.py
    -cria um novo path
    -from galeria.views import index, imagem, buscar
    -path("buscar", buscar, name="buscar")
    -Depois volta no galeria/views.py e cria essa rota feita na urls.py
    -def buscar(request):
        return render(request, "galeria/buscar.html")
    -cria um novo arquivo dentro de templates/galeria/buscar.html
        <h1>buscar</h1>
    -inserir no templates/galeria/partials/_menu.html a chamada do mecanismo de busca depois da <div class="busca__fundo">
        <form action="{% url 'buscar' %}">
            <input class="busca__input" type="text" name="buscar" placeholder="O que você procura?">
            <button type="submit">
                <img class="busca__icone" src="{% static '/assets/ícones/1x/search.png' %}" alt="ícone de search">
            </button>
        </form>
    -copiar tudo do galeria/index.html e colar em buscar.html
    -inserir depois do else, tando no index.html quanto em buscar.html
        <div class="imagem__texto">
            <p>Fotografia não encontradas</p>
        </div>
    -precisamos ajustar novamente em galeria/views.py a função buscar
        def buscar(request):
            fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)

            if "buscar" in request.GET:
                nome_a_buscar = request.GET['buscar']
                if nome_a_buscar:
                    fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
        
            return render(request, "galeria/buscar.html", {"cards": fotografias})

O que aprendemos nesta aula:
Construímos uma nova funcionalidade para o website através da criação de uma nova url, view e template;
Entendemos como criar queries nas nossas views para checar o nome de cada fotografia e comparar com a informação adquirida pelo formulário do mecanismo de busca.


# Curso Django: autenticação de formulários e alertas

Aula 1

-crie um novo app chamado usuarios
    -python manage.py startapp usuarios
    -informe o arquivo setup/settings.py INSTALLED_APPS sobre a criação deste novo app
        "usuarios.apps.UsuariosConfig",
    -como boa prática, criamos um novo arquivo chamado urls.py dentro do app usuarios
    -copia tudo de galeria/urls.py e cola neste novo arquivo usuarios/urls.py. Ajustando e removendo o que for necessário
        from django.urls import path

        urlpatterns = [
        
        ]
    -precisamos criar um novo path para informar o setup/urls.py sobre a criação de um novo arquivo direcionando para usuarios/urls.py
        -path("", include("usuarios.urls"))    
        
    - Vamos inserir nossas usuarios/urls.py
        from usuarios.views import login, cadastro

        urlpatterns = [
            path('login', login, name='login'),
            path('cadastro', cadastro, name='cadastro'),
        ]
    - Vamos inserir nossa visualização em usuarios/views.py
        def login(request):
            return render(request, "usuarios/login.html")
    
    def cadastro(request):
            return render(request, "usuarios/cadastro.html")
-Boas práticas, vamos criar uma pasta dentro de templates chamada usuarios
-Vamos ajustar no templates/galeria/partials/_menu.html e ajustar o menu de navegação
        <a href="{% url 'login' %}"><img src="{% static '/assets/ícones/1x/Mais vistas - inativo.png' %}"> Login</a>
        <a href="{% url 'cadastro' %}"><img src="{% static '/assets/ícones/1x/Novas - inativo.png' %}"> Cadastro</a>
-inserimos o código html já pronto nos arquivos templates/usuarios/cadastro.html e login.html

Aprendemos nesta aula:

Criamos um novo app de usuarios através do comando python manage.py startapp usuarios;
Configuramos as URLs e views do novo app de usuarios para que pudéssemos acessar seus respectivos templates;
Alteramos o index.html para redirecionar para as novas páginas de Login e Cadastrar. Fizemos isso por meio da utilização do menu lateral da página inicial do site.
    

Aula 2

- Crie um novo arquivo dentro de usuarios/forms.py para criar classes que vão mexer no nosso formulário
    from django import forms

    class LoginForms(forms.Form):
        nome_login = forms.CharField(
            label="Nome de login",
            required=True,
            max_length=100
        )
        senha = forms.CharField(
            label="Senha",
            required=True,
            max_length=70,
            widget=forms.PasswordInput()
        )
- volte em usuarios/views.py e importe o formulário criado
    from usuarios.forms import LoginForms
    def login(request):
        form = LoginForms()
        return render(request, "usuarios/login.html", {"forme": form})
- depois ajuste o templates/usuarios/login.html e ajuste apagando todos os imputs depois de <div class="row">
- uso do {% csrf_token %} para segurança do formulário
    O Cross-Site Request Forgery ou CSRF é uma vulnerabilidade na segurança da web que possibilita que alguma ameaça se passe por clientes comuns. 
    Assim, ela pode se disfarçar como o servidor e passar informações através do método POST. 
    Após o recebimento pelo usuário, o token é checado novamente. O servidor só aceita o POST caso o CSRF Token se provar igual ao enviado inicialmente.    
- antes da tag form, para garantir a segurança do formulário insira:
    <form action="" method="">
        {% csrf_token %}
- depois da div ficaria assim:
    <div class="row">
        {% for field in form.visible_fields %}
        <div>
            <label for="{{ field.id_for_label }}">{{field.label}}</label>
            {{ field }}
        </div>
        {% endfor %}
    </div>
- vamos criar novamente o nosso botão de logal no arquivo login.html
    <div>
        <button type="submit">Logar</button>
    </div>
    
- vamos ajustar os estilos das divs, buttons e labels no meu arquivo templates/usuarios/login.html copiando do arquivo cadastro.html
- depois disso, vamos estilizar dentro do forms.py ajustando a classe LoginForms
    class LoginForms(forms.Form):
        nome_login = forms.CharField(
            label="Nome de login",
            required=True,
            max_length=100,
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: João Silva"
                }
            )
        )
        senha = forms.CharField(
            label="Senha",
            required=True,
            max_length=70,
            widget=forms.PasswordInput(
                attrs={
        "class": "form-control",
                 "placeholder": "Digite sua senha"
                }
            )
        )

- Ajustaremos agora o formulário de cadastro.html, vamos começar primeiro pelo forms.py criando a class
    class CadastroForms(forms.Form):
        nome_cadastro = forms.CharField(
            label="Nome de Cadastro",
            required=True,
            max_length=100,
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: João Silva"
                }
            )
        )
        email = forms.EmailField(
            label="Nome de email",
            required=True,
            max_length=100,
            widget= forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex.: joaosilva@xpto.com"
                }
            )
        )
        senha_1 = forms.CharField(
            label="Senha",
            required=True,
            max_length=70,
            widget=forms.PasswordInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite sua senha"
                }
            )
        )
        senha_2 = forms.CharField(
            label="Senha",
            required=True,
            max_length=70,
            widget=forms.PasswordInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite sua senha novamente"
                }
            )
        )
- precisamos importar para a nossa usuarios/viewes.py   
    from usuarios.forms import LoginForms, CadastroForms
        def cadastro(request):
            form = CadastroForms()
            return render(request, "usuarios/cadastro.html", {"form": form})
- vamos copiar todo o formulário inserido em login.html e colar no form do cadastro.html, lembrando de trocar o botão de "Logar" por "Cadastrar"

O que aprendemos nesta aula:

Criamos um novo arquivo chamado forms.py dentro do app de usuario;
Criamos dois novos formulários: Login e Cadastro. Fizemos isso através da criação de classes que representam formulários, com o módulo forms nativo do Django;
Alteramos os templates login.html e cadastro.html para acessar as classes de formulários em forms.py e mostrá-los no site.


Aula 3
- Ajustar no arquivo de login.html
    <form action="{% url 'login' %}" method="POST">
- Ajustar no arquivo de cadastro.html
    <form action="{% url 'cadastro' %}" method="POST">

- Agora vamos tornar nossas páginas responsivas em usuarios/views.py
    from django.shortcuts import render, redirect
    from usuarios.forms import LoginForms, CadastroForms
    from django.contrib.auth.models import User
    
    
    def login(request):
        form = LoginForms()
        return render(request, "usuarios/login.html", {"form": form})
    
    
    def cadastro(request):
        form = CadastroForms()
    
        if request.method == 'POST':
            form = CadastroForms(request.POST)
    
            if form.is_valid():
                if form["senha_1"].value() != form["senha_2"].value():
                    return redirect('cadastro')
    
                nome = form["nome_cadastro"].value()
                email = form["email"].value()
                senha = form["senha_1"].value()
    
            if User.objects.filter(username=nome).exists():
                return redirect('cadastro')
    
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            return redirect('login')
    
        return render(request, "usuarios/cadastro.html", {"form": form})

- agora a nossa tela de cadastro já funciona, precisamos mostrar a tela de login.
- ajustamos a nossa usuarios/views.py de login 
- precisamos inserir alertas importando o 'messages'
    from django.contrib import messages
    messages.success(request, f"{nome} logado com sucesso!") ->se der sucesso
    messages.error(request, "Erro ao efetuar login") -> se der erro
-será necessário inserir nos meus arquivos templates/usuarios/login.html e cadastro.html. Também será necessário incluir no arquivo _menu.html
    {% for message in messages %}
    <did>
        <p id="messages">{{message}}</p>
    </did>
-Precisará copiar e colar o boostrap do arquivo login.html para a minha base.html também
-Será necessário criar a minha função de logout na usuarios/viewes.py
    def logout(request):
    auth.logout(request)
    messages.success(request,"Logout efetuado com sucesso!")
    return redirect('login')
-Depois redicionar nas minhas usuarios/urls.py
    from usuarios.views import login, cadastro, logout


    urlpatterns = [
        path('login', login, name='login'),
        path('cadastro', cadastro, name='cadastro'),
        path('logout', logout, name='logout'),
    
    ]

-Altere no template de login.html, cadastro.html e _menu.html

O que aprendemos nesta aula:
-Aprendemos que o Django possui um banco de dados interno para armazenar informações sobre os usuários do projeto;
-Vimos como alterar as views do app usuarios para possibilitar o acesso e alteração no banco de dados interno do Django;
-Criamos nossas próprias condições de autenticação no views.py para as informações vindas dos formulários;
-Inserimos mensagens e alertas nos templates do site.


Aula 4

- Vamos precisar ajustar o bootstrap do arquivo static/styles/style.css, inserindo o comando/classes:
    .alert {
    --bs-alert-bg: transparent;
    --bs-alert-padding-x: 1rem;
    --bs-alert-padding-y: 1rem;
    --bs-alert-margin-bottom: 1rem;
    --bs-alert-color: inherit;
    --bs-alert-border-color: transparent;
    --bs-alert-border: 1px solid var(--bs-alert-border-color);
    --bs-alert-border-radius: 0.375rem;
    position: relative;
    padding: var(--bs-alert-padding-y) var(--bs-alert-padding-x);
    margin-bottom: var(--bs-alert-margin-bottom);
    color: var(--bs-alert-color);
    background-color: var(--bs-alert-bg);
    border: var(--bs-alert-border);
    border-radius: var(--bs-alert-border-radius);
    }
    
        .alert-primary {
        --bs-alert-color: #084298;
        --bs-alert-bg: #cfe2ff;
        --bs-alert-border-color: #b6d4fe;
    }

- Remova o link do bootstrap que estava dando conflito do seu arquivo templates/galeria/base.html
- vamos precisar ajustar a galeria/views.py para mostrar imagens apenas se a pessoa estiver logada.
    from django.shortcuts import render, get_object_or_404, redirect
    from django.http import HttpResponse
    from galeria.models import Fotografia
    from django.contrib import messages
    
    def index(request):
        if not request.user.is_authenticated:
            messages.error(request, "Usuário não logado!")
            return redirect('login')
        
    def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado!")
        return redirect('login')
        
- Associando as minhas fotos a um usuário específico
    - vamos criar um novo campo no galeria/models.py
        from django.contrib.auth.models import User
        usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user",
    )
    -python manage.py makemigrations (cria novas migrações com base nas alterações detectadas nos modelos)
    -python manage.py migrate (sincroniza o estado do banco de dados com o conjunto atual de modelos e migrações)
    
-Vamos precisar alterar o arquivo galeria/admin.py inserindo um filtro também de usuário
    list_filter = ("categoria","usuario",)

-Validando nome de usuário dentro do forms.py na class CadastroForms
        def clean_nome_cadastro(self):
        nome = self.clean_data.get("nome_cadastro")
        
        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError("Não é possível inserir espaços dentro do campo usuário")
            else:
                return nome
-Vamos precisar ajustar a validação de senhas também dentro do arquivo forms.py
        def clean_senha_2(self):
        senha_1 = self.cleaned_data.get("senha_1")
        senha_2 = self.cleaned_data.get("senha_2")

        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError("Senhas não são iguais")
            else:
                return senha_2
-Em usuarios/views.py, remova a validação de senha, pois você já está fazendo dentro do arquivo forms.py
    
O que aprendemos nesta aula:

Criamos um novo campo no model de Fotografia e o associamos à tabela de usuários presente no banco de dados interno do Django;
Criamos novas validações nos dados vindos do formulário utilizando a boa prática do Clean;
Inserimos mensagens de erro personalizadas para cada campo dos formulário que pudesse ter seu input incorreto.


Aula 5

- Vamos criar uma partial para alertas em templates/galeria/partials/_alertas.html
- vamos copiar os alertas de login.html ou cadastro.html e colar no meu arquivo _alertas.html
    {% if messages %}
        {% for message in messages %}
            <did class="alert alert-primary">
                {{message}}
            </did>
        {% endfor %}
    {% endif %}
- Depois disso, vamos deletar isso de login.html e cadastro.html, redirecionando nos 2 arquivos para _alertas.html
        {% include 'galeria/partials/_alertas.html' %}
- Vamos inserir no setup/settings.py uma configuração para mensagens própria do django
    from django.contrib.messages import constants as messages
    MESSAGE_TAGS = {
        messages.ERROR: 'danger',
        messages.SUCCESS: 'success',
    }
- Depois voltamos na nossa partials e alteramos o arquivo _alertas.html chamando esse alerta de settings.py
    {% if messages %}
        {% for message in messages %}
            <did class="alert alert-{{ message.tags }}">
                {{message}}
            </did>
        {% endfor %}
    {% endif %}
- Vamos precisar inverter os links do bootstrap nos nossos arquivos de login.html

- Vamos reorganizar a nossa pasta de templates
    -mova a pasta partials para dentro de templates, retirando-a de galeria
    -vamos precisar ajustar os caminhos dos arquivos(login, cadastro e base) que apontavam para o antigo caminho, removendo:
        galeria/
        

O que aprendemos nesta aula:

-Criamos uma no partial chamada _alertas.html para evitar a repetição de código envolvendo mensagens e alertas;
-Alteramos o settings.py para criar uma padronização de todos os alertas de erro e de sucesso;
-Reorganizamos os diretórios de templates para ficar de acordo com as melhores práticas de utilização do Django.

"""

"""

Curso CRUD e persistência no S3

Aula 1


- Reorganizando os meus aplicativos galeria e usuários dentro de uma única pasta apss
- Vamos precisar alterar o caminho de alguns arquivos, importando para o caminho novo o 'apps.' antes do caminho do arquivo.
    -setup/settings.py 
        INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'apps.galeria.apps.GaleriaConfig',
        "apps.usuarios.apps.UsuariosConfig",
        ]
        
    -apps/galeria/apps.py
        from django.apps import AppConfig


        class GaleriaConfig(AppConfig):
            default_auto_field = 'django.db.models.BigAutoField'
            name = 'apps.galeria'
    
    - apps/galeria/admin.py
        from apps.galeria.models import Fotografia
    
    -apps/galeria/urls.py
        from apps.galeria.views import index, imagem, buscar
    
    -apps/galeria/views.py
        from apps.galeria.models import Fotografia
    
    -apps/usuarios/apps.py
        from django.apps import AppConfig

        
        class UsuariosConfig(AppConfig):
            default_auto_field = 'django.db.models.BigAutoField'
            name = 'apps.usuarios'
    
    -apps/usuarios/urls.py
        from apps.usuarios.views import login, cadastro, logout
    
    -apps/usuarios/views.py
        from apps.usuarios.forms import LoginForms, CadastroForms
    
    -setup/urls.py
            from django.contrib import admin
            from django.urls import path, include
            from django.conf import settings
            from django.conf.urls.static import static
            
            
            urlpatterns = [
                path('admin/', admin.site.urls),
                path('', include('apps.galeria.urls')),
                path("", include("apps.usuarios.urls"))
            ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        
- Criar um novo diretório dentro de templates chamado 'shared' e mova o arquivo templates/galeria/base.html para dentro dele.
    - Depois de mover, ajuste o caminho de base.html nos arquivos: buscar.html, imagem.html e index.html
    
- vamos reduzir a quantidade de códigos repetidos nos arquivos html
    -login.html e cadastro.html : apague da linha 43 pra cima e insira o código abaixo no topo
        {% extends 'shared/base.html' %}
        {% load static %}
        {% block content %}
        {% endblock %} - no final

- Como o bootstrap foi removido do html dos arquivos login e cadastro, vamos precisar inserir no final do código algumas estilizações no arquivo
static/styles/style.css / pegue os códigos na aula 1 video aula 06

O que aprendemos Nesta aula:

-Organizamos os diretórios do projeto para melhorar nossa navegação na IDE;
-Utilizamos dos conceitos de partials para deixar o código de templates mais dinâmico.


Aula 2

- Vamos inserir CRUD na parte de templates/partials/_menu.html
    <a href=""><img src="{% static '/assets/ícones/1x/new.png' %}"> Nova Imagem</a>
    -a imagem precisa estar dentro de setup/static/assets/icones/1x/new.png

- vamos inserir as urls novas em apps/galeria/urls.py
    from apps.galeria.views import \
    index, imagem, buscar, nova_imagem, editar_imagem, deletar_imagem
    
    path("nova-imagem", nova_imagem, name="nova_imagem"),
    path("editar-imagem", editar_imagem, name="editar_imagem"),
    path("deletar-imagem", deletar_imagem, name="deletar_imagem")

- vamos precisar criar nossos métodos as apps/galeria/viewes.py também
    def nova_imagem(request):
    pass

    def editar_imagem(request):
        pass
    
    def deletar_imagem(request):
        pass


- Por fim, volto no meu botão em templates/partials/_menu.html e redireciono o caminho
    <a href="{% url 'nova_imagem' %}"><img src="{% static '/assets/ícones/1x/new.png' %}"> Nova Imagem</a>
    
- Voltamos na nossa views.py e ajustamos a minha função de 'nova_imagem'
    def nova_imagem(request):
    return render(request, 'galeria/nova_imagem')
    
- Criei o arquivo 'nova_imagem' dentro de templates/galeria e inserimos um código html simples, apenas para abrir a página.
- Copia todo o html de login.html e cola no arquivo nova_imagem.html

- Cria um novo arquivo dentro de apps/galeria/forms.py
- esse forms.py vai ser baseado com o meu apps/galeria/models.py
- O Django tem um recurso para nos ajudar a fazer formulários baseados em models. 
Ele encontra os models existentes e cria um formulário com base neles. 
Só precisamos informar qual model deve ser usado para o formulário.
    from django import forms
    from apps.galeria.models import Fotografia
    
    
    class FotografiaForms(forms.ModelForm): #criando um model a partir de um já existente
        class Meta:
            model = Fotografia
            exclude = ['publicada',]
    
            widgets = {
                'nome': forms.TextInput(attrs={'class': 'form-control'}),
                'legenda': forms.TextInput(attrs={'class': 'form-control'}),
                'categoria': forms.Select(attrs={'class': 'form-control'}),
                'descricao': forms.Textarea(attrs={'class': 'form-control'}),
                'foto': forms.FileInput(attrs={'class': 'form-control'}),
                'data_fotografia': forms.DateInput(
                    format='%d/%m/%Y',
                    attrs={
                        'type': 'date',
                        'class': 'form-control'}),
                'usuario': forms.Select(attrs={'class': 'form-control'}),
            }

- Depois do forms.py ajustado, precisamos montar a nossa lógica na apps/galeria/views.py dentro das minhas funções criadas
    from apps.galeria.forms import FotografiaForms
    
    def nova_imagem(request):
    form = FotografiaForms
    return render(request, 'galeria/nova_imagem.html', {'form': form})

- Ajustando os nomes do meu apps/galeria/forms.py
    labels = {
            'descricao': 'Descrição',
            'data_fotografia': 'Data de registro',
            'usuario': 'Usuário',


        } 
    
- Vamos modificar também o publicada no meu apps/galeria/models.py
    publicada = models.BooleanField(default=True)
    -python manage.py makemigrations (cria novas migrações com base nas alterações detectadas nos modelos)
    -python manage.py migrate (sincroniza o estado do banco de dados com o conjunto atual de modelos e migrações)
    
-voltar para as views.py para inserir a nossa lógica na função 'nova_imagem'
    def nova_imagem(request):
    # verica se o usuário está logado
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado!")
        return redirect('login')
    
    # caso o usuário preencha o form, seja salvo dentro do banco de dados 
    form = FotografiaForms
    if request.method == 'POST':
        form = FotografiaForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Nova fotografia cadastrada")
            return redirect('index')
            
    return render(request, 'galeria/nova_imagem.html', {'form': form})
    
- No arquivo templates/galeria/nova_imagem.html, vamos ajustar o nome do botão 'logar' para Cadastrar Nova Fotografia.
- Ainda no arquivo templates/galeria/nova_imagem.html altere também a linha para:
    <form action="{% url 'nova_imagem' %}" method="POST" enctype="multipart/form-data">
    
- Em apps/galeria/views.py vamos ajustar para pegar além do POST, também os arquivos (imagens)
    form = FotografiaForms(request.POST, request.FILES)
    
- Vamos criar o nosso botão de editar/deletar dentro de templates/galeria/imagem.html
    <div>
        <a href="{% url 'editar_imagem' %}"><button class="btn btn-success col-12" style="padding: top 5px;">Editar</button></a>
        <a href="{% url 'deletar_imagem' %}"><button class="btn btn-danger col-12" style="padding: top 5px;">Deletar</button></a>
    </div>
    
O que aprendemos nesta aula:
-Criamos um formulário a partir de um model existente;
-Recebemos os dados do formulário preenchido e criamos um novo item na tabela do banco de dados usando o comando form.save();
-Criamos algumas novas views alterando o arquivo de URLs, views e diretório de templates.
    
    
Aula 3

- Capturando o ID das imagens
- Vamos no arquivo imagem.html e inserimos fotografia.id na nossa url tanto pra editar quanto pra deletar
- Abrindo a apps/galeria/urls.py vamos ajustar o path de editar_imagem e deleta_imagem inserindo
    /<int:foto_id>
- Em apps/galeria/viwes.py vamos montar a nossa função de editar_imagem
    def editar_imagem(request, foto_id):
    fotogragia = Fotografia.objects.get(id=foto_id)
    form = FotografiaForms(instance=fotogragia)

    return render(request, 'galeria/editar_imagem.html', {'form': form})
- cria um novo arquivo em templates/galeria/editar_imagem.html
- copia o mesmo molde html de nova_imagem.html e cola em editar_imagem.html
- altere a url de action para 'editar_imagem' e altere o nome do botão para 'Editar Fotografia'
- Ajustando os filtros de busca dentro de templates/galeria/index.html
    <ul class="tags__lista">
        <li class="tags__tag"><a href="{% url 'filtro' 'NEBULOSA' %}" class="btn" style="color: #C9C9C9;">Nebulosa</a></li>
        <li class="tags__tag"><a href="{% url 'filtro' 'ESTRELAS' %}" class="btn" style="color: #C9C9C9;">Estrelas</a></li>
        <li class="tags__tag"><a href="{% url 'filtro' 'GALÁXIA' %}" class="btn" style="color: #C9C9C9;">Galáxia</a></li>
        <li class="tags__tag"><a href="{% url 'filtro' 'PLANETA' %}" class="btn" style="color: #C9C9C9;">Planeta</a></li>
    </ul>
- Vamos criar o path para o filtro em apps/galeria/urls.py
    path('filtro/<str:categoria>', filtro, name='filtro')

- Em apps/galeria/views.py vamos criar a função para o filtro
    def filtro(request, categoria):
        fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True, categoria=categoria)
    
        return render(request, 'geleria/index.html', {'cards': fotografias})
        
- Vamos ajustar o retorno da função de busca em apps/galeria/viwes.py para:
    galeria/index.html
    depois disso podemos apagar o arquivo busca.html
    
    
O que aprendemos nesta aula:

-Passamos valores por variáveis para as views através das URLs;
-Criamos a nova view de edição dentro do arquivo views.py em apps/galeria;
-Construímos a nova view de deleção que irá garantir o DELETE do CRUD das fotografias;
-Implementamos a nova funcionalidade de filtro para selecionar as fotografias presentes em cada uma das categorias existentes.

AULA 4

- criação da conta na AWS
- criação do bucket no S3 da AWS: "fotografias-alura-space"
- vamos buscar por "IAM" para criar e gerenciar identidades(pessoas usuárias) para uma página
- No painel IAM, busque por "Usuários" no menu lateral em "Adicionar usuários".
- No campo nome de usuário deixe como "django-dev". A opção "Habilitar acesso ao console" deve estar desabilitada.
- licaremos em "Próximo", o que nos levará para a tela "Definir permissões". 
Nela, definiremos quais permissões a pessoa usuária terá. Na seção "Opções de permissões", selecionaremos "Anexar políticas diretamente".
- Selecione o campo de busca e digite "s3", seguido de "Enter". buscaremos e escolheremos a "AmazonS3FullAccess", clicando na caixa de seleção à sua esquerda.
- Abaixo desta seção, clicaremos em "Próximo", o que nos levará para a tela "Revisar e criar". 
- Nela, revisaremos o nome e a permissão que concedemos. Abaixo destes dados, clicaremos em "Criar usuário".
- Para poder utilizar este login de pessoa usuária na aplicação do Django, precisaremos criar uma credencial de segurança.
- Para isso, clicaremos na aba "Credenciais de segurança", localizada acima do título da seção atual.
- Buscaremos a seção "Chaves de acesso", onde clicaremos no botão "Criar chave de acesso" e seremos direcionados para a 
tela "Práticas recomendadas e alternativas para chaves de acesso", onde selecionaremos a opção "Command Line Interface (CLI)".

- Abaixo desta seção, surgirá uma mensagem de recomendação junto a uma caixa de seleção indicando que compreendemos a 
recomendação acima e queremos prosseguir, ignorando-a por enquanto. Marcaremos esta opção e abaixo dela, clicaremos em "Próximo".

- Seremos direcionados para a tela "Definir etiqueta de descrição" que possui um campo a ser preenchido com a descrição da 
chave de acesso. Não preencheremos nenhuma etiqueta, e clicaremos diretamente em "Criar chave de acesso", abaixo da seção.

O que aprendemos nesta aula:
-Vimos que é interessante criar um bucket no S3 da AWS para persistir as fotografias de forma independente do servidor no qual o projeto está rodando;
-Criamos nosso bucket na S3 acessando o site da AWS, criando a nossa conta e colocando as configurações de acesso públicas;
-Criamos um novo usuário no IAM através do acesso à nossa conta da AWS e garantimos ao mesmo um FullAccess ao recurso do S3.


AULA 5

- Conexão com o django e aws
    - instale as bibliotecas:
        pip install django-storages
        pip install boto3
    - depois atualize o requirements.txt
        pip freeze > requirements.txt
-vamos acessar "setup > settings.py" e definir algumas configurações em formato de variáveis globais.
    AWS_ACCESS_KEY_ID = 'AKIA2ARL7LO5GURU3XPJ'

    AWS_SECRET_ACCESS_KEY = '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'
    
    AWS_STORAGE_BUCKET_NAME = 'projeto-fotografia-alura-space'
    
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    
    AWS_DEFAULT_ACL = 'public-read'
    
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400'
    }
    
    AWS_LOCATION = 'static'
    
    AWS_QUERYSTRING_AUTH = False
    
    AWS_HEADERS = {
        'Access-Control-Allow-Origin': '*',
    }
    
    AWS_S3_USE_SSL = False

- Ainda em "setup > settings.py" vamos definir algumas configurações para os meus métodos statics
    - acesse a documentação do django-storages
    - vá em Amazon s3
    - copie e cole no acima dos meus métodos static:
        DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
        STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'
    - altere a url de:
        STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
        MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
    - em INSTALLED_APPS precisa citar o 'storages',

- Vá em setup/urls.py e altere para:
    urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.galeria.urls')),
    path("", include("apps.usuarios.urls"))
    ]
    
    if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)

- vamos precisar retirar a primeira "/styles" e "/assets" de todos os redirecionamentos de static nos arquivos .html

- vamos coletar todos os arquivos statics e enviar para o nosso bucket
    python manage.py collectstatic
    yes
    
- vamos esconder nossas senhas e buckets da aws do arquivo settings.py
    -vamos criar um novo diretório "scripts" e um arquivo chamado secret_key_generator.py
        from django.core.management.utils import get_random_secret_key

        print(get_random_secret_key())
    - executando o terminal a partir deste arquivo e com comando python secret_key_generator.py é gerado uma nova key
    - vamos copiar as credencias da AWS para o nosso arquivo .env
    - vamos ajustar as credencias no arquivo setup/settings, deixando igual como ficou meu SECRET_KEY
        AWS_ACCESS_KEY_ID = str(os.getenv('AWS_ACCESS_KEY_ID'))

        AWS_SECRET_ACCESS_KEY = str(os.getenv('AWS_SECRET_ACCESS_KEY'))
        
        AWS_STORAGE_BUCKET_NAME = str(os.getenv('AWS_STORAGE_BUCKET_NAME'))
        
- python manage.py collectstatic deu 404 e retornei o projeto conforme estava na aula 3.
        

O que aprendemos nesta aula:

-Conectar com um usuário da IAM da AWS através das bibliotecas django-storages e boto3;
-Usar a biblioteca dotenv para evitar expor senhas e dados sensíveis.


"""
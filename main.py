"""
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
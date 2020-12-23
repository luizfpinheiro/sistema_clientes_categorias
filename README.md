### Pré-requisitos
- docker-compose (versão 3)
- python3.8
- virtualenv
- node >= 12

### Passo a passo com Docker Compose

1. Dentro da pasta principal do projeto, executar o comando `docker-compose up -d --build` para subir os containers. (Esse passo pode demorar um pouco, por conta do build das imagens)
    - Ao final do passo 1 é esperado que 3 containers estejam em execução (django_api, vue_ui e postgres_projeto_igd)

2. Identificar IP do container da API (django_api) 
    - Executar comando `docker inspect django_api` e procurar por "IPAddress".

3. Atualizar arquivo 'client/src/utils.js' com o ip recém identificado, que corresponda a API.

```
    const api = axios.create({
        baseURL: 'http://<ip_correto_do_container>:8000',
    });
```
4. Reiniciar containers, executando o comando `docker-compose restart`

5. Tudo ok. Acessar o projeto pelo endereço "http://localhost:8080".
    - http://localhost:8080/clientes (tela com a listagem de clientes)
    - http://localhost:8080/categorias (tela com listagem de categorias/tags)

### Passo a passo sem Docker Compose

1. Na pasta 'client', executar `npm install` ou `yarn install` para instalar dependencias do client.
2. Após instalado, executar server com `npm run serve` ou `yarn serve`.
3. Criar um ambiente virtual do python na pasta raíz do projeto com o comando `virtualenv venv --python=python3.8`
4. Após criado o ambiente virtual e ativado (`source venv/bin/activate` para ativar), instalar as dependencias com `pip install -r api/requirements.txt`
5. Após instaladas as dependências, executar o comando `python manage.py migrate` para criar a estrutur inicial do banco de dados.
6. Por fim, rodar o servidor da api com o comando `python manage.py runserver 0.0.0.0:8000`.
7. Tudo ok. Acessar o projeto pelo endereço "http://localhost:8080".
    - http://localhost:8080/clientes (tela com a listagem de clientes)
    - http://localhost:8080/categorias (tela com listagem de categorias/tags)

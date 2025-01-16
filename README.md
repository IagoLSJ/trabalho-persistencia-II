# Trabalho de Persistência II

Este projeto foi desenvolvido como parte da cadeira de Persistência II. Ele utiliza Python/FastApi, postgres e Docker para a criação de um ambiente de desenvolvimento padronizado. O gerenciamento de dependências é feito com o `pipenv`.

## Requisitos

Certifique-se de ter os seguintes softwares instalados em seu ambiente:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Pipenv](https://pipenv.pypa.io/en/latest/)

## Configuração do Ambiente

### Passo 1: Clonar o Repositório

Clone este repositório em sua máquina local:

```bash
git clone https://github.com/IagoLSJ/trabalho-persistencia-II.git
cd trabalho-persistencia-II
```

### Passo 2: Configurar o Ambiente Virtual

Use o `pipenv` para instalar as dependências do projeto:

```bash
pipenv install
```

Para ativar o ambiente virtual, execute:

```bash
pipenv shell
```

### Passo 3: Configurar o Docker

Certifique-se de que o Docker esteja em execução e inicie os serviços com o comando:

```bash
docker-compose up
```

Este comando irá configurar os serviços definidos no arquivo `docker-compose.yml`.

## Estrutura do Projeto

Abaixo está uma visão geral dos principais arquivos e diretórios do projeto:

```
.
├── src/                   # Código-fonte principal
├── Pipfile               # Dependências do projeto
├── Pipfile.lock          # Versões bloqueadas das dependências
├── docker-compose.yml    # Configuração de serviços Docker
├── .gitignore            # Arquivos ignorados pelo Git
```

## Como Executar

1. Certifique-se de que o ambiente virtual está ativado:

    ```bash
    pipenv shell
    ```

2. Inicie os serviços com o Docker:

    ```bash
    docker-compose up
    ```

3. Acesse a aplicação conforme instruído no código ou na saída do terminal. Caso a aplicação tenha uma interface web, você poderá acessá-la em `http://localhost` (ou outra porta configurada no `docker-compose.yml`).

## Licença

Este projeto está sob a licença [MIT](LICENSE). Sinta-se à vontade para usá-lo e modificá-lo como desejar.

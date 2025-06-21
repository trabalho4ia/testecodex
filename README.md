# Sistema de Cadastro de Pessoas

Este projeto apresenta um exemplo simples de cadastro de pessoas utilizando **PHP**, **MySQL** e uma interface em **React** estilizada com **TailwindCSS** e **daisyUI**.

## Estrutura

- `backend/` - API em PHP que se comunica com o banco MySQL.
- `frontend/` - Aplicação React carregada via CDN.
- `backend/schema.sql` - Script de criação da tabela `persons`.

## Configuração

1. Crie um banco MySQL chamado `testdb` e execute o script `backend/schema.sql`.
2. Ajuste as credenciais de acesso em `backend/config.php` (padrão: host `127.0.0.1`, usuário `root`, senha `leo123`).
3. Hospede os arquivos PHP em um servidor compatível (por exemplo Apache ou Nginx).
4. Abra `frontend/index.html` em um servidor web apontando para a pasta `frontend/`.

A interface permite cadastrar novas pessoas e listar os registros existentes.

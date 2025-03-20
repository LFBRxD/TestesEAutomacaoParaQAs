#bin/bash

# Script para inicializar o ambiente de desenvolvimento
cd ..
# O script deve ser executado na pasta raiz do projeto
# O script deve ser executado com permissão de execução
# chmod +x scripts_inicializacao/start_env.sh

# remove os containers e volumes existentes
docker-compose down -v
# remove as imagens existentes
docker rmi $(docker images -q)
# cria as imagens e inicia os containers do ambiente
docker-compose build --no-cache
# inicia os containers do ambiente criados 
docker-compose up

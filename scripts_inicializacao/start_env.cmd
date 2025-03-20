@echo off
echo "Iniciando ambiente de desenvolvimento..."
cd ..
docker-compose down
echo "Removendo volumes..."
docker volume prune -f 
echo "Construindo imagens..."
docker-compose build --no-cache
echo "Iniciando containers... (pode demorar alguns minutos)"
docker-compose up -d

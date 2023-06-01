docker-compose up -d
docker network inspect inquisitor_net | grep -e IPv4 -e Name -e Mac > src/network.txt

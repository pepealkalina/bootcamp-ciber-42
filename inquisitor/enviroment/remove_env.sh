docker rm -f client server attacker
docker rmi -f inquisitor.atk jlesage/filezilla:v1.35.3 panubo/vsftpd:v1.0.0
rm -rf src/network.txt
echo "\033[31mREMOVE NETWORK.TXT\033[0m"
echo "\033[32m---- REMOVED ENVIROMENT ----\033[0m"

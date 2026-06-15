# Cloud Computing

## Laptop A / Gateway

### 1. Setup MinIO
`mkdir -p ./CC_UAS/laptop-a-gateway/minio-data`
# edit docker-compose.yml + dnsmasq.conf (manual)

### 2. Restart gateway services
`cd ./CC_UAS/laptop-a-gateway
docker compose up -d`

### 3. Setup Functions Framework
`python3 -m venv ./gcp-functions
source ./gcp-functions/bin/activate
pip install functions-framework`
### create main.py

### Perintah jalanin Functions Framework
`functions-framework --target=minio_webhook --port=8080`

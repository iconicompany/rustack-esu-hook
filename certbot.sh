DOMAIN=$1
certbot certonly \
  --server https://acme-v02.api.letsencrypt.org/directory \
  --preferred-challenges dns \
  --email certbot@${DOMAIN} \
  --manual \
  --manual-auth-hook /etc/letsencrypt/rustack-esu-hook/auth.py \
  --manual-public-ip-logging-ok \
  --domain ${DOMAIN} \
  --domain "*.${DOMAIN}"


#  --manual-cleanup-hook /etc/letsencrypt/rustack-esu-hook/cleanup.py \

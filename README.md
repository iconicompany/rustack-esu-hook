# rustack-esu-hook
Rustask ESU Acme Hook

RUN certbot:
sudo env ESU_API_TOKEN=.... ESU_API_URL=https://lk.makecloud.ru ./certbot.sh example.com

TEST auth.py:
ESU_API_TOKEN=... ESU_API_URL=https://lk.makecloud.ru CERTBOT_DOMAIN=example.com CERTBOT_VALIDATION=test2 ./auth.py

TODO: cleanup

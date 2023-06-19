# Line Notification Gateway #

Line Notification Gateway for Alertmanager (Promtheus).

This program runs as a web server between Alertmanager and Line by helping to parse the format of JSON to string.

# How to set up Line Notify
- Login to the website https://notify-bot.line.me/th/ with **Line Account**.
- Go to **My Page** then click **Generate token**.
- Insert Token name as you want. (For this project use **AlertManager**)
- Select the group you want to use Line Notify or use 1-on-1 if for yourself.
- Click **Generate token**.
- Copy your token in the safe place.


# Install with Docker
Using docker to run the program
## Prerequisite
- Docker

Run commands below to clone source code that need to have to run program with docker compose.

```bash
git clone <link>
cd line-notify-gateway
docker compose up -d
```

# Install Manually
This is how to run this program manually without using docker.

## Prerequisite
- python3

Run commands below to install tools that need to have to run the program.
```bash
git clone <link>
cd line-notify-gateway
pip install -r requirements.txt
python app.py
```

# AlertManager #

Set receiver of generic webhook from Alertmanager.

```yaml
receivers:
  - name: 'line'
    webhook_configs:
      - url: 'http://localhost:5000/webhook'
        http_config:
          bearer_token: '« YOUR_LINE_API_TOKEN »'
```

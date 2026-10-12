# Python IP Toolkit

[راهنمای فارسی](README_FA.md)

Two small Python tools adapted from earlier IP list and Telegram bot experiments: a CLI that formats validated IP addresses, and a Telegram bot that classifies IPv4/IPv6 addresses locally. The bot does **not** perform geolocation or contact an IP lookup service.

## CLI

```bash
python format_ips.py examples/ips.txt --template "https://example.test/host/{ip}"
```

The input is one address per line. Blank lines and `#` comments are ignored. Invalid addresses produce a line-numbered error. The included addresses are reserved for documentation.

## Telegram bot

Create a fresh Telegram bot token, set `BOT_TOKEN` in the environment, and run:

```bash
pip install -r requirements.txt
python bot.py
```

The original local bot contained a token and returned a static response from an HTTP endpoint. That code and all original IP lists are excluded here. This version uses only Python's `ipaddress` module for classification. MIT licensed.

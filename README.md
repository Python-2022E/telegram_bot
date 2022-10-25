# Telegram Bot API

## Introduction

Bots are third-party applications that run inside Telegram. Users can interact with bots by sending them messages, commands and inline requests. You control your bots using HTTPS requests to Telegram's Bot API.

## Methods

- [getMe](https://core.telegram.org/bots/api#getme) — Get the bot info
- [getUpdates](https://core.telegram.org/bots/api#getupdates) — Get updates
- [sendMessage](https://core.telegram.org/bots/api#sendmessage) — Send a message
- [sendPhoto](https://core.telegram.org/bots/api#sendphoto) — Send a photo
- [sendAudio](https://core.telegram.org/bots/api#sendaudio) — Send an audio
- [sendDocument](https://core.telegram.org/bots/api#senddocument) — Send a document
- [sendSticker](https://core.telegram.org/bots/api#sendsticker) — Send a sticker
- [sendVideo](https://core.telegram.org/bots/api#sendvideo) — Send a video
- [sendLocation](https://core.telegram.org/bots/api#sendlocation) — Send a location
- [sendContact](https://core.telegram.org/bots/api#sendcontact) — Send a contact

- [setWebhook](https://core.telegram.org/bots/api#setwebhook) — Set webhook
- [getWebhookInfo](https://core.telegram.org/bots/api#getwebhookinfo) — Get webhook info
- [deleteWebhook](https://core.telegram.org/bots/api#deletewebhook) — Delete webhook

## Types

- [User](https://core.telegram.org/bots/api#user) — User object
- [update](https://core.telegram.org/bots/api#update) — Update object
- [Message](https://core.telegram.org/bots/api#message) — Message object
- [Chat](https://core.telegram.org/bots/api#chat) — Chat object
- [PhotoSize](https://core.telegram.org/bots/api#photosize) — PhotoSize object

## Examples

```python
import telegram
bot = telegram.Bot(token='TOKEN')
bot.getMe()
```
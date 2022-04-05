# piazza-bot

This is a simple Discord bot which responds to messages that mention Piazza questions (for instance `p38` to refer to question @38) with a link to the question and a preview of the content.

Originally written @glapa-grossklag, now maintained (only the minimum amount necessary :3) by me.

## Setup

First, move `example-config.py` to `config.py` and fill in the Discord bot token and the Piazza network ID (the part after `https://piazza.com/class/` in a URL).

Then, to install dependencies, run the following (with [Poetry](https://python-poetry.org/) installed):

```sh
$ poetry install
```

## Usage

```sh
$ poetry run python main.py
```

By default, this will prompt you for your Piazza email address and password. If you don't want to log in every time, set `email` and `password` in your configuration file.

## Docker

The example [`docker-compose.yml`](./docker-compose.yml) will build and run this bot in a Docker container. Edit it as needed; just make sure that your configuration is at `/app/config.py` in the container.

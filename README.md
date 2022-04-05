# piazza-bot

This is a simple Discord bot which responds to messages that mention Piazza questions (for instance `p38` to refer to question @38) with a link to the question and a preview of the content.

Originally written @glapa-grossklag, now maintained (only the minimum amount necessary) by me.

## Setup

First, move `example-config.py` to `config.py` and fill in the Discord bot token and the Piazza network ID.

Then, to install dependencies, run the following (with [Poetry](https://python-poetry.org/) installed):

```sh
$ poetry install
```

## Usage

```sh
$ poetry run python main.py
```

This will prompt you for your Piazza email address and password.

FROM python:3.10
RUN pip install poetry
WORKDIR /app
COPY pyproject.toml .
COPY poetry.lock .
COPY poetry.toml .
COPY main.py .
RUN poetry install
ENTRYPOINT ["poetry", "run", "python", "main.py"]

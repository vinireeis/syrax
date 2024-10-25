FROM python:3.12

RUN pip install poetry

WORKDIR ./

COPY pyproject.toml poetry.lock ./

RUN poetry install

COPY . .

CMD ["poetry", "run", "uvicorn", "python3", "main.py", "--host", "0.0.0.0", "--port", "8000"]

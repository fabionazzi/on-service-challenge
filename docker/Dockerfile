# ==================== DEV ===================
FROM python:3.12-slim AS dev

RUN pip3 install poetry==2.1.3
COPY pyproject.toml poetry.lock .
RUN poetry config virtualenvs.in-project true

WORKDIR /app
COPY ./app/ /app/

RUN poetry install --without test

CMD ["poetry", "run", "uvicorn", "src.on_service.main:app", "--reload", "--host", "0.0.0.0", "--port", "9090"]

# =================== TEST ===================
FROM dev AS test

RUN poetry install --only test
CMD ["pytest", "/app/tests/"]

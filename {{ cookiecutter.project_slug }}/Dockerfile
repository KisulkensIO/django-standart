FROM python:3.12-alpine as build

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=on \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

WORKDIR /code
COPY pyproject.toml poetry.lock /code/
RUN pip install poetry
RUN poetry export --only main --output=requirements.txt
RUN pip install -r requirements.txt

FROM python:3.12-alpine

WORKDIR /code

RUN apk add gettext postgresql-client

COPY --from=build /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/
COPY --from=build /usr/local/bin/ /usr/local/bin/

COPY . /code
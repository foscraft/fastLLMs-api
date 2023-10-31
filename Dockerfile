FROM python:3.10

RUN apt-get update

# Set working directory for the Python project
WORKDIR /app/python

# Install Python dependencies and other build dependencies
RUN apt-get update && \
    apt-get install -y \
        ca-certificates \
        gcc \
        libffi-dev \
        libpq-dev && \
    pip3 install --upgrade pip poetry

COPY . .

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes && \
    pip3 install --no-cache-dir -r requirements.txt

RUN pip install gpt4all

RUN pip install uvicorn

CMD ["uviicorn", "main:app"]

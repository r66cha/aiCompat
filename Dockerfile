FROM python:3.12.11

WORKDIR /aiCompat

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN ["python", "main.py"]
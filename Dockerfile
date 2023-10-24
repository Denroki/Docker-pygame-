FROM python:3

WORKDIR .

COPY main.py .

RUN pip install --no-cache-dir -r requirements.txt

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

COPY . .

CMD [ "python", "main.py"]
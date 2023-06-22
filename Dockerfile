FROM python:3.9.16

WORKDIR /home/app

COPY . .

RUN pip install -r requirements.backup.txt

EXPOSE 5000

CMD ["python", "main.py"]

FROM python:3.10

WORKDIR /usr/src/app

COPY web/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "python", "web/manage.py", "runserver" ]

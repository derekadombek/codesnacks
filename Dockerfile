FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
COPY requirements.txt /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 5000
ENTRYPOINT python /app/src/app.py

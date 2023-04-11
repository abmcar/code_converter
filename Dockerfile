FROM python:3.9
LABEL authors="abmcar"
WORKDIR /app
COPY . /app
ENV OPENAI_URL="https://api.openai.com/v1"
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "app.py"]
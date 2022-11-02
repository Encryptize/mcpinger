FROM python:3.10-alpine

RUN apk add --no-cache curl

WORKDIR /app
ADD requirements.txt .
RUN pip install -r requirements.txt

ADD . ./
ENTRYPOINT [ "uvicorn", "main:app" ]

CMD ["--host", "0.0.0.0"]
HEALTHCHECK --interval=30s --timeout=5s --retries=3 CMD curl --silent --fail http://localhost:8000/healthcheck || exit 1
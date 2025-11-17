FROM python:3

WORKDIR /app

RUN pip install mcp litellm google-adk python-dotenv

COPY agent /app/agent
COPY script.sh /app/script.sh

RUN chmod +x /app/script.sh

EXPOSE 8000

ENTRYPOINT [ "/app/script.sh" ]
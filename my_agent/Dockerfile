FROM python:3

WORKDIR /app

RUN pip install mcp litellm google-adk python-dotenv

COPY agent /app/agent
COPY script.sh /app/script.sh

RUN chmod +x /app/script.sh

EXPOSE 8000

ENV OLLAMA_API_BASE=http://ollama:11434
ENV URL_MCP=http://mcp_server:8100/mcp

ENTRYPOINT [ "/app/script.sh" ]
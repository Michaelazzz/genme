FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y texlive texlive-latex-extra perl make && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["main.tex"]
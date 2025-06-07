FROM python:3.10-slim

# Install dependencies
RUN apt-get update && \
    apt-get install -y texlive texlive-latex-base texlive-latex-recommended perl && \
    apt-get clean

WORKDIR /app
COPY . .

# Make sure entrypoint is executable
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]

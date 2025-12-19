# Use Python 3.10 slim image for a smaller footprint
FROM python:3.10-slim

# Install system dependencies
# curl: needed for installing Ollama and health checks
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Install uv from the official image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies using uv (Faster & More Reliable)
# --system: Install into the system python environment (no venv needed in Docker)
RUN uv pip install --system --no-cache -r requirements.txt

# Install Ollama CLI
# This script usually installs to /usr/bin/ollama or /usr/local/bin/ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Copy application code
COPY . .

# Make entrypoint executable
RUN chmod +x entrypoint.sh

# Expose port
EXPOSE 8000

# Set entrypoint
ENTRYPOINT ["./entrypoint.sh"]

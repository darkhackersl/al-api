FROM python:3.11-slim

# Install dependencies
RUN apt-get update && apt-get install -y wget gnupg curl ca-certificates fonts-liberation libnss3 libatk-bridge2.0-0 libxss1 libasound2 libgbm1 libgtk-3-0 libxshmfence1 libxrandr2 libxdamage1 libpango-1.0-0 libatk1.0-0 libatspi2.0-0 libdrm2 libxcomposite1 libcups2

# Install Python packages
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Install Playwright and browsers
RUN playwright install --with-deps

COPY . .

CMD ["python", "app.py"]

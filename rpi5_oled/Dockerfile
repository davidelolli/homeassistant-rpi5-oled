FROM alpine:3.19

# Install dependencies needed for smbus-cffi compilation
RUN apk add --no-cache \
    python3 \
    py3-pip \
    i2c-tools \
    py3-psutil \
    gcc \
    musl-dev \
    python3-dev \
    linux-headers

# Install Python libraries
RUN pip3 install --break-system-packages --no-cache-dir smbus-cffi

# Setup working directory
WORKDIR /app

# Copy scripts
COPY rpi5-oled.py .
COPY shutdown.py .

# Fix permissions just in case
RUN chmod +x rpi5-oled.py shutdown.py

# Run the main script directly
CMD ["python3", "rpi5-oled.py"]

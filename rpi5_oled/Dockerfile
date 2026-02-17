FROM alpine:3.19

# Install system dependencies
RUN apk add --no-cache \
    python3 \
    py3-pip \
    i2c-tools \
    py3-psutil

# Install pure Python libraries (no compilation needed!)
RUN pip3 install --break-system-packages --no-cache-dir smbus2

# Setup app
WORKDIR /app
COPY rpi5-oled.py .
COPY shutdown.py .

# Fix permissions
RUN chmod +x rpi5-oled.py shutdown.py

# Run script
CMD ["python3", "rpi5-oled.py"]

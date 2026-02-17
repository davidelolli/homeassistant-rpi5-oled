ARG BUILD_FROM
FROM $BUILD_FROM

# Install Python and required packages
RUN apk add --no-cache python3 py3-pip i2c-tools

# Install Python packages
RUN pip3 install --no-cache-dir psutil smbus-cffi

# Copy scripts
COPY rpi5-oled.py /usr/local/bin/
COPY shutdown.py /usr/local/bin/
COPY run.sh /
RUN chmod a+x /run.sh /usr/local/bin/rpi5-oled.py /usr/local/bin/shutdown.py

CMD [ "/run.sh" ]
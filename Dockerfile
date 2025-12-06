FROM odoo:18

# Install extra python packages
RUN pip3 install --no-cache-dir --break-system-packages PyJWT
RUN pip3 install --no-cache-dir --break-system-packages cryptography
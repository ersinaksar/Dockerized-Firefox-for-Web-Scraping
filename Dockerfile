FROM --platform=linux/amd64 python:3.9-slim-buster

# Install Firefox and other dependencies
RUN apt-get update && apt-get install -y firefox-esr xvfb

# Install Python packages
RUN pip install selenium


# Install xvfb and xauth packages
RUN apt-get install -y xvfb xauth

# Copy Python script
COPY main.py .

ENV DISPLAY=:99

# Run script with xvfb
CMD ["xvfb-run", "--server-args='-screen 0 1024x768x24'", "--auto-servernum", "python", "main.py"]

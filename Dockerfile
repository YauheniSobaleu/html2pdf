FROM python:3.7-slim-buster
ENV PYTHONUNBUFFERED 1

ARG WKHTMLTOPDF_FILENAME=wkhtmltox_0.12.5-1.buster_amd64.deb
ARG WKHTMLTOPDF_URL=https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/${WKHTMLTOPDF_FILENAME}

RUN apt update && \
    apt install -y --no-install-recommends wget && \
    wget ${WKHTMLTOPDF_URL} && \
    apt install -y --no-install-recommends ./${WKHTMLTOPDF_FILENAME} && \
    apt remove -y --auto-remove wget && \
    rm ${WKHTMLTOPDF_FILENAME}

# Allows docker to cache installed dependencies between builds
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Adds our application code to the image
COPY . code
WORKDIR /code

EXPOSE 8000

# Run the production server
CMD newrelic-admin run-program gunicorn --bind 0.0.0.0:$PORT --access-logfile - html2pdf.wsgi:application

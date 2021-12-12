FROM python:3.6.9

WORKDIR /app
COPY import_external.py /app/
COPY import_internal.py /app/

ENV PYTHONPATH /app/utils
ENV PATH=$PATH:/app/utils

CMD python import_external.py ; python import_internal.py

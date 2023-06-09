FROM python:3.10-slim

LABEL org.opencontainers.image.title="Zero Systems Data aggregation interview task - API"

WORKDIR /app/

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# COPY src/ /app/
# RUN mkdir -p 
COPY /mapper/ /app/mapper
# COPY api.py /app/
# COPY engine.py /app/


# COPY config.yml /app/

EXPOSE 8080

CMD ["gunicorn", "-b", "0.0.0.0:8080", "--timeout", "0", "mapper:app"]
FROM python:3.9-slim

WORKDIR /app

COPY GPS&TAGGING/Geo-Tagging/Generating-KML.py .

RUN pip install pykml lxml

CMD ["python", "Generating-KML.py"] 
FROM python:latest
COPY . .
RUN python3 -m pip install flask
EXPOSE 8080
CMD ["python", "-u", "index.py"]
FROM python:3.4-alpine
ADD . ./
WORKDIR /home/mrobot
RUN pip install --upgrade pip && pip install -r requirements.txt
CMD ["python", "-u", "app.py"]
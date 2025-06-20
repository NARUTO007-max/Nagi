FROM python:3.11

WORKDIR /root/waifu

COPY . .

RUN pip3 install --upgrade pip setuptools
RUN pip3 install -U -r requirements.txt

CMD ["python3", "-m", "waifu"]


FROM python:3.9

WORKDIR /trading_app

COPY ./requirements.txt /trading_app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /trading_app/requirements.txt

#
COPY ./main.py /trading_app/

#
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
FROM python:3.10

RUN mkdir -p /workspace/
WORKDIR /workspace/
COPY requirements.txt /workspace/
RUN apt-get update
ENV TZ=Europe/Rome
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN pip install --no-cache-dir --upgrade -r requirements.txt
ENTRYPOINT ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]

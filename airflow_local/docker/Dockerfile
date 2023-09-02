FROM apache/airflow:2.7.0

#RUN sudo apt-get install libpq-dev

COPY requirements.txt /

RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" -r /requirements.txt

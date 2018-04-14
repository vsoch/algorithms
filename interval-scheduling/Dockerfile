FROM continuumio/miniconda3

# docker build -t vanessa/algorithms:interview-scheduling .

RUN mkdir /code
ADD . /code
ENV PATH /opt/conda/bin:$PATH
ENTRYPOINT ["python", "/code/main.py"]

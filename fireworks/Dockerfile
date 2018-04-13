FROM continuumio/miniconda3

# docker build -t vanessa/algorithms:fireworks .
# docker run -it vanessa/algorithms:fireworks

RUN mkdir /code
ADD . /code
ENV PATH /opt/conda/bin:$PATH
ENTRYPOINT ["python", "/code/main.py"]

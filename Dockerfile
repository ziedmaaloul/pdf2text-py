FROM python:3.7

WORKDIR /input

COPY . /input/
RUN apt update
RUN apt install -yq build-essential 
RUN apt install -yq libpoppler-cpp-dev 
RUN apt install -yq pkg-config 
RUN pip install --upgrade pip && \
    pip install requests && \
    python -m pip install requests && \
    pip install pdftotext && \
    mkdir /output
RUN chmod +x script.sh
CMD /bin/bash
RUN apt update && apt install -yq ffmpeg
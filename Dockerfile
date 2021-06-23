FROM python:3.7
WORKDIR /input
COPY . /input/
RUN apt update
RUN pip install --upgrade pip && \
    pip install requests && \
    python -m pip install requests && \
    pip install pdfplumber && \
    mkdir /output
RUN chmod +x script.sh
CMD /bin/bash
RUN apt update
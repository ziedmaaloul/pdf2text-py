## Convert PDF File to Text using Python

To Run With Docker

[Docker Image](https://hub.docker.com/r/maaloulmz/pdf2text)


Build Docker Image
```sh
docker build -t maaloulmz/pdf2text -f Dockerfile .
```

Run Container and extract result
```sh
docker run -it --rm -v /path/to/pdf2text-py/folder:/output/folder -v /path/to/pdf2text-py/orig/220.pdf:/input/220.pdf maaloulmz/pdf2text sh /input/script.sh /input/220.pdf /output/folder
```

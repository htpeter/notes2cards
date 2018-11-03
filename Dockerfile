FROM ubuntu:16.04

# Needed to prevent UnicodeDecodeError: 'ascii' codec can't decode byte
# when installing fairseq.
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
# ENV LANG C.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN apt-get update \
    && apt-get install -y software-properties-common curl \
    && add-apt-repository ppa:jonathonf/python-3.6 \
    && apt-get remove -y software-properties-common \
    && apt autoremove -y \
    && apt-get update \
    && apt-get install -y python3.6 \
    && curl -o /tmp/get-pip.py "https://bootstrap.pypa.io/get-pip.py" \
    && python3.6 /tmp/get-pip.py \
    && apt-get remove -y curl \
    && apt autoremove -y \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get -y update && apt-get install -y python3.6-dev
RUN apt-get -y install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
RUN apt-get -y install ffmpeg libav-tools


ADD . /code
WORKDIR /code
VOLUME .:/code

RUN pip install -r requirements.txt
CMD ["python3.6", "notes2cards.py", \
        "--inputFile", "./test/test_file.md", \
        "--deckName", "Docker_Deck",  \
        "--outputFile", "docker_deck.apkg"]

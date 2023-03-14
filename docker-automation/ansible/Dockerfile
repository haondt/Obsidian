FROM rundeck/rundeck:4.11.0

USER root
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get -y update && \
    apt-get -y install \
	python3-pip \
	sudo \
	wget \
	curl \
	sshpass 
RUN apt-get clean

RUN pip install --upgrade pip
RUN pip install ansible-core

RUN ln -s /home/rundeck /var/lib/rundeck

USER rundeck


FROM biothings:0.9.0

ARG APP_GIT=https://github.com/biothings/biothings_studio.git
ARG APP_TAG=master
ARG APP_NAME=biothings-standalone-hub
ENV SRC_URI=mongodb://mongodb:27017
ENV SRC_DB=biothings_src
ENV TARGET_URI=mongodb://mongodb:27017
ENV TARGET_DB=biothings_target
ENV HUB_URI=mongodb://mongodb:27017
ENV HUB_DB=biothings_hub

RUN mkdir -p /home/biothings/${APP_NAME}
WORKDIR /home/biothings/${APP_NAME}
RUN git clone ${APP_GIT} . && git checkout ${APP_TAG}
RUN find . -maxdepth 1 -name 'requirements*.txt' -exec pip install -r {} \;
RUN rm -f src/bin/ssh_host_key{,.pub}
RUN ln -sv /data/biothings/ssh_host_key src/bin/ssh_host_key
RUN ln -sv /data/biothings/ssh_host_key.pub src/bin/ssh_host_key.pub

# create dirs
USER root
RUN mkdir /data
RUN ["/bin/bash", "-c", "mkdir -p /data/biothings/${APP_NAME}/{datasources,plugins,dataupload,diff,logs,release,cache,run}"]
# fix permissions
RUN chown -R biothings:biothings /data/biothings

# export persistent data
VOLUME [ "/data" ]

ADD docker-entrypoint.sh /
RUN sed -i s/APP_NAME/${APP_NAME}/g /docker-entrypoint.sh


USER biothings
WORKDIR /home/biothings/${APP_NAME}/src
ENV PYTHONPATH=.

ADD config.py .
RUN sed -i s/API_NAME/${APP_NAME}/g config.py

# will fix later
# It is better to send a interrupt than a sigkill
# given that implementing SIGTERM handler takes more time
STOPSIGNAL SIGINT

EXPOSE 7080/tcp
EXPOSE 7022/tcp

CMD ["/docker-entrypoint.sh"]

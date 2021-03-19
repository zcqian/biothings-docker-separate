ARG BIOTHINGS_VERSION

FROM biothings:${BIOTHINGS_VERSION}

ARG APP_GIT=https://github.com/biothings/biothings_studio.git
ARG APP_TAG=master
ARG API_NAME=biothings-hub
ENV SRC_URI=mongodb://mongodb:27017
ENV SRC_DB=biothings_src
ENV TARGET_URI=mongodb://mongodb:27017
ENV TARGET_DB=biothings_target
ENV HUB_URI=mongodb://mongodb:27017
ENV HUB_DB=biothings_hub
ARG TINI_VERSION=v0.19.0




RUN mkdir -p /home/biothings/api
WORKDIR /home/biothings/api
RUN git clone ${APP_GIT} . && git checkout ${APP_TAG}
RUN find . -maxdepth 1 -name 'requirements*.txt' -exec pip install -r {} \;
# Remove existing ssh keys
RUN rm -f src/bin/ssh_host_key \
    && rm -f src/bin/ssh_host_key.pub \
    && ln -sv /data/biothings/ssh_host_key src/bin/ssh_host_key \
    && ln -sv /data/biothings/ssh_host_key.pub src/bin/ssh_host_key.pub

# create dirs
USER root
ADD docker-entrypoint.sh /

RUN mkdir /data
RUN ["/bin/bash", "-c", "mkdir -p /data/biothings/${API_NAME}/{datasources,plugins,dataupload,diff,logs,release,cache,run,esbackup}"]
# fix permissions
RUN chown -R biothings:biothings /data/biothings

# export persistent data
VOLUME [ "/data" ]


USER biothings
WORKDIR /home/biothings/api/src
ENV PYTHONPATH=.

ADD config.py .
RUN sed -i s/__REPLACE_WITH_API_NAME/${API_NAME}/g config.py

# will fix later
# It is better to send a interrupt than a sigkill
# given that implementing SIGTERM handler takes more time
STOPSIGNAL SIGINT

EXPOSE 7080/tcp
EXPOSE 7022/tcp

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["/home/biothings/venv/bin/python", "/home/biothings/api/src/bin/hub.py"]


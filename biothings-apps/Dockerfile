FROM python:3.6

RUN mkdir /data
RUN useradd --user-group -m -d /data/biothings -s /bin/bash biothings

ARG BIOTHINGS_GIT=https://github.com/biothings/biothings.api.git
ARG BIOTHINGS_TAG=master

ARG APP_GIT=https://github.com/biothings/biothings_studio.git
ARG APP_TAG=master
ARG APP_NAME=biothings-standalone-hub
# trying to set this from inside the image is very difficult
WORKDIR /data/biothings/${APP_NAME}
ENV SRC_URI=mongodb://mongodb:27017
ENV SRC_DB=biothings_src
ENV TARGET_URI=mongodb://mongodb:27017
ENV TARGET_DB=biothings_target
ENV HUB_URI=mongodb://mongodb:27017
ENV HUB_DB=biothings_hub
RUN git clone ${APP_GIT} . && git checkout ${APP_TAG}
RUN python3 -m venv venv
ENV VIRTUAL_ENV=/data/biothings/${APP_NAME}/venv
ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"
ENV PYTHONPATH=/data/biothings/${APP_NAME}/src
# Some dependency of our dependencies (or even deeper dependencies)
#  dedided that they need rustc to build, just this Sunday.
# RUN pip install "cryptography<3.4.0"
 
RUN CRYPTOGRAPHY_DONT_BUILD_RUST=1 pip install -e "git+${BIOTHINGS_GIT}@${BIOTHINGS_TAG}#egg=biothings[hub]"
RUN find . -maxdepth 1 -name 'requirements*.txt' -exec pip install -r {} \;

# create dirs
RUN ["/bin/bash", "-c", "mkdir -p /data/biothings/${APP_NAME}/{datasources,plugins,dataupload,diff,logs,release,cache,run}"]

# fix permissions
RUN chown -R biothings:biothings /data/biothings

WORKDIR /data/biothings/${APP_NAME}/src

# export persistent data
VOLUME [ "/data" ]

COPY docker-entrypoint.sh /
RUN sed -i s/APP_NAME/${APP_NAME}/g /docker-entrypoint.sh

USER biothings

STOPSIGNAL SIGINT
# will fix later
EXPOSE 7080/tcp
EXPOSE 7022/tcp

CMD ["/docker-entrypoint.sh"]

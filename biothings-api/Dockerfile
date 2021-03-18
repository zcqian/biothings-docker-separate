ARG PYTHON_VERSION=3.6
# FIXME: as I was saying ... 3.7 doesn't break my stuff
#  but it breaks dependencies like asyncssh now that async is a reserved keyword

FROM python:${PYTHON_VERSION}

# FIXME: use external pip and cache (for build speed and smaller container)

# UID and GID chosen arbitrarily -- it is better to choose a specific GID/UID
# but I have no idea how this won't collide with other things
ARG BIOTHINGS_UID=454
ARG BIOTHINGS_GID=454

# this argument is only used when installing from git
ARG BIOTHINGS_GIT=https://github.com/biothings/biothings.api.git
# VERSION can be a version from PyPI or a git tag/revision/branch
ARG BIOTHINGS_VERSION=master
ARG BIOTHINGS_EXTRA_REQUIRES=hub,web_extra

# create biothings user, run as the user 
RUN groupadd -g ${BIOTHINGS_GID} -r biothings \
    && useradd -g biothings -r -m -d /home/biothings -s /bin/bash \
    -u ${BIOTHINGS_UID} biothings
USER biothings
WORKDIR /home/biothings

# init. virtualenv
RUN python3 -m venv venv
# activate
ENV VIRTUAL_ENV=/home/biothings/venv
ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"
# update pip
RUN pip install --upgrade pip
# install cryptography, 1) we need this to generate SSH keys 2) install w/o Rust
RUN CRYPTOGRAPHY_DONT_BUILD_RUST=1 pip install cryptography
# if we can't find the version from pypi then try git
RUN pip install biothings[${BIOTHINGS_EXTRA_REQUIRES}]==${BIOTHINGS_VERSION} \
    || pip install "git+${BIOTHINGS_GIT}@${BIOTHINGS_VERSION}#egg=biothings[${BIOTHINGS_EXTRA_REQUIRES}]"

CMD [ "/home/biothings/venv/bin/python" ]

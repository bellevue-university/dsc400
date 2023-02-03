ARG BASE_CONTAINER=jupyter/pyspark-notebook
FROM $BASE_CONTAINER

LABEL maintainer="Shawn Hermans <shermasn@bellevue.edu>"

# Fix: https://github.com/hadolint/hadolint/wiki/DL4006
# Fix: https://github.com/koalaman/shellcheck/wiki/SC3014
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root

# Install netcat and graphviz
RUN apt-get update --yes && \
    apt-get install --yes --no-install-recommends \
    netcat \
    graphviz && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

USER ${NB_UID}

# Install libraries with Mamba
RUN mamba install --quiet --yes \
    'networkx' \
    'tinydb' \
    'pydot' \
    'pillow' \
    'Jinja2' \
    'requests' \
    's3fs' \
    'kafka-python' \
    'matplotlib' \
    'pygal' \
    'plotly' \
    'tabulate' \
    'Faker' \
    'graphviz' && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

# Install non-Mamba libraries
RUN pip install --quiet --no-cache-dir \
    'devtools' \
    'cogdb' \
    'falcon' \
    'Pillow' && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

# Install Tensorflow
RUN pip install --quiet --no-cache-dir \
    'tensorflow' && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

## Install Keras
RUN pip install --quiet --no-cache-dir \
    'keras' && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

USER root

# Configure IPython system-wide
COPY ipython_kernel_config.py "/etc/ipython/"
RUN fix-permissions "/etc/ipython/"

USER $NB_UID
WORKDIR "${HOME}"
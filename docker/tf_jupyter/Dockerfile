FROM ubuntu:18.04

# Pick up some TF dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        libfreetype6-dev \
        libpng-dev \
        libzmq3-dev \
        pkg-config \
        python \
        python3 \
        python3-dev \
        python-pip \
        python3-pip \
        python3-setuptools \
        rsync \
        software-properties-common \
        unzip \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 --no-cache-dir install \
        cython \
        ipykernel \
        jupyter \
        matplotlib \
        numpy \
        scipy \
        sklearn \
        pandas \
        Pillow \
        nltk\
        imageio\
        future\
        keras\
        && \
    python3 -m ipykernel.kernelspec

RUN apt-get update
#RUN apt-get install python3.6-dev

RUN pip3 install -U wheel
RUN pip3 install tornado==5.1.1
RUN pip3 install ipywidgets
RUN jupyter nbextension enable --py widgetsnbextension

# --- DO NOT EDIT OR DELETE BETWEEN THE LINES --- #
# These lines will be edited automatically by parameterized_docker_build.sh. #
# COPY _PIP_FILE_ /
# RUN pip --no-cache-dir install /_PIP_FILE_
# RUN rm -f /_PIP_FILE_

# Install TensorFlow CPU version from central repo
RUN pip3 --no-cache-dir install --upgrade tensorflow
# --- ~ DO NOT EDIT OR DELETE BETWEEN THE LINES --- #

RUN pip3 install ipython jupyter jupyter-tensorboard --upgrade
RUN jupyter tensorboard enable --system
# RUN ln -s /usr/bin/python3 /usr/bin/python#

# Install OpenJDK-8
RUN apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    apt-get install -y ant && \
    apt-get clean;

# Fix certificate issues
RUN apt-get update && \
    apt-get install ca-certificates-java && \
    apt-get clean && \
    update-ca-certificates -f;

# Setup JAVA_HOME -- useful for docker commandline
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
RUN export JAVA_HOME

# Set up our notebook config.
COPY ./docker/tf_jupyter/jupyter_notebook_config.py /root/.jupyter/

# Copy sample notebooks.
COPY ./notebooks /notebooks

# Jupyter has issues with being run directly:
#   https://github.com/ipython/ipython/issues/7062
# We just add a little wrapper script.
COPY ./docker/tf_jupyter/run_jupyter.sh /

# TensorBoard
EXPOSE 6006
# IPython
EXPOSE 8888

WORKDIR "/notebooks"

RUN chmod +x /run_jupyter.sh

CMD ["sh", "/run_jupyter.sh", "--allow-root"]
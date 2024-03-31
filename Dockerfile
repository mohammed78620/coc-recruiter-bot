FROM python:3.11

ENV POETRY_VERSION=1.4.2
ENV POETRY_VIRTUALENVS_CREATE=false
ENV POETRY_CACHE_DIR='/var/cache/pypoetry'
  
RUN apt-get update
RUN apt-get upgrade -y

RUN curl https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-409.0.0-linux-x86_64.tar.gz > /tmp/google-cloud-cli.tar.gz
RUN mkdir -p /usr/local/gcloud && tar -xf /tmp/google-cloud-cli.tar.gz && ./google-cloud-sdk/install.sh --quiet

# create the app user
RUN adduser --system --group app

# Set the working directory inside the container
WORKDIR /app

# Copy the project and entrypoint script to the working directory
COPY . /app
# COPY start_bot.sh start_bot.sh


# Install dependencies
RUN pip install --upgrade pip
RUN pip install "poetry==$POETRY_VERSION" && poetry --version
RUN poetry config virtualenvs.create false
RUN poetry install $(test "$VAI_ENV" == production && echo "--no-dev") --no-interaction --no-ansi --no-root


# Run the bash script to execute the Python code
CMD ["sh", "/app/start_bot.sh"]
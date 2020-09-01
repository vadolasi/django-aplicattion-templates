FROM python:3.8

# Configure project dir
ENV PROJECT_DIR /code
WORKDIR ${PROJECT_DIR}
COPY . ${PROJECT_DIR}

# Install dependencies
RUN pip install pipenv
RUN pipenv install --system --deploy

FROM python:3.12-slim

# Define the working directory.
WORKDIR learner

# Flag that we're in a Docker container.
ENV DOCKERIZED Yes

# Install the Linux utilities.
RUN apt -y update
RUN apt -y upgrade
RUN apt -y install less
RUN apt -y install tree

# Install the Python packages.
RUN python3 -m pip install --upgrade pip
RUN pip3 install --user --upgrade pip
RUN pip3 install seaborn==0.13.2
RUN pip3 install matplotlib==3.9.2
RUN pip3 install numpy==2.0.1
RUN pip3 install pandas==2.2.2
RUN pip3 install scikit-learn==1.5.1
RUN pip3 install pytest==8.3.2
RUN pip3 install python-dotenv==1.0.1
RUN pip3 install fastapi==0.112.0
RUN pip3 install uvicorn==0.30.6
RUN pip3 install pydantic==2.8.2
RUN pip3 install requests==2.32.3
# Copy all the necessary files
COPY Dockerfile *.py *.yml *.txt *.sh *.toml README.* .pre-commit-config.yaml .env ./
COPY learner/ learner
COPY tests/ tests

# Sets up the entry point to invoke the trainer.
ENTRYPOINT ["python3", "main.py"]

# EXPOSE 8000
# CMD ["uvicorn", "server:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]

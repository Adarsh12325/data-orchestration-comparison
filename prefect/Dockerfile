FROM python:3.9-slim

WORKDIR /opt/project

COPY . /opt/project

# Install required packages
RUN pip install --no-cache-dir prefect pandas pyarrow

# Set environment variables to disable ephemeral API server and events
ENV PREFECT_API_URL=""
ENV PREFECT_EXPERIMENTAL_ENABLE_EVENTS=false
ENV PREFECT_LOGGING_LEVEL=INFO
ENV PYTHONPATH=/opt/project

# Set default command to run your flow
CMD ["python", "flow.py"]


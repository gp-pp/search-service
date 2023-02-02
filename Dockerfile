FROM node:alpine
USER root
WORKDIR /app

# Install dependencies for Node.js and Python
RUN apk add --no-cache nodejs python3 curl

# Copy Node.js and Python files into the container
COPY ./ ./

RUN chmod +x start.sh

# Start the Python script in the background
RUN cd /app/python_and_meilisearch && \
	apk add --no-cache py3-pip && \
	pip install -r requirements.txt

RUN cd /app/new_node && \
	npm install


EXPOSE 3003:3003

# Start the Node.js app in the foreground
CMD ["/bin/sh", "-c", "/app/start.sh"]


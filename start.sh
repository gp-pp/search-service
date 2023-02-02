#!/bin/sh

sleep 0.5

echo "Executing python script"
python3 /app/python_and_meilisearch/query_and_indexing.py

echo "Running server"
cd ./new_node && npm start

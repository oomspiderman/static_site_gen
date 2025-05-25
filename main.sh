#!/bin/bash

# Kill anything using port 8888
echo "Checking for server on port 8888..."
PID=$(lsof -t -i:8888)
if [ -n "$PID" ]; then
  echo "Killing existing server on port 8888 (PID $PID)..."
  kill -9 $PID
fi

# Rebuild the site
python3 src/main.py

# Serve the site
cd public && python3 -m http.server 8888
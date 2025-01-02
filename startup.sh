#!/bin/bash
apt-get update && apt-get install -y espeak
streamlit run app.py --server.port $PORT

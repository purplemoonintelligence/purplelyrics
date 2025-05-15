#!/bin/bash
cd /home/site/wwwroot/purplelyrics
pip install -r requirements.txt
exec uvicorn main:app --host 0.0.0.0 --port $PORT

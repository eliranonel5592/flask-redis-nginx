import os
from flask import Flask
import redis

app = Flask(__name__)

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)

@app.route("/")
def index():
    count = r.incr("hits")
    return f"Hello from Flask + Redis! This page was visited {count} times."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

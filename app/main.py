from flask import Flask
import redis
import os

app = Flask(__name__)

# חיבור ל-Redis לפי שם השירות בקומפוז
redis_host = os.getenv("REDIS_HOST", "redis")
redis_port = int(os.getenv("REDIS_PORT", 6379))
r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/')
def index():
    # ננסה לספור כמה פעמים ביקרו בעמוד
    count = r.incr('visits')
    return f"Hello from Flask! You visited this page {count} times."

@app.route('/reset')
def reset():
    r.delete('visits')
    return "Counter reset successfully!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

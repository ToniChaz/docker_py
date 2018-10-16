import time
import redis
from flask import Flask, send_from_directory

app = Flask(__name__, static_url_path='', static_folder='web')
r = redis.Redis(host='redis', port=6379, charset="utf-8", decode_responses=True)


def main():
    print(' * Loading data..', flush=True)
    r.set('user', 'root')
    r.set('password', '1234')


def get_data():
    print(' * Method get_data()', flush=True)
    retries = 5
    while True:
        try:
            return [r.incr('hits'), r.get('user')]
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/api')
def api():
    print(' * Endpoint /api', flush=True)
    count, user = get_data()
    return 'Hello ' + user + '! You have been seen {} times.\n'.format(count)


@app.route('/')
def index():
    print(' * Endpoint /index.html', flush=True)
    return send_from_directory('web', 'index.html')


if __name__ == "__main__":
    print(' * Application running..', flush=True)
    main()
    app.run(host="0.0.0.0", debug=True)

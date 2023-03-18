from flask import Flask, abort, jsonify
import dbm

class MemoryStorage:
    d = {}
    def __init__(self):
        pass
    def set(self, k, v):
        self.d[k] = v
    def get(self, k):
        return self.d[k]
    def delete(self, k):
        return self.d.pop(k)
    def exists(self, k):
        return k in self.d
    def list(self):
        return self.d

class DbmStorage:
    def __init__(self, db):
        self.db = db
    def set(self, k, v):
        self.db[k] = v
    def get(self, k):
        return self.db[k]
    def delete(self, k):
        tmp = self.db[k]
        del self.db[k]
        return tmp
    def exists(self, k):
        return k in self.db
    def list(self):
        return {k.decode('ascii'):self.db[k].decode('ascii') for k in self.db.keys()}

data_path = "/data"
db_path = data_path + "/" + "data.db"
store = DbmStorage(None)
app = Flask(__name__)
@app.route('/url/<key>', methods=['GET'])
def url_get(key):
    if store.exists(key):
        return store.get(key)
    abort(404)
@app.route('/url/<key>/<value>', methods=['POST'])
def url_set(key, value):
    store.set(key, value)
    return store.get(key)
@app.route('/url/<key>', methods=['DELETE'])
def url_delete(key):
    if store.exists(key):
        return store.delete(key)
    abort(404)
@app.route('/list', methods=['GET'])
def url_list():
    return store.list()

@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


with dbm.open(db_path, 'c') as db:
    store.db = db
    app.run(host='0.0.0.0', port=8188)

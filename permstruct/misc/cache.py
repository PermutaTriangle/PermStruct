import sys
import base64
import os
import tempfile
from .hasher import Hasher
try:
    import pickle as pickle
except:
    import pickle

CACHE_PATH = os.path.join(tempfile.gettempdir(), 'PermStruct')
CACHE_LIM = 128*1024**2 # 128MB

class Cache(object):
    @staticmethod
    def get_path(key):
        # print('h start')
        h = Hasher()
        h.update(key)
        key = h.digest()
        # print('hash: ' + key)
        # print('h end')
        return os.path.join(CACHE_PATH,key)

    @staticmethod
    def contains(key):
        # print('start')
        res = os.path.exists(Cache.get_path(key))
        # print('end')
        return res

    @staticmethod
    def get(key):
        # print('get start')
        with open(Cache.get_path(key), 'rb') as f:
            res = pickle.load(f)
            # print('get done')
            return res

    @staticmethod
    def put(key, value):
        # print('put start')
        # print('putting')
        # for i,v in enumerate(sorted(value,key=repr)):
        #     print(i)
        #     print(v)
        # for i,v in enumerate(sorted(value,key=repr)):
        #     if i == 16:
        #         value = v
        #         break
        if not os.path.isdir(CACHE_PATH):
            try:
                os.mkdir(CACHE_PATH)
            except:
                sys.stderr.write('warning: could not create cache directory: %s\n' % CACHE_PATH)
                sys.stderr.write('warning: caching will be disabled\n' % CACHE_PATH)

        try:
            with open(Cache.get_path(key), 'wb') as f:
                res = pickle.dump(value,f)
        except:
            print('nooooooooooooooo')
            print(value)
            import sys
            sys.exit(0)

        # print('woo')
        # import sys
        # sys.exit(0)
        # print('put done')
        # Cache.cleanup()
        return res

    @staticmethod
    def cleanup():
        arr = []
        tot = 0
        for f in os.listdir(CACHE_PATH):
            curf = os.path.join(CACHE_PATH,f)
            if not os.path.isfile(curf):
                continue
            sz = os.path.getsize(curf)
            tot += sz
            arr.append((os.path.getmtime(curf), curf, sz))
        if tot <= CACHE_LIM:
            return
        sys.stderr.write('info: cache is full, cleaning up...\n')
        arr = sorted(arr)
        for (_,curf,sz) in arr:
            try:
                os.unlink(curf)
                tot -= sz
            except:
                sys.stderr.write('warning: could not delete file %s\n' % curf)
            if tot < CACHE_LIM:
                break


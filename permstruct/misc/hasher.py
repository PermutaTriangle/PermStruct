from hashlib import md5
import inspect

# http://stackoverflow.com/questions/5417949/computing-an-md5-hash-of-a-data-structure

class Hasher(object):
    """Hashes Python data into md5."""
    def __init__(self):
        self.md5 = md5()

    @staticmethod
    def hash(v):
        h = Hasher()
        h.update(v)
        return h.digest()

    def update(self, v):
        """Add `v` to the hash, recursively if needed."""
        self.md5.update(str(type(v)).encode('utf-8'))
        if isinstance(v, str):
            self.md5.update(v.encode('utf-8'))
        elif isinstance(v, (int, float)):
            self.update(str(v))
        elif isinstance(v, (tuple, list)):
            for e in v:
                self.update(e)
        elif isinstance(v, dict):
            keys = [ (Hasher.hash(k), k) for k in v.keys() ]
            for h,k in sorted(keys, key=lambda x: x[0]):
                self.update(h)
                self.update(v[k])
        elif isinstance(v, set):
            keys = [ Hasher.hash(k) for k in v ]
            for h in sorted(keys):
                self.update(h)
        # elif hasattr(v, '__call__'):
        #     self.update(v.__code__.co_code)
        else:
            for k in dir(v):
                if k.startswith('__'):
                    continue
                a = getattr(v, k)
                if inspect.isroutine(a):
                    continue
                # print(k)
                self.update(k)
                self.update(a)

    def digest(self):
        """Retrieve the digest of the hash."""
        return self.md5.hexdigest()


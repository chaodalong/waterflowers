# -*- coding: utf-8 -*-
def md5(str=None):
    import hashlib
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()

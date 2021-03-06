import sys

PY3 = sys.version_info[0] == 3

if PY3: # pragma: no cover
    string_types = str,
    text_type = str
else:
    string_types = basestring,
    text_type = unicode

def text_(s, encoding='latin-1', errors='strict'):
    """ If ``s`` is an instance of ``bytes``, return ``s.decode(encoding,
    errors)``, otherwise return ``s``"""
    if isinstance(s, bytes):
        return s.decode(encoding, errors)
    return s # pragma: no cover

try:
    xrange = xrange
except NameError: # pragma: no cover
    xrange = range


import pickle, os
p='movie_recommendation_model.pkl'
print('exists', os.path.exists(p))
with open(p, 'rb') as f:
    o = pickle.load(f)
print('type', type(o))
try:
    print('len', len(o))
except Exception:
    pass
if isinstance(o, dict):
    print('keys:', list(o.keys())[:50])
else:
    try:
        import numpy as np
        if isinstance(o, (list, tuple)):
            print('list/tuple len', len(o))
        elif hasattr(o, 'shape'):
            print('shape', getattr(o, 'shape'))
    except Exception:
        pass
print('repr preview:', repr(o)[:1000])

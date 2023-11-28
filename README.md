A python library for shapely geoprocessing operations

To clip a linestring (projected in equal area projection) in between two given points p1 and p2 with a precision of 1 , you can use
```python
from tools import linestrings as lnops
clipped_linestring = lnops.clip_linestring(p1, p2, linestring, step_size = 1.0)
```
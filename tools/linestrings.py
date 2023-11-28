from shapely.geometry import LineString
import numpy as np

def clip_linestring(p1, p2, linestring, step_size = 0.1):
    """ Clip a linestring between two given points.
    All geometries are assumed to be on equal area projection

    Args:
        p1 (Point): Shapely point geometry 1 which lies on the linestring
        p2 (Point): Shapely point geometry 2 which lies on the linestring
        linestring (LineString): Linestring which is to be cliped between point p1 and p2
        step_size (float, optional): Precision of the clipped linestring in the units of distance. Defaults to 0.1.        

    Returns:
        LineString: Clipped linestring
    """
    p1_distance = linestring.project(p1)
    p2_distance = linestring.project(p2)
    projected_points = []
    for dist in np.arange(p1_distance, p2_distance , step_size):
        projected_point = linestring.interpolate(dist)
        projected_points.append(projected_point)
    if(len(projected_points)>1):
        clipped_line = LineString(projected_points)
    else:
        clipped_line = LineString([p1,p2])
    return clipped_line

def split_linestring(linestring, seg_len):
    """ Split a linestring into different segments of length seg_len

    Args:
        linestring (LineString): Linestring in equal area
        seg_len (float): Length of the individual segments of the linestring

    Returns:
        list: List of linestring segments
    """
    length = linestring.length
    closer_pt, further_pt = linestring.boundary.geoms
    if(length>seg_len):
        linestrings = []
        prev_point = closer_pt
        for dist in np.arange(seg_len, length, seg_len):
            end_point = linestring.interpolate(dist)
            l1 = clip_linestring(prev_point, end_point , linestring)
            prev_point = end_point
            linestrings.append(l1)
        final = clip_linestring(end_point, further_pt, linestring)
        linestrings.append(final)
        return linestrings
    return [linestring]
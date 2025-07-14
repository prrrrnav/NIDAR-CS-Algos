from math import atan2, degrees, sin, cos, radians

def bearing(lat1, lon1, lat2, lon2):
    dLon = radians(lon2 - lon1)
    y = sin(dLon) * cos(radians(lat2))
    x = cos(radians(lat1)) * sin(radians(lat2)) - sin(radians(lat1)) * cos(radians(lat2)) * cos(dLon)
    brng = atan2(y, x)
    return (degrees(brng) + 360) % 360

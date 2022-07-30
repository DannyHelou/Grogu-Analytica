import pyproj


_projections = {}

"""
converting the utm values into a ZONE value thats fed into unproject function
"""
def zone(coordinates):
    if 56 <= coordinates[1] < 64 and 3 <= coordinates[0] < 12:
        return 32
    if 72 <= coordinates[1] < 84 and 0 <= coordinates[0] < 42:
        if coordinates[0] < 9:
            return 31
        elif coordinates[0] < 21:
            return 33
        elif coordinates[0] < 33:
            return 35
        return 37
    return int((coordinates[0] + 180) / 6) + 1

"""
Finding the letter zone of the coordinates needed unproject function
"""
def letter(coordinates):
    return 'CDEFGHJKLMNPQRSTUVWXX'[int((coordinates[1] + 80) / 8)]

"""
creating a projection of the coordinates to be fed into the unproject function
"""
def project(coordinates):
    z = zone(coordinates)
    l = letter(coordinates)
    if z not in _projections:
        _projections[z] = pyproj.Proj(proj='utm', zone=z, ellps='WGS84')
    x, y = _projections[z](coordinates[0], coordinates[1])
    if y < 0:
        y += 10000000
    return z, l, x, y

"""
converting the projection of the coordinates into long, lat output <--- function can be used without 
any prerequisites as long as information is given in format(zone, letter, longitude, latitude) <--- most commonly used
"""
def unproject(z, l, x, y):
    if z not in _projections:
        _projections[z] = pyproj.Proj(proj='utm', zone=z, ellps='WGS84')
    if l < 'N':
        y -= 10000000
    lng, lat = _projections[z](x, y, inverse=True)
    return (lng, lat)

print(unproject(40, "R", 416410, 2838000))

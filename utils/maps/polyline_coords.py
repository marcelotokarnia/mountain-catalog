from toolz import compose
#  reference: https://developers.google.com/maps/documentation/utilities/polylinealgorithm


def split(value, bits):
    arr = []
    while value >= 1 << bits:
        arr.append((value & 31))
        value >>= 5
    return arr + [value]


multiply_round = lambda x: round(x * 1e5)
to_binary = lambda x: format(x % (1 << 32), '032b')
left_shift = lambda x: format((int(x, 2) << 1) % (1 << 32), '032b')[-32:]
compliment = lambda x: format(~int(x, 2) % (1 << 32), '032b')
invert_if_negative = lambda x: (lambda y: compliment(y)[2:]) if x < 0 else (lambda z: z)
split_str_to_int = lambda x: split(int(x, 2), 5)
fix_integers = lambda x: [y + (95 if idx != len(x) - 1 else 63) for idx, y in enumerate(x)]
convert_to_str = lambda x: ''.join([chr(y) for y in x])


def encode_coord_to_str(coord):
    return compose(
        convert_to_str,
        fix_integers,
        split_str_to_int,
        invert_if_negative(coord),
        left_shift,
        to_binary,
        multiply_round
    )(coord)


def convert_latlng_to_polyline(lat, lng):
    return encode_coord_to_str(lat) + encode_coord_to_str(lng)


def encode(coords):
    for idx in range(len(coords) - 1, -1, -1):
        if idx != 0:
            coords[idx] = (
                coords[idx][0] - coords[idx - 1][0],
                coords[idx][1] - coords[idx - 1][1]
            )
    return ''.join([convert_latlng_to_polyline(*x) for x in coords])


coords_arr_to_bin = lambda coords: [
    ''.join([
        format(n, '05b') for n in coord[::-1]
    ]) for coord in coords
]


def split_str(coord_str):
    coords = [[]]
    for x in coord_str:
        value = ord(x) - 63
        coords[-1].append(value & 0x1F)
        if value < 32:
            coords.append([])
    coords.pop()
    return coords


maybe_invert_shift = lambda y: [((~int(x, 2) if x[-1] == '1' else int(x, 2)) >> 1) / 1e5 for x in y]
group_pairs = lambda y: [[y[2 * i], y[2 * i + 1]] for i in range(int(len(y) / 2))]


def fix_coords(coords):
    for idx, coord in enumerate(coords):
        if idx != 0:
            coord[0] += coords[idx - 1][0]
            coord[1] += coords[idx - 1][1]
    return coords


def decode(coord_str):
    return compose(
        fix_coords,
        group_pairs,
        maybe_invert_shift,
        coords_arr_to_bin,
        split_str
    )(coord_str)

labels = {
    'Car': 0,
    'Van': 1,
    'Truck': 2,
    'Pedestrian': 3,
    'Person_sitting': 4,
    'Cyclist': 5,
    'Tram': 6,
    'Misc': 7,
    'DontCare': 8
}

label_colors = {
    'Car': ('green', (0, 255, 0)),
    'Van': ('red', (255, 0, 0)),
    'Truck': ('yellow', (255, 255, 0)),
    'Pedestrian': ('purple', (128, 0, 128)),
    'Person_sitting': ('blue', (0, 0, 255)),
    'Cyclist': ('orange', (255, 165, 0)),
    'Tram': ('white', (255, 255, 255)),
    'Misc': ('black', (0, 0, 0)),
    'DontCare': ('pink', (255, 192, 203)),
}


class BoxCoordinates:
    classification: str
    _x1: int
    _x2: int
    _y1: int
    _y2: int

    def __init__(self, arr, raw=False):
        if not raw:
            self.classification, self._x1, self._y1, self._x2, self._y2 = read_labels(arr)
        else:
            self.classification, self._x1, self._y1, self._x2, self._y2 = arr

    def get_box(self, img_width, img_height) -> tuple:
        """Return normalized box values [x, y, w, h]"""
        width = abs(self._x1 - self._x2)
        height = abs(self._y1 - self._y2)
        x = min(self._x1, self._x2) + (width / 2)
        y = min(self._y1, self._y2) + (height / 2)
        return round(x / img_width, 6), round(y / img_height, 6), round(width / img_width, 6), round(height / img_height, 6)

    def to_line(self, img_width, img_height) -> str:
        x, y, w, h = self.get_box(img_width, img_height)
        return f"{labels[self.classification]} {x} {y} {w} {h}\n"


def read_labels(arr) -> tuple:
    """Returns [type, x1, x2, y1, y2]"""
    if len(arr) == 0:
        return None, None, None, None, None
    return arr[0], round(float(arr[4])), round(float(arr[5])), round(float(arr[6])), round(float(arr[7]))

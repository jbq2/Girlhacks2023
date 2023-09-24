# use .__dict__ to turn created object into dictionary form

class ImageWithAlien:
    
    def __init__(self, username: str, img_bson: bytes, coordinates: list):
        self.username = username
        self.img_bson = img_bson
        self.coordinates = coordinates

class User:

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

class LeaderboardStat:

    def __init__(self, username: str, time: int, num_images: int):
        self.username = username
        self.time = time
        self.num_images = num_images
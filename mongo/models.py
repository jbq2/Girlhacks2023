# use .__dict__ to turn created object into dictionary form

class ImageWithAlien:
    
    def __init__(self, username, img_bson, coordinates):
        self.username = username
        self.img_bson = img_bson
        self.coordinates = coordinates

class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password
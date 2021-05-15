# To complete: add the definition for the class MediaItem
#    and write the __init__ method.


class MediaItem:
    def __init__(self, media="", title="", price=0, ref="", director="", author="", lead_actor=""):
        self.media = media
        self.title = title
        self.price = price
        self.ref = ref
        self.director = director
        self.author = author
        self.lead_actor = lead_actor
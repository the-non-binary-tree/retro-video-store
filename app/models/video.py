from app import db

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    release_date = db.Column(db.DateTime, nullable=False)
    total_inventory = db.Column(db.Integer, nullable=False, default=1)
    rentals = db.relationship('Rental', backref='video')
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
            'total_inventory': self.total_inventory
        }
def video_from_json(request_body):
    video = Video(
        title=request_body['title'],
        release_date=request_body['release_date'],
        total_inventory=request_body['total_inventory']
    )
    return video
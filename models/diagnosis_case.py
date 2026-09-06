from models import db
from datetime import datetime

class DiagnosisCase(db.Model):
    __tablename__ = 'diagnosis_cases'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    symptoms_selected = db.Column(db.Text) 
    diagnosis_result = db.Column(db.Text)  
    confidence_score = db.Column(db.Float)
    disease_diagnosed = db.Column(db.String(100))
    location = db.Column(db.String(100))
    notes = db.Column(db.Text)
    image_path = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Case {self.id}: {self.disease_diagnosed}>'
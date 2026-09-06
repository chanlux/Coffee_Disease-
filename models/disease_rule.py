from models import db
from datetime import datetime

class Disease(db.Model):
    __tablename__ = 'diseases'
    
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    scientific_name = db.Column(db.String(100))
    description = db.Column(db.Text)
    treatment = db.Column(db.Text)
    prevention = db.Column(db.Text)
    severity = db.Column(db.String(20)) 
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    rules = db.relationship('DiseaseRule', backref='disease', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Disease {self.code}: {self.name}>'


class DiseaseRule(db.Model):
    __tablename__ = 'disease_rules'
    
    id = db.Column(db.Integer, primary_key=True)
    disease_id = db.Column(db.Integer, db.ForeignKey('diseases.id'), nullable=False)
    symptom_id = db.Column(db.Integer, db.ForeignKey('symptoms.id'), nullable=False)
    certainty_factor = db.Column(db.Float, default=1.0)
    weight = db.Column(db.Float, default=1.0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    symptom = db.relationship('Symptom', backref='rules')
    
    def __repr__(self):
        return f'<Rule D{self.disease_id}-S{self.symptom_id}>'
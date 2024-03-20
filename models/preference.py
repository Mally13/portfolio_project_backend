#!/usr/bin/python
""" holds class Preference"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Boolean, Text, Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

class Preference(BaseModel, Base):
    """Representation of a preferece """
    __tablename__ = 'preferences'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    destination = Column(String(100))
    travel_dates = Column(String(100))
    budget = Column(Float)
    accommodation_type = Column(String(50))  # Type of accommodation preferred
    room_type = Column(String(50))  # Room type preference
    amenities = Column(String(200))  # Amenities desired
    transportation_mode = Column(String(50))  # Preferred mode of transportation
    transportation_class = Column(String(50))  # Class or seating preference
    airline_preference = Column(String(100))  # Specific airline preference
    seat_preference = Column(String(50))  # Seat location preference
    activity_types = Column(String(200))  # Types of activities preferred
    cultural_preferences = Column(String(200))  # Cultural preferences
    adventure_level = Column(String(50))  # Adventure level
    dietary_restrictions = Column(String(200))  # Dietary restrictions or preferences
    language_preference = Column(String(50))  # Preferred language
    translator_requirements = Column(String(200))  # Translator or language assistance requirements
    contact_preference = Column(String(50))  # Preferred contact method
    maximum_budget = Column(Float)  # Maximum budget
    currency_preference = Column(String(50))  # Currency preference
    payment_method_preference = Column(String(50))  # Payment method preference
    special_occasion = Column(String(50))  # Special occasion or celebration
    additional_services = Column(String(200))  # Additional services or arrangements desired
    mobility_requirements = Column(String(200))  # Mobility requirements
    accommodation_accessibility = Column(String(200))  # Accommodation accessibility features
    transportation_accessibility = Column(String(200))  # Transportation accessibility accommodations
    eco_friendly_accommodation = Column(Boolean)  # Eco-friendly accommodation options
    sustainable_transportation = Column(Boolean)  # Sustainable transportation choices
    responsible_tourism = Column(Boolean)  # Responsible tourism initiatives
    additional_notes = Column(Text)  # Additional notes or customization options

    def __init__(self, *args, **kwargs):
        """initializes user preferences"""
        super().__init__(*args, **kwargs)

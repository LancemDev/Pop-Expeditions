import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import create_app, db
from app.models import Country, Destination

app = create_app()

with app.app_context():
    db.create_all()

    # Add countries
    kenya = Country(name='Kenya', languages_spoken='Swahili, English', currency='Kenyan Shilling', visa_requirements='Visa required')
    tanzania = Country(name='Tanzania', languages_spoken='Swahili, English', currency='Tanzanian Shilling', visa_requirements='Visa required')

    db.session.add(kenya)
    db.session.add(tanzania)
    db.session.commit()

    # Add destinations
    destinations = [
        Destination(name='Ruaha National Park', description='A large park in Tanzania', photo_main='ruaha_main.jpg', photo_profile='ruaha_profile.jpg', photo_others='ruaha_others.jpg', area='20,226 km²', country_id=tanzania.id),
        Destination(name='Selous Game Reserve', description='A large game reserve in Tanzania', photo_main='selous_main.jpg', photo_profile='selous_profile.jpg', photo_others='selous_others.jpg', area='50,000 km²', country_id=tanzania.id),
        Destination(name='Mikumi National Park', description='A national park in Tanzania', photo_main='mikumi_main.jpg', photo_profile='mikumi_profile.jpg', photo_others='mikumi_others.jpg', area='3,230 km²', country_id=tanzania.id),
    ]

    db.session.bulk_save_objects(destinations)
    db.session.commit()
import csv
from django.core.management.base import BaseCommand
from trucks.models import FoodTruck
from django.db import transaction
import os

class Command(BaseCommand):
    help = 'Import food trucks from CSV file'

    def handle(self, *args, **options):
        file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'data/food-truck-data.csv')

        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            try:
                with transaction.atomic():
                    for row in reader:
                        try:
                            # Skip processing if 'expiration_date' or 'Approved' is present in the row
                            if 'ExpirationDate' in row or 'Approved' in row:
                                continue

                            # Handle the case where 'X' is empty or not a valid float
                            x_value = float(row['X']) if row['X'].strip() else 0.0

                            # Handle the case where 'Y' is empty or not a valid float
                            y_value = float(row['Y']) if row['Y'].strip() else 0.0

                            truck = FoodTruck(
                                location_id=row['locationid'],
                                applicant=row['Applicant'],
                                facility_type=row['FacilityType'],
                                cnn=row['cnn'],
                                location_description=row['LocationDescription'],
                                address=row['Address'],
                                block_lot=row['blocklot'],
                                block=row['block'],
                                lot=row['lot'],
                                permit=row['permit'],
                                status=row['Status'],
                                food_items=row['FoodItems'],
                                x=x_value,
                                y=y_value,
                                latitude=float(row['Latitude']),
                                longitude=float(row['Longitude']),
                                schedule=row['Schedule'],
                                dayshours=row['dayshours'],
                                noi_sent=row['NOISent'],
                                received=row['Received'],
                                prior_permit=row['PriorPermit'],
                                location=row['Location'],
                                fire_prevention_districts=row['Fire Prevention Districts'],
                                police_districts=row['Police Districts'],
                                supervisor_districts=row['Supervisor Districts'],
                                zip_codes=row['Zip Codes'],
                                neighborhoods_old=row['Neighborhoods (old)'],
                            )
                            truck.save()

                        except ValueError as e:
                            print(f"Error processing row: {e}")
                        except Exception as e:
                            print(f"Error: {e}")

            except Exception as outer_exception:
                print(f"Error: {outer_exception}")

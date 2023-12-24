import csv
from django.core.management.base import BaseCommand
from trucks.models import FoodTruck
from django.db import transaction
import os

class Command(BaseCommand):
    help = 'Import food trucks from CSV file'

    def handle(self, *args, **options):
        # Define the path to the CSV file
        file_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
            'data/food-truck-data.csv'
        )

        # Open the CSV file for reading
        with open(file_path, 'r') as file:
            # Create a CSV reader using DictReader for easy access to columns
            reader = csv.DictReader(file)
            
            try:
                # Use a database transaction for atomicity
                with transaction.atomic():
                    # Iterate over each row in the CSV file
                    for row in reader:
                        try:
                            # Skip processing if 'ExpirationDate' or 'Approved' is present in the row
                            if 'ExpirationDate' in row or 'Approved' in row:
                                continue

                            # Convert 'X' and 'Y' values to floats, handling empty or invalid cases
                            x_value = float(row['X']) if row['X'].strip() else 0.0
                            y_value = float(row['Y']) if row['Y'].strip() else 0.0

                            # Create a FoodTruck object with data from the CSV row
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

                            # Save the FoodTruck object to the database
                            truck.save()

                        except ValueError as e:
                            # Handle ValueError (e.g., when converting to float)
                            print(f"Error processing row: {e}")
                        except Exception as e:
                            # Handle other exceptions
                            print(f"Error: {e}")

            except Exception as outer_exception:
                # Handle exceptions at the outer level (e.g., database transaction failure)
                print(f"Error: {outer_exception}")

import json
import csv
import os

class Exporter:
    """
    Handles exporting processed data
    to different file formats.
    """

    def __init__(self, output_dir="exports"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def export_to_json(self, data, filename="cleaned_data.json"):
        """
         Save list of dictionaries to a JSON file.
        """
        path = os.path.join(self.output_dir, filename)
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
            print(f"Data successfully exported to {path}")
        except Exception as e:
            print(f"Failed to export JSON: {e}")
            return False
        return True
         

    def export_to_csv(self, data, filename="cleaned_data.csv"):
        """
        
        """
        if not data:
            print("No data to export.")
            return False
        path = os.path.join(self.output_dir, filename)
        try:
            with open(path, "w", newline="",encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
            print(f"Data successfully exported to {path}")
        except Exception as e:
            print(f"Failed to export CSV: {e}")
            return False
        return True


        


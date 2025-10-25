import datetime

class Transformer:
    """
      Cleans, format, and enriches validated records for analysis
    """
    def __init__(self):
        pass
    def transform_record(self, record):
        """Apply transformation per row"""
        try:
            #convert numeric record to float
            record["quantity"] = float(record["quantity"])
            record["price"] = float(record["price"])
            record["total"] = float(record["total"])

            # Standardize text
            record["item"] = record["item"].strip().title()
            record["payment_status"] = record["payment_status"].strip().lower()

            #Format  timestamp
            record["timestamp"] = datetime.datetime.strptime(record["timestamp"],"%Y-%m-%d")

        except Exception as e:
            print(f"Tranformaton failed for record {record.get('order_id')}: {e}")
            return None
        
        return record
    
    def transform_all(self, records):
        """
        Apply transform_record to all items in a dataset.
        Returns a list of successfully transformed records.
        """
        transformed = []
        for r in records:
            new_r = self.transform_record(r)
            if new_r:
                transformed.append(r)
        return transformed


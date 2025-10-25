import re
class Validator:
    """Validates order records ensuring data completeness,
      type correctness, 
      and logical consistency."""
    def __init__(self):
            pass
    def validate_record(self, record):
        """
        Validate a single record.
        Returns True if record passes all checks, otherwise False.
        """
        required_fields = ["order_id", "timestamp", "item", "quantity", "price", "payment_status", "total"]

        # Check all required fields exist
        for field in required_fields:
            if field not in record or record[field] in (None, "", " "):
                return False
        if not isinstance(record["order_id"], (str, int)):
            return False
        if not isinstance(record["item"], str):
            return False

        #Check numeric fields
            # numeric_fields = ["quantity", "price", "total"]
            # for field in numeric_fields:
            #     try:
            #         value = float(record[field])
            #         if value <= 0:
            #             return False
            #     except (ValueError, TypeError):
            #         return False
        # check numeric fields
        try:
            quantity = float(record["quantity"])
            price = float(record["price"])
            total = float(record["total"])
        except (ValueError, TypeError):
            return False
        if quantity <= 0 or price <= 0 or total <= 0:
            return False 
        if abs((quantity*price)- total) > 0.01:
            return False
        
        #Normalize payment status
        status = str(record["payment_status"].strip().lower())
        if status not in {"paid", "pending","refunded"}:
            return False
        
         # Ensure timestamp is valid, YYYY-MM-DD
        if not re.match(r"\d{4}-\d{2}-\d{2}", str(record.get("timestamp", ""))):
            return False
        return True
        
       
    

    # validate all and return valid records only
    def validate_all(self, data):
        if not isinstance(data, list):
            raise ValueError("Input data must be a list of dictionaries")

        valid_records = [] #[r for r in data if self.validate_record(r)]
        invalid_records_count = 0
        for r in data:
            if self.validate_record(r):
                valid_records.append(r)
            else:
                print(f"Invalid record skipped: {r}")
                invalid_records_count += 1
        print(f"Total number of invalid records skipped is: \n {invalid_records_count} out of the total {len(data)}")
                
        return valid_records  #, invalid_records_count


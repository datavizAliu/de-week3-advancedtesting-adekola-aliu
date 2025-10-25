from collections import Counter, defaultdict

class Analyzer:
    """
    Performs data analysis and summary data on transformed data.
    """
    def __init__(self, data):
        if not isinstance(data, list):
            raise ValueError("Data must be a list of dictionaries")
        self.data = data

    def total_sales(self):
        """
         Compute total revenue from all records.
        """
        return sum(r.get("total", 0) for r in self.data)
    
    def average_order_value(self):
        """
        Compute average total per order.
        """
        if not self.data:
            return 0
        return self.total_sales() / len(self.data)
    
    def sales_by_status(self):
        """
        Return dictionary of total sales grouped by payment_status.
        """
        result = defaultdict(float)
        for r in self.data:
            status = r.get("payment_status", "unknown")
            result[status] += r.get("total", 0)
        return dict(result) 
    def top_items(self, n=3):
        """
        Return the top N most frequently ordered items.
        """
        items = [ r["item"]for r in self.data if "item" in r]
        return Counter(items).most_common(n)
    


        
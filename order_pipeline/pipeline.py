from order_pipeline.reader import Reader
from order_pipeline.validator import Validator
from order_pipeline.transformer import Transformer
from order_pipeline.analyzer import Analyzer
from order_pipeline.exporter import Exporter

class Pipeline:
    """
    Orchestrate the full data processing pipeline
    """

    def __init__(self, input_path):
        self.input_path = input_path
        self.reader = Reader()
        self.validator = Validator()
        self.transformer = Transformer()
        self.exporter = Exporter()

    def run(self):
        """
        
        """
        print("Starting pipeline excution...")

        #Read
        raw_data = self.reader.read_json(self.input_path)
        print(f"loaded {len(raw_data)} records")

        #Validate
        valid_data = self.validator.validate_all(raw_data)
        print(f"{len(valid_data)} valid records after validation")

        #Transform
        transformed_data = self.transformer.transform_all(valid_data)
        print(f"{len(transformed_data)} records transformed successfully")

        #analyze

        analyzer = Analyzer(transformed_data)
        summary = {
            "total_sales": analyzer.total_sales(),
            "average_order_value": analyzer.average_order_value(),
            "sales_by_status": analyzer.sales_by_status(),
            "top_items": analyzer.top_items()
        }

        print(" Analysis Summary:")
        for k, v in summary.items():
            print(f"{k}: {v}")
        
        #Export results
        self.exporter.export_to_json(transformed_data, "cleaned_orders.json")
        self.exporter.export_to_csv(summary, "summary.json")

        print( "Pipeline completed successfully.")
        return summary
             
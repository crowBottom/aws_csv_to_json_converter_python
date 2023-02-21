# aws_csv_to_json_converter_python
A simple service that converts a csv to json format for use in other microservices.

## constructs utilized
This project uses an infrastructure as code approach and uses an AWS S3 bucket which triggers an AWS Lmabda when a csv file is uploaded to the bucket. The lambda parses the csv file into json.

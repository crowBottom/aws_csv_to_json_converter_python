import json
import boto3
import csv

def handler(event, context):
    print("CSV to JSON Lambda Running")
    print(f"Incoming Event")
    print(f"{event}")

    try:
        # Get the object from the event and show its content type
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
        print("utilizing bucket name and bucket key to get csv object")


        # Convert csv file to json format
        s3 = boto3.client('s3')
        csv_obj = s3.get_object(Bucket=bucket, Key=key)
        csv_string = csv_obj['Body'].read().decode('utf-8')
        print("csv object retrieved from bucket")
        print("converting csv object into json")


        csv_list = list(csv.DictReader(csv_string.splitlines()))
        json_data = json.dumps(csv_list)
        print(f"Converted json: {json_data}")
        print("NEXT STEPS: Iterate over json")



    except Exception as e:
        print(f"Error: {e}")
        print(f"Unable to get object from bucket {bucket} with key {key}")

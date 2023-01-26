import os

import aws_cdk
import cdk

app = aws_cdk.App()

cdk.CSVConverter(
    app,
    "csv-converter-dev",
    env=aws_cdk.Environment(account="221278850141", region="us-east-1"),
    description="Convert a csv to json and store record in Dynamo",
    tags={
        "Application": "CSV converter python application",
        "Environment": "dev",
        "Version": os.environ["VERSION"]
    },
)

app.synth()

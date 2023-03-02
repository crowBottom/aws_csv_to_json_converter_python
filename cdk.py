import os

import aws_cdk
import cdk

app = aws_cdk.App()

cdk.CSVConverter(
    app,
    "csv-converter-dev",
    env=aws_cdk.Environment(account="221278850141", region="us-east-1"),
    description="Convert a csv to json",
    tags={
        "Application": "CSV converter python application",
        "Environment": "dev",
        "Version": os.environ["VERSION"]
    },
)

cdk.CSVConverter(
    app,
    "csv-converter-staging",
    env=aws_cdk.Environment(account="221278850141", region="us-east-1"),
    description="Convert a csv to json",
    tags={
        "Application": "CSV converter python application",
        "Environment": "staging",
        "Version": os.environ["VERSION"]
    },
)

cdk.CSVConverter(
    app,
    "csv-converter-prod",
    env=aws_cdk.Environment(account="221278850141", region="us-east-1"),
    description="Convert a csv to json",
    tags={
        "Application": "CSV converter python application",
        "Environment": "prod",
        "Version": os.environ["VERSION"]
    },
)

app.synth()

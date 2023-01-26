import os

import aws_cdk
import cdk

app = aws_cdk.App()

cdk.UHCAutoOrderIntake(
    app,
    "uhc-auto-order-intake-dev",
    env=aws_cdk.Environment(account="221278850141", region="us-east-1"),
    description="Auto order intake python dev environment for uhc",
    tags={
        "Application": "Auto order intake python application",
        "Environment": "dev",
        "Version": os.environ["VERSION"]
    },
)

app.synth()

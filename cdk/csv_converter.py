import builtins
import aws_cdk
import constructs

from aws_cdk import (
    aws_lambda as _lambda,
    aws_sqs as sqs,
    aws_events as events,
    aws_s3 as s3,
    aws_s3_notifications as s3n,
)


class CSVConverter(aws_cdk.Stack):
    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *args,
        **kwargs
    ):

        super().__init__(scope, id, *args, **kwargs)

        # Define resources in your stack below

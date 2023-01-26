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


        # Define an S3
        image_bucket = s3.Bucket(
            scope=self,
            id="image-bucket"
        )


        # Define a Lmabda to convert csv files to json and store the records in Dynamo
        csv_converter_lambda = _lambda.Function(
            scope=self,
            id="csv-converter-lambda",
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset("events/convert_files"),
            handler="lambda_function.lambda_handler",
        )


        # Define a notification to trigger the lambda from S3
        image_bucket.add_event_notification(
            s3.EventType.OBJECT_CREATED,
            s3n.LambdaDestination(csv_converter_lambda)
        )

        # Define a DynamoDB

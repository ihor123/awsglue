import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality
import gs_now

####test comment lets see

args = getResolvedOptions(sys.argv, ['JOB_NAME','BRONZE_S3BUCKET','silver_s3bucket','source_supplier'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

bronze_s3bucket=args['BRONZE_S3BUCKET']
silver_s3bucket=args['silver_s3bucket']
source_supplier=args['source_supplier']


# Script generated for node Amazon S3
AmazonS3_node1750776576879 = glueContext.create_dynamic_frame.from_options(format_options={"compression": "snappy"}, connection_type="s3", format="parquet", connection_options={"paths": [bronze_s3bucket]}, transformation_ctx="AmazonS3_node1750776576879")

# Script generated for node Add Current Timestamp
AddCurrentTimestamp_node1750847898093 = AmazonS3_node1750776576879.gs_now(colName="TimeStampLoad")

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=AddCurrentTimestamp_node1750847898093, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1750776547134", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3_node1750778049146 = glueContext.write_dynamic_frame.from_options(frame=AddCurrentTimestamp_node1750847898093, connection_type="s3", format="glueparquet", connection_options={"path": silver_s3bucket, "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="AmazonS3_node1750778049146")

job.commit()
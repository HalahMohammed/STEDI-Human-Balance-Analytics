import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
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

# Script generated for node customer_curated
customer_curated_node1777393398419 = glueContext.create_dynamic_frame.from_options(format_options={"multiLine": "false"}, connection_type="s3", format="json", connection_options={"paths": ["s3://databucketdemo53/customer_curated/"], "recurse": True}, transformation_ctx="customer_curated_node1777393398419")

# Script generated for node step_trainer
step_trainer_node1777395242448 = glueContext.create_dynamic_frame.from_options(format_options={"multiLine": "false"}, connection_type="s3", format="json", connection_options={"paths": ["s3://databucketdemo53/step_trainer/"], "recurse": True}, transformation_ctx="step_trainer_node1777395242448")

# Script generated for node Renamed keys for Join
RenamedkeysforJoin_node1777407945011 = ApplyMapping.apply(frame=step_trainer_node1777395242448, mappings=[("sensorreadingtime", "bigint", "sensorreadingtime", "bigint"), ("serialnumber", "string", "serial_number", "string"), ("distancefromobject", "int", "distancefromobject", "int")], transformation_ctx="RenamedkeysforJoin_node1777407945011")

# Script generated for node Join
Join_node1777395281184 = Join.apply(frame1=RenamedkeysforJoin_node1777407945011, frame2=customer_curated_node1777393398419, keys1=["serial_number"], keys2=["serialnumber"], transformation_ctx="Join_node1777395281184")

# Script generated for node Select Fields
SelectFields_node1777399643993 = SelectFields.apply(frame=Join_node1777395281184, paths=["t__serialnumber", "t__distancefromobject", "t__sensorreadingtime", "sensorreadingtime", "distancefromobject", "serial_number"], transformation_ctx="SelectFields_node1777399643993")

# Script generated for node step_trainer_trusted
EvaluateDataQuality().process_rows(frame=SelectFields_node1777399643993, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1777399112117", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
step_trainer_trusted_node1777399675127 = glueContext.write_dynamic_frame.from_options(frame=SelectFields_node1777399643993, connection_type="s3", format="json", connection_options={"path": "s3://databucketdemo53/step_trainer_trusted/", "partitionKeys": []}, transformation_ctx="step_trainer_trusted_node1777399675127")

job.commit()

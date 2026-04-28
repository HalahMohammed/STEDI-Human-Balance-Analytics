import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Read Step Trainer Trusted
step_trainer_trusted = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://databucketdemo53/step_trainer_trusted/"],
        "recurse": True
    },
    transformation_ctx="step_trainer_trusted"
)

# Read Accelerometer Trusted
accelerometer_trusted = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://databucketdemo53/accelerometer_trusted/"],
        "recurse": True
    },
    transformation_ctx="accelerometer_trusted"
)

# Join on timestamp
joined = Join.apply(
    frame1=step_trainer_trusted,
    frame2=accelerometer_trusted,
    keys1=["sensorreadingtime"],
    keys2=["timestamp"],
    transformation_ctx="joined"
)

# Keep only required fields
machine_learning_curated = ApplyMapping.apply(
    frame=joined,
    mappings=[
        ("sensorreadingtime", "long", "sensorreadingtime", "long"),
        ("serialnumber", "string", "serialnumber", "string"),
        ("distancefromobject", "int", "distancefromobject", "int"),
        ("user", "string", "user", "string"),
        ("x", "double", "x", "double"),
        ("y", "double", "y", "double"),
        ("z", "double", "z", "double")
    ],
    transformation_ctx="machine_learning_curated"
)

# Write Machine Learning Curated
glueContext.write_dynamic_frame.from_options(
    frame=machine_learning_curated,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://databucketdemo53/machine_learning_curated/",
        "partitionKeys": []
    },
    transformation_ctx="machine_learning_curated_output"
)

job.commit()

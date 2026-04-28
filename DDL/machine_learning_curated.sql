CREATE EXTERNAL TABLE IF NOT EXISTS `stedi`.`machine_learning_curated` (
  `sensorreadingtime` bigint,
  `serialnumber` string,
  `distancefromobject` int
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
WITH SERDEPROPERTIES ('serialization.format' = '1')
LOCATION 's3://databucketdemo53/step_trainer/'
TBLPROPERTIES ('has_encrypted_data' = 'false');

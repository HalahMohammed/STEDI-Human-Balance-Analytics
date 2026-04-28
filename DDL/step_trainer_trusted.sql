CREATE EXTERNAL TABLE IF NOT EXISTS `stedi`.`step_trainer_trusted` (
  `sensorreadingtime` bigint,
  `serial_number` string,
  `distancefromobject` int
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
WITH SERDEPROPERTIES ('serialization.format' = '1')
LOCATION 's3://databucketdemo53/step_trainer_trusted/'
TBLPROPERTIES ('has_encrypted_data' = 'false');

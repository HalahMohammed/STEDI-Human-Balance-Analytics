CREATE EXTERNAL TABLE IF NOT EXISTS `stedi`.`customers_curated` (
  `registrationdate` bigint,
  `customername` string,
  `birthday` string,
  `sharewithfriendsasofdate` bigint,
  `lastupdatedate` bigint,
  `email` string,
  `serialnumber` string,
  `phone` string,
  `sharewithresearchasofdate` bigint,
  `sharewithpublicasofdate` bigint
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
WITH SERDEPROPERTIES ('serialization.format' = '1')
LOCATION 's3://databucketdemo53/customer_trusted/'
TBLPROPERTIES ('has_encrypted_data' = 'false');

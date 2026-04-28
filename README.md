# STEDI Human Balance Analytics

This project implements a serverless data lakehouse pipeline on AWS for the STEDI Human Balance Analytics dataset. The goal is to ingest raw customer, accelerometer, and step trainer data from Amazon S3, sanitize the data according to customer privacy consent, and prepare curated datasets for downstream machine learning.

The pipeline is implemented using:

- Amazon S3 for lakehouse storage
- AWS Glue Studio for ETL jobs
- AWS Glue Data Catalog for table metadata
- Amazon Athena for SQL validation and querying
- JSON data format for landing, trusted, and curated zones

---

## Project Architecture

The lakehouse is organized into three zones:

```text
Landing Zone  →  Trusted Zone  →  Curated Zone

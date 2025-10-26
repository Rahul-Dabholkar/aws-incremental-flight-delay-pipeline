import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
import re

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node Raw Flights Data - Glue Catalogue Table
RawFlightsDataGlueCatalogueTable_node1761075022491 = glueContext.create_dynamic_frame.from_catalog(
    database="project1-airlines-datamart", 
    table_name="raw_flights", 
    transformation_ctx="RawFlightsDataGlueCatalogueTable_node1761075022491"
    )

# Script generated for node Airports Dim - Redshift Glue Catalogue Table
AirportsDimRedshiftGlueCatalogueTable_node1761077115851 = glueContext.create_dynamic_frame.from_catalog(
    database="project1-airlines-datamart", 
    table_name="dev_project1_airlines_airports_dim", 
    redshift_tmp_dir="s3://aws-glue-assets-360226252516-ap-south-1/temporary/", 
    transformation_ctx="AirportsDimRedshiftGlueCatalogueTable_node1761077115851"
    )

# Script generated for node Filter
Filter_node1761075176644 = Filter.apply(
    frame=RawFlightsDataGlueCatalogueTable_node1761075022491, 
    f=lambda row: (row["depdelay"] >= 60), 
    transformation_ctx="Filter_node1761075176644")

# Script generated for node Departure Airport Join
Filter_node1761075176644DF = Filter_node1761075176644.toDF()
AirportsDimRedshiftGlueCatalogueTable_node1761077115851DF = AirportsDimRedshiftGlueCatalogueTable_node1761077115851.toDF()
DepartureAirportJoin_node1761077003455 = DynamicFrame.fromDF(
    Filter_node1761075176644DF.join(
        AirportsDimRedshiftGlueCatalogueTable_node1761077115851DF, (
            Filter_node1761075176644DF['originairportid'] == AirportsDimRedshiftGlueCatalogueTable_node1761077115851DF['airport_id']), "left"), 
            glueContext, "DepartureAirportJoin_node1761077003455"
            )

# Script generated for node Modify Departure Airport Columns
ModifyDepartureAirportColumns_node1761077432786 = ApplyMapping.apply(
    frame=DepartureAirportJoin_node1761077003455, 
    mappings=[("carrier", "string", "carrier", "string"), 
              ("destairportid", "long", "destairportid", "long"), 
              ("depdelay", "long", "dep_delay", "bigint"), 
              ("arrdelay", "long", "arr_delay", "bigint"), 
              ("airport_id", "bigint", "airport_id", "long"), 
              ("city", "string", "dep_city", "string"), 
              ("name", "string", "dep_airport", "string"), 
              ("state", "string", "dep_state", "string")], 
    transformation_ctx="ModifyDepartureAirportColumns_node1761077432786")

# Script generated for node Arrival Airport Join
ModifyDepartureAirportColumns_node1761077432786DF = ModifyDepartureAirportColumns_node1761077432786.toDF()
AirportsDimRedshiftGlueCatalogueTable_node1761077115851DF = AirportsDimRedshiftGlueCatalogueTable_node1761077115851.toDF()
ArrivalAirportJoin_node1761077642729 = DynamicFrame.fromDF(
    ModifyDepartureAirportColumns_node1761077432786DF.join(
        AirportsDimRedshiftGlueCatalogueTable_node1761077115851DF, 
        (ModifyDepartureAirportColumns_node1761077432786DF['destairportid'] == AirportsDimRedshiftGlueCatalogueTable_node1761077115851DF['airport_id']), "left"), 
        glueContext, "ArrivalAirportJoin_node1761077642729"
        )

# Script generated for node Modify Arrival Airport Columns
ModifyArrivalAirportColumns_node1761077675417 = ApplyMapping.apply(
    frame=ArrivalAirportJoin_node1761077642729, 
    mappings=[("carrier", "string", "carrier", "string"), 
              ("destairportid", "long", "destairportid", "long"), 
              ("dep_delay", "bigint", "dep_delay", "long"), 
              ("arr_delay", "bigint", "arr_delay", "long"), 
              ("airport_id", "long", "airport_id", "bigint"), 
              ("dep_city", "string", "dep_city", "string"), 
              ("dep_airport", "string", "dep_airport", "string"), 
              ("dep_state", "string", "dep_state", "string"), 
              ("airport_id", "bigint", "airport_id", "bigint"), 
              ("city", "string", "arr_city", "string"), 
              ("name", "string", "name", "string"), 
              ("state", "string", "arr_state", "string")], 
    transformation_ctx="ModifyArrivalAirportColumns_node1761077675417")

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1761077928165 = glueContext.write_dynamic_frame.from_catalog(
    frame=ModifyArrivalAirportColumns_node1761077675417, 
    database="project1-airlines-datamart", 
    table_name="dev_project1_airlines_daily_flights_fact", 
    redshift_tmp_dir="s3://project1-airlines-data-ingestion-landing-zone",
    additional_options={"aws_iam_role": "arn:aws:iam::360226252516:role/redshift_access_s3_role"}, 
    transformation_ctx="AWSGlueDataCatalog_node1761077928165"
    )

job.commit()
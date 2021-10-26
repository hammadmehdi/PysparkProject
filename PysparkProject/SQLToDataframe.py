from pyspark.context import SparkContext
from pyspark.sql.context import SQLContext
from pyspark.sql import functions as F
from pyspark.sql.session import SparkSession

val prop=new java.util.Properties()
prop.put("user","username")
prop.put("password","yourpassword")
val url="jdbc:mysql://host:port/db_name"

val df=spark.read.jdbc(url,"table_name",prop)
df.show()
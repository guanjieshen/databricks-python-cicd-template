from pyspark.sql import dataframe
from pyspark.sql.functions import col, round

def convertFtoC(df: dataframe, tempCol:str, outputColName: str) -> dataframe:

    return df.withColumn(outputColName, (col(tempCol) - 32) * (5/9))

def roundedTemp(df: dataframe, tempCol:str) -> dataframe:

    return df.withColumn("rounded_temp", round(tempCol, 2)).drop(col(tempCol)).withColumnRenamed("rounded_temp",tempCol)

  
import snowflake.connector
import pandas as pd

print("connecting to Snowflake")
snowconn = snowflake.connector.connect(user='sridarkrishnamoorthy', password='Pass#123', account='aka25424.us-east-1')

cv = snowconn.cursor()
cv2 = snowconn.cursor()

cv.execute("SELECT * FROM SNOWFLAKE_SAMPLE_DATA.INFORMATION_SCHEMA.DATABASES;")
cv2.execute("INSERT INTO A1.PUBLIC.TWO VALUES (9,9)")

df = cv.fetch_pandas_all()
# df2 = cv.fetch_pandas_all()
# df = cv.fetchall()
# df = cv.fetchone()
# df = cv.fetchmany()
# df = cv.fetch_pandas_batches()
# for df in cv.fetch_pandas_batches():
#     my_dataframe_processing_function(df)

# to apply where condition in the dataframe result set
# df1 = pd.DataFrame({'database_name': ['DEMO_DB']})
# print(df1)

print(df)
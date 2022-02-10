# Databricks notebook source
# DBTITLE 1,Importando biblioteca
import pandas as pd


# COMMAND ----------

# DBTITLE 1,Extração da Api
Api_dolar = pd.read_csv("https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial='01-01-2019'&@dataFinalCotacao='12-31-2025'&$top=9000&$format=text/csv&$select=cotacaoCompra,cotacaoVenda,dataHoraCotacao")
             

# COMMAND ----------

# DBTITLE 1,Criação do Data Frame
df = pd.DataFrame(Api_dolar)
print(df)

# COMMAND ----------

# DBTITLE 1,Conexão com o SQL
servidor = 'sql-estudo.database.windows.net'
porta = 1433
banco = 'db-estudos'
usuario = 'admin-azure'
senha = 'a&Ehs&HB'
jdbcDriver = 'com.microsoft.sqlserver.jdbc.SQLServerDriver'
stage = 'dolar_Rafael_Mendes.dolar_stage_RafaelMendes2'


# COMMAND ----------

jdbcUrl = f"jdbc:sqlserver://{servidor}:{porta};databaseName={banco};user={usuario};password={senha}"
  #
stage = 'dolar_Rafael_Mendes.dolar_stage_RafaelMendes2'



# COMMAND ----------

dataframe2 = spark.createDataFrame(df)
dataframe2.write \
    .format ("jdbc") \
    .option("url",jdbcUrl )\
    .option("dbtable", "dolar_Rafael_Mendes.dolar_Stage_RafaelMendes2")\
    .mode("overwrite")\
    .save()

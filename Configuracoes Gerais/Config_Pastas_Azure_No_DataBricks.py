# Databricks notebook source
# DBTITLE 1,Abaixo comandos que podem ser úteis em qualquer situacao
"""
=========================================================================
Listando diretorio   ( somente a  "/" identifica diretorio raiz)
%fs
ls /

=========================================================================
# Listando TODAS as pastas
%python
dbutils.fs.ls("/mnt/Bruno_DataLake")

=========================================================================
#Criando diretorio
%fs mkdirs /mnt/diretoriosDataLake
%python mkdirs /mnt/diretoriosDataLake

=========================================================================
#Removendo diretorio criado errado
%fs rm -r /teste/

=========================================================================
"""

# COMMAND ----------

# DBTITLE 1,Criando pasta RAIZ para receber Diretorios do Data Lake
# MAGIC %fs
# MAGIC mkdirs /mnt/Bruno_DataLake

# COMMAND ----------

# DBTITLE 1,Confirma Diretorio criado no passo anterior
# MAGIC %fs
# MAGIC ls /mnt/Bruno_DataLake/

# COMMAND ----------

# DBTITLE 1,Config Acesso Databricks => Data Lake   -   Dados do Registro de APP feito no Azure com Acessos
# https://docs.databricks.com/pt/dbfs/mounts.html#mount-adls-gen2-or-blob-storage-with-abfs  (Aqui tem a config Python e Scala)
# Esta config aqui foi baseada no que criei em como configurar o databricks do 0

configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": "8e7b5b81-da9d-42b1-9ba9-d18d9e906317",
           "fs.azure.account.oauth2.client.secret": "LN_8Q~sk-95enqZ88gREqj7.qemwZZ7Kbq04TccL",
           "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/347e59b9-a070-4775-b422-c536805d6492/oauth2/token"
           }

# COMMAND ----------

# DBTITLE 1,Montar Diretorios do Data Lake => DataBricks (DBFS)
dbutils.fs.mount(
  source = "abfss://estudos-gerais-bruno@datalake20231015.dfs.core.windows.net/",
   mount_point = "/mnt/Bruno_DataLake",
  extra_configs = configs)

# COMMAND ----------

# DBTITLE 1,Confirma PASTAS do AZURE criadas no Databricks (Inbound, Bronze, Silve). Para visualizar usar Catalog e depois DBFS
# MAGIC %fs
# MAGIC ls /mnt/Bruno_DataLake/

# COMMAND ----------

# DBTITLE 1,Este token abaixo é do Github, no caso para que o Databricks armazene os notebooks lá
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

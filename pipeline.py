from etl import pipeline_calcular_kpi_de_vendas_consolidado

pasta: str = 'data'
formato_saida: list = ['csv', 'parquet']

pipeline_calcular_kpi_de_vendas_consolidado(pasta=pasta, formato_saida=formato_saida)
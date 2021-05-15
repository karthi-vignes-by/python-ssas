import ssas_api 
conn = ssas_api.set_conn_string(
server='powerbi://api.powerbi.com/v1.0/myorg/_Analytics 2.0',
db_name='carbon-footprint-new',
username='karthi.vignes@jda.com',
password='Jda@1234'
)

dax_string = '''
   EVALUATE
   CALCULATETABLE(inbound-emissions)
   '''

df = ssas_api.get_DAX(connection_string=conn, dax_string=dax_string)
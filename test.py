import ssas_api 
conn = ssas_api.set_conn_string(
server='powerbi://api.powerbi.com/v1.0/myorg/_Analytics 2.0',
db_name='carbon-footprint-new',
username=,
password=
)

dax_string = '''
   EVALUATE
   CALCULATETABLE(inbound-emissions)
   '''

df = ssas_api.get_DAX(connection_string=conn, dax_string=dax_string)

username='32f1a596-ab1e-46ad-b25a-f97f00855c54'
password='tnKRcv7_5V-96o~InNXGx1k~Y73SDC_4O6'
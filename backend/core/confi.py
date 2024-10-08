import mysql.connector

mysql_confi = {
    'host': 'localhost',
    'user':'root',
    'database':'api',
    'auth_plugin':'mysql_native'
}
connetion = mysql.connector.connect(**mysql_confi)
def get_connetion():
    return connetion
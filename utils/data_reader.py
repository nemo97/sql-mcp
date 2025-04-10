import pymysql
import json
DATABASE_HOST = '127.0.0.1'
DATABASE_PORT = 3310  # 3306 Default MySQL port
DATABASE_USER = 'admidio'
DATABASE_PASSWORD = 'admidio'
DATABASE_NAME = 'admidio'
def db_search_booking(booking_number):    
    conn = pymysql.connect(host=DATABASE_HOST,
                           port=DATABASE_PORT,
                           user=DATABASE_USER, 
                           passwd=DATABASE_PASSWORD, db=DATABASE_NAME)
    cur = conn.cursor(pymysql.cursors.DictCursor)
    if(booking_number == "latest"):
        cur.execute("SELECT * FROM hotel_bookings BKG ORDER BY  `reservation_status_date` DESC LIMIT 0,10")
    else:    
        cur.execute("SELECT * FROM hotel_bookings BKG where `booking_nbr` = %s  LIMIT 0,10",(booking_number,))

    results = cur.fetchall()
    #print(json.dumps(results))
    # for r in cur:
    #     print(json.dumps(r, default=str))
    #     print(r[0])
    cur.close()
    conn.close()
    return results
# def db_search_booking_ref(booking_reference_number):    
#     conn = pymysql.connect(host=DATABASE_HOST, user=DATABASE_USER, passwd=DATABASE_PASSWORD, db=DATABASE_NAME)
#     cur = conn.cursor(pymysql.cursors.DictCursor)
#     cur.execute("SELECT * FROM gbb_booking_mt BKG where `shipment_number` = %s  LIMIT 0,10",(booking_number,))
#     results = cur.fetchall()
#     #print(json.dumps(results))
#     # for r in cur:
#     #     print(json.dumps(r, default=str))
#     #     print(r[0])
#     cur.close()
#     conn.close()
#     return results

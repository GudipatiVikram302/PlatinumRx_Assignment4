import sqlite3
import os

sql_file_path = os.path.join('sql', 'hotel.sql')

conn = sqlite3.connect('hotel.db')
cursor = conn.cursor()

with open(sql_file_path, 'r') as f:
    sql_script = f.read()

cursor.executescript(sql_script)

print("Database setup completed.\n")

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables:", cursor.fetchall())

print("\nQ1")
cursor.execute("""
SELECT b.user_id, b.room_no
FROM bookings b
JOIN (
    SELECT user_id, MAX(booking_date) AS last_date
    FROM bookings
    GROUP BY user_id
) t
ON b.user_id = t.user_id AND b.booking_date = t.last_date;
""")
for row in cursor.fetchall():
    print(row)

print("\nQ2")
cursor.execute("""
SELECT bc.booking_id,
       SUM(bc.item_quantity * i.item_rate) AS total_amount
FROM booking_commercials bc
JOIN items i ON bc.item_id = i.item_id
WHERE strftime('%m', bc.bill_date) = '11'
GROUP BY bc.booking_id;
""")
for row in cursor.fetchall():
    print(row)

print("\nQ3")
cursor.execute("""
SELECT bc.bill_id,
       SUM(bc.item_quantity * i.item_rate) AS total_amount
FROM booking_commercials bc
JOIN items i ON bc.item_id = i.item_id
GROUP BY bc.bill_id
HAVING total_amount > 1000;
""")
for row in cursor.fetchall():
    print(row)

print("\nQ4")
cursor.execute("""
WITH item_counts AS (
    SELECT strftime('%m', bill_date) AS month,
           item_id,
           SUM(item_quantity) AS total_qty
    FROM booking_commercials
    GROUP BY month, item_id
),
ranked AS (
    SELECT *,
           RANK() OVER (PARTITION BY month ORDER BY total_qty DESC) AS r_high,
           RANK() OVER (PARTITION BY month ORDER BY total_qty ASC) AS r_low
    FROM item_counts
)
SELECT * FROM ranked
WHERE r_high = 1 OR r_low = 1;
""")
for row in cursor.fetchall():
    print(row)

print("\nQ5")
cursor.execute("""
WITH bill_totals AS (
    SELECT strftime('%m', bill_date) AS month,
           bill_id,
           SUM(item_quantity * i.item_rate) AS total
    FROM booking_commercials bc
    JOIN items i ON bc.item_id = i.item_id
    GROUP BY month, bill_id
),
ranked AS (
    SELECT *,
           RANK() OVER (PARTITION BY month ORDER BY total DESC) AS rnk
    FROM bill_totals
)
SELECT * FROM ranked
WHERE rnk = 2;
""")
for row in cursor.fetchall():
    print(row)

conn.close()
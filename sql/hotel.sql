-- RESET
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS booking_commercials;

-- CREATE TABLES

CREATE TABLE users (
    user_id TEXT,
    name TEXT
);

CREATE TABLE bookings (
    booking_id TEXT,
    booking_date TEXT,
    room_no TEXT,
    user_id TEXT
);

CREATE TABLE items (
    item_id TEXT,
    item_name TEXT,
    item_rate INTEGER
);

CREATE TABLE booking_commercials (
    id TEXT,
    booking_id TEXT,
    bill_id TEXT,
    bill_date TEXT,
    item_id TEXT,
    item_quantity REAL
);

-- INSERT DATA

INSERT INTO users VALUES ('U1','John');
INSERT INTO users VALUES ('U2','Alice');

INSERT INTO bookings VALUES ('B1','2021-11-10','R1','U1');
INSERT INTO bookings VALUES ('B2','2021-11-15','R2','U2');

INSERT INTO items VALUES ('I1','Food',100);
INSERT INTO items VALUES ('I2','Drink',50);

INSERT INTO booking_commercials VALUES ('1','B1','BL1','2021-11-10','I1',2);
INSERT INTO booking_commercials VALUES ('2','B1','BL1','2021-11-10','I2',1);
INSERT INTO booking_commercials VALUES ('3','B2','BL2','2021-11-15','I1',5);
CREATE USER 'alx_travel_user'@'localhost' IDENTIFIED BY 'alx_travel_pwd';
GRANT ALL PRIVILEGES ON alx_travel_db.* TO 'alx_travel_user'@'localhost';
FLUSH PRIVILEGES;
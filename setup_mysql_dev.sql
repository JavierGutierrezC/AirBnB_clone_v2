-- beauty comment for the fucking holberton
CREATE DATA BASE IF NOT EXISTS hbnb_dev_db;
CREATE IF NOT EXISTS USER 'hbnb_dev@localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';


-- Creating the database
CREATE DATABASE TMS;
USE TMS;

-- Creating relations
CREATE TABLE COMPANY(
	COMPANY_ID INT AUTO_INCREMENT,
	COMPANY_NAME VARCHAR(20) NOT NULL,
	EMAIL_ID VARCHAR(25) NOT NULL,
    CONTACT_DETAILS INT NOT NULL,
    STREET VARCHAR(20) NOT NULL,
    CITY VARCHAR(15) NOT NULL,
    ZIPCODE INT(6),
    CONSTRAINT PK_COMPANY PRIMARY KEY(COMPANY_ID));
    
    SELECT * FROM COMPANY;
    
CREATE TABLE CUSTOMER(
	CUSTOMER_ID INT AUTO_INCREMENT,
    CUSTOMER_NAME VARCHAR(20) NOT NULL,
    EMAIL_ID VARCHAR(25) NOT NULL,
    CUSTOMER_PASSWORD VARCHAR(30) NOT NULL,
    GENDER CHAR(1),
    DOB DATE,
    STREET VARCHAR(20),
    CITY VARCHAR(15),
    ZIPCODE INT(6),
    CONTACT_DETAILS INT,
    CREDIT_POINTS INT DEFAULT 0,
    CONSTRAINT PK_CUSTOMER PRIMARY KEY(CUSTOMER_ID),
    CONSTRAINT UC_CUSTOMER UNIQUE(EMAIL_ID),
    CONSTRAINT CHK_CUSTOMER CHECK(GENDER IN ('M', 'F', 'T')));
    select * from CUSTOMER;
    
    CALL UPDATE_CUST_DETAILS(4, 'Naitik', 'new1', 'test', '2000-01-01', 'Gali-sim-sim', 'new', 313324, 90909);
    
    insert into customer(CUSTOMER_NAME, EMAIL_ID, CUSTOMER_PASSWORD, GENDER, 
    DOB, STREET, CITY, ZIPCODE, CONTACT_DETAILS, CREDIT_POINTS) values('Naitik', 'parmar@gmail.com', 'test', 'M', '2000-01-01','new', 'Kankroli',313324, 9414174, 12);
CREATE TABLE SYS_ADMIN(
	ADMIN_ID INT AUTO_INCREMENT,
    ADMIN_NAME VARCHAR(20) NOT NULL,
    EMAIL_ID VARCHAR(25) NOT NULL,
    ADMIN_PASSWORD VARCHAR(30) NOT NULL,
    GENDER CHAR(1),
    DOB DATE,
    STREET VARCHAR(20),
    CITY VARCHAR(15),
    ZIPCODE INT(6),
    CONTACT_DETAILS INT,
    HIRE_DATE DATE,
    CONSTRAINT PK_ADMIN PRIMARY KEY(ADMIN_ID),
    CONSTRAINT UC_ADMIN UNIQUE(EMAIL_ID),
    CONSTRAINT CHK_ADMIN CHECK(GENDER IN ('M', 'F', 'T')));
    INSERT INTO SYS_ADMIN(ADMIN_NAME, EMAIL_ID, ADMIN_PASSWORD, GENDER,
    DOB, STREET, CITY, ZIPCODE, CONTACT_DETAILS, HIRE_DATE) 
    VALUES('admin', 'admin@gmail.com', 'admin', 'M', '2000-02-03', 'New lane', 'Pune', 411004, 1111122222, '2020-09-11');
    
CREATE TABLE CITY(
	CITY_CODE VARCHAR(10),
    CITY_NAME VARCHAR(15) NOT NULL,
    ZIPCODE INT(6),
    BOARDING_POINT VARCHAR(50) NOT NULL,
    CONSTRAINT PK_CITY PRIMARY KEY(CITY_CODE));
SELECT * FROM CITY;

CREATE TABLE AMENITIES(
	AMENITY_ID INT AUTO_INCREMENT,
    AMENITY_SET VARCHAR(40),
    CONSTRAINT PK_AMENITY PRIMARY KEY(AMENITY_ID));
    SELECT * FROM amenities;
    
CREATE TABLE ROUTE(
	ROUTE_ID INT AUTO_INCREMENT,
    START_CITY VARCHAR(10),
    DEST_CITY VARCHAR(10),
    TIME_TAKEN TIME NOT NULL,
    CONSTRAINT PK_ROUTE PRIMARY KEY(ROUTE_ID),
    CONSTRAINT FK1_ROUTE FOREIGN KEY(START_CITY) REFERENCES CITY(CITY_CODE) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT FK2_ROUTE FOREIGN KEY(DEST_CITY) REFERENCES CITY(CITY_CODE) ON DELETE CASCADE ON UPDATE CASCADE);  
    SELECT * FROM ROUTE;
    DELETE FROM ROUTE WHERE ROUTE_ID=1;
CREATE TABLE VEHICLE(
	VEHICLE_ID VARCHAR(10),
    MODEL_NAME VARCHAR(20) NOT NULL,
    START_TIME TIME NOT NULL,
	PRICE FLOAT NOT NULL,
    RATING DECIMAL(2,1),
    ROUTE_ID INT,
	COMPANY_ID INT,
    AMENITY_ID INT,
    CONSTRAINT PK_VEHICLE PRIMARY KEY(VEHICLE_ID),
    CONSTRAINT FK1_VEHICLE FOREIGN KEY(ROUTE_ID) REFERENCES ROUTE(ROUTE_ID) ON DELETE SET NULL ON UPDATE CASCADE,
    CONSTRAINT FK2_VEHICLE FOREIGN KEY(COMPANY_ID) REFERENCES COMPANY(COMPANY_ID) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT FK3_VEHICLE FOREIGN KEY(AMENITY_ID) REFERENCES AMENITIES(AMENITY_ID) ON DELETE SET NULL ON UPDATE CASCADE);
    DELETE FROM VEHICLE WHERE VEHICLE_ID = 1;
    SELECT * FROM VEHICLE;

CREATE TABLE BUS(
	VEHICLE_ID VARCHAR(10),
    NO_OF_SLEEPER_SEATS INT NOT NULL,
    NO_OF_SEATER_SEATS INT NOT NULL,
    CONSTRAINT PK_BUS PRIMARY KEY(VEHICLE_ID),
    CONSTRAINT FK_BUS FOREIGN KEY(VEHICLE_ID) REFERENCES VEHICLE(VEHICLE_ID) ON DELETE CASCADE ON UPDATE CASCADE);
    SELECT* FROM BUS;
    
CREATE TABLE CAR(
	VEHICLE_ID VARCHAR(10),
    NO_OF_SEATS INT NOT NULL,
    CONSTRAINT PK_CAR PRIMARY KEY(VEHICLE_ID),
    CONSTRAINT FK_CAR FOREIGN KEY(VEHICLE_ID) REFERENCES VEHICLE(VEHICLE_ID) ON DELETE CASCADE ON UPDATE CASCADE);
    
CREATE TABLE FLIGHT(
	VEHICLE_ID VARCHAR(10),
    NO_OF_FIRSTCLASS_SEATS INT NOT NULL,
    NO_OF_ECONOMY_SEATS INT NOT NULL,
    NO_OF_BUSINESS_SEATS INT NOT NULL,
    NO_OF_PREMIUM_SEATS INT NOT NULL,
    CONSTRAINT PK_FLIGHT PRIMARY KEY(VEHICLE_ID),
    CONSTRAINT FK_FLIGHT FOREIGN KEY(VEHICLE_ID) REFERENCES VEHICLE(VEHICLE_ID) ON DELETE CASCADE ON UPDATE CASCADE);
    
CREATE TABLE EMPLOYEE(
	EMP_ID INT AUTO_INCREMENT,
    EMP_NAME VARCHAR(20) NOT NULL,
    GENDER CHAR(1),
    SALARY FLOAT,
    AADHAAR_NO INT(12) NOT NULL,
    EMAIL_ID VARCHAR(25),
    CONTACT_DETAILS INT(10) NOT NULL,
    DOB DATE,
    STREET VARCHAR(20) NOT NULL,
    CITY VARCHAR(15) NOT NULL,
    ZIPCODE INT(6),
    EMP_ROLE VARCHAR(15),
    MGR_ID INT,
    VEHICLE_ID VARCHAR(10),
    COMPANY_ID INT,
    CONSTRAINT PK_EMPLOYEE PRIMARY KEY(EMP_ID),
    CONSTRAINT FK1_EMPLOYEE FOREIGN KEY(MGR_ID) REFERENCES EMPLOYEE(EMP_ID) ON DELETE SET NULL ON UPDATE CASCADE,
	CONSTRAINT FK2_EMPLOYEE FOREIGN KEY(VEHICLE_ID) REFERENCES VEHICLE(VEHICLE_ID) ON DELETE SET NULL ON UPDATE CASCADE,
    CONSTRAINT FK3_EMPLOYEE FOREIGN KEY(COMPANY_ID) REFERENCES COMPANY(COMPANY_ID) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT UC_EMPLOYEE UNIQUE(EMAIL_ID),
    CONSTRAINT CHK1_EMPLOYEE CHECK(GENDER IN ('M', 'F', 'T')));
    
CREATE TABLE JOURNEY_CAR(
	JOURNEY_ID INT AUTO_INCREMENT,
    JOURNEY_DATE DATE NOT NULL, 
    AVAILABLE_SEATS INT NOT NULL,
    VEHICLE_ID VARCHAR(10),
    JOURNEY_STATUS INT DEFAULT 1,
    CONSTRAINT PK_JOURNEY_CAR PRIMARY KEY(JOURNEY_ID),
    CONSTRAINT FK_JOURNEY_CAR FOREIGN KEY(VEHICLE_ID) REFERENCES VEHICLE(VEHICLE_ID) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT CHK_JOURNEY_CAR CHECK(JOURNEY_STATUS IN (0, 1)));
    
CREATE TABLE JOURNEY_BUS(
	JOURNEY_ID INT AUTO_INCREMENT,
    JOURNEY_DATE DATE NOT NULL, 
    AVAILABLE_SLEEPER_SEATS INT NOT NULL,
	AVAILABLE_SEATER_SEATS INT NOT NULL,
    VEHICLE_ID VARCHAR(10),
    CONSTRAINT PK_JOURNEY_BUS PRIMARY KEY(JOURNEY_ID),
    CONSTRAINT FK_JOURNEY_BUS FOREIGN KEY(VEHICLE_ID) REFERENCES VEHICLE(VEHICLE_ID) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT CHK_JOURNEY_BUS CHECK(JOURNEY_STATUS IN (0, 1)));
    
CREATE TABLE JOURNEY_FLIGHT(
	JOURNEY_ID INT AUTO_INCREMENT,
    JOURNEY_DATE DATE NOT NULL, 
    AVAILABLE_FIRSTCLASS_SEATS INT NOT NULL,
	AVAILABLE_ECONOMY_SEATS INT NOT NULL,
    AVAILABLE_BUSINESS_SEATS INT NOT NULL,
    AVAILABLE_PREMIUM_SEATS INT NOT NULL,
    VEHICLE_ID VARCHAR(10),
    JOURNEY_STATUS INT DEFAULT 1,
    CONSTRAINT PK_JOURNEY_FLIGHT PRIMARY KEY(JOURNEY_ID),
    CONSTRAINT FK_JOURNEY_FLIGHT FOREIGN KEY(VEHICLE_ID) REFERENCES VEHICLE(VEHICLE_ID) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT CHK_JOURNEY_FLIGHT CHECK(JOURNEY_STATUS IN (0, 1)));
    
CREATE TABLE BOOKS_CAR(
	JOURNEY_ID INT,
    CUSTOMER_ID INT,
    DATE_OF_BOOKING DATE NOT NULL,
    PRICE FLOAT,
    CONSTRAINT PK_BOOKS_CAR PRIMARY KEY(JOURNEY_ID, CUSTOMER_ID, DATE_OF_BOOKING),
    CONSTRAINT FK1_BOOKS_CAR FOREIGN KEY(JOURNEY_ID) REFERENCES  JOURNEY_CAR(JOURNEY_ID) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT FK2_BOOKS_CAR FOREIGN KEY(CUSTOMER_ID) REFERENCES  CUSTOMER(CUSTOMER_ID) ON DELETE CASCADE ON UPDATE CASCADE);
    
CREATE TABLE BOOKS_BUS(
	JOURNEY_ID INT,
    CUSTOMER_ID INT,
    DATE_OF_BOOKING DATE NOT NULL,
	PRICE FLOAT,
    SEAT_TYPE VARCHAR(15),
    SEAT_NO VARCHAR(10),
    CONSTRAINT PK_BOOKS_BUS PRIMARY KEY(JOURNEY_ID, CUSTOMER_ID, DATE_OF_BOOKING),
    CONSTRAINT FK1_BOOKS_BUS FOREIGN KEY(JOURNEY_ID) REFERENCES  JOURNEY_BUS(JOURNEY_ID) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT FK2_BOOKS_BUS FOREIGN KEY(CUSTOMER_ID) REFERENCES  CUSTOMER(CUSTOMER_ID) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT CHK_BOOKS_BUS CHECK(SEAT_TYPE IN ('SLEEPER', 'SEATER')));
 
CREATE TABLE BOOKS_FLIGHT(
	JOURNEY_ID INT,
    CUSTOMER_ID INT,
    DATE_OF_BOOKING DATE NOT NULL,
	PRICE FLOAT,
    SEAT_TYPE VARCHAR(15),
    SEAT_NO VARCHAR(10),
    CONSTRAINT PK_BOOKS_FLIGHT PRIMARY KEY(JOURNEY_ID, CUSTOMER_ID, DATE_OF_BOOKING),
    CONSTRAINT FK1_BOOKS_FLIGHT FOREIGN KEY(JOURNEY_ID) REFERENCES  JOURNEY_FLIGHT(JOURNEY_ID) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT FK2_BOOKS_FLIGHT FOREIGN KEY(CUSTOMER_ID) REFERENCES  CUSTOMER(CUSTOMER_ID) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT CHK_BOOKS_FLIGHT CHECK(SEAT_TYPE IN ('FIRSTCLASS', 'ECONOMY', 'BUSINESS', 'PREMIUM')));

-- Checking created tables
SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'TMS';


-- DROP DATABASE TMS;

    
    
    
    
   
	
    
    

    
    

    
    
    
    
    
    
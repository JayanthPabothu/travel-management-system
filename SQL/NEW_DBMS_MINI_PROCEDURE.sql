USE FMS;

DELIMITER $$

CREATE PROCEDURE CHECK_IF_CUSTOMER_EXISTS(IN EMAIL VARCHAR(25), OUT E_STATUS INT)
BEGIN
		SELECT EXISTS(SELECT EMAIL_ID FROM CUSTOMER WHERE EMAIL = EMAIL_ID) INTO E_STATUS;
END $$

-- ----------------------------------------------------------------

CREATE PROCEDURE INSERT_CUSTOMER(IN NEW_CUSTOMER_NAME VARCHAR(20), IN NEW_EMAIL_ID VARCHAR(25),
									IN NEW_CUSTOMER_PASSWORD VARCHAR(30), IN NEW_GENDER CHAR(1), IN NEW_DOB DATE,
                                    IN NEW_STREET VARCHAR(20), IN NEW_CITY VARCHAR(15), IN NEW_ZIPCODE INT(6), IN NEW_CONTACT_DETAILS BIGINT)
BEGIN
	INSERT INTO CUSTOMER(CUSTOMER_NAME, EMAIL_ID, CUSTOMER_PASSWORD, GENDER, DOB, STREET, CITY, ZIPCODE, CONTACT_DETAILS)
    VALUES(NEW_CUSTOMER_NAME, NEW_EMAIL_ID, NEW_CUSTOMER_PASSWORD, NEW_GENDER, NEW_DOB, NEW_STREET, NEW_CITY, NEW_ZIPCODE, NEW_CONTACT_DETAILS);
END $$

-- ----------------------------------------------------------------

CREATE PROCEDURE UPDATE_CUST_DETAILS(IN CUST_ID INT, IN NEW_CUSTOMER_NAME VARCHAR(20), IN NEW_EMAIL_ID VARCHAR(25),
									IN NEW_CUSTOMER_PASSWORD VARCHAR(30), IN NEW_DOB DATE,
                                    IN NEW_STREET VARCHAR(20), IN NEW_CITY VARCHAR(15), IN NEW_ZIPCODE INT(6), IN NEW_CONTACT_DETAILS BIGINT)
BEGIN
	UPDATE CUSTOMER
    SET 
		CUSTOMER_NAME = NEW_CUSTOMER_NAME,
        EMAIL_ID = NEW_EMAIL_ID,
        CUSTOMER_PASSWORD = NEW_CUSTOMER_PASSWORD,
        DOB = NEW_DOB,
        STREET = NEW_STREET,
        CITY = NEW_CITY,
        ZIPCODE = NEW_ZIPCODE,
        CONTACT_DETAILS = NEW_CONTACT_DETAILS
	WHERE 
		CUSTOMER_ID = CUST_ID;
END $$

-- ---------------------------------------------------------------

CREATE PROCEDURE CHECK_IF_COMPANY_EXISTS(IN COMP_NAME VARCHAR(25), OUT E_STATUS INT)
BEGIN
		SELECT EXISTS(SELECT COMPANY_NAME FROM COMPANY WHERE COMP_NAME = COMPANY_NAME) INTO E_STATUS;
END $$

-- ----------------------------------------------------------------

CREATE PROCEDURE INSERT_COMPANY(IN NEW_COMPANY_NAME VARCHAR(20), IN NEW_EMAIL_ID VARCHAR(25),
								IN NEW_CONTACT_DETAILS BIGINT, IN NEW_STREET VARCHAR(20), IN NEW_CITY VARCHAR(15), IN NEW_ZIPCODE INT(6))
BEGIN
	INSERT INTO COMPANY(COMPANY_NAME, EMAIL_ID, CONTACT_DETAILS, STREET, CITY, ZIPCODE)
    VALUES(NEW_COMPANY_NAME, NEW_EMAIL_ID, NEW_CONTACT_DETAILS, NEW_STREET, NEW_CITY, NEW_ZIPCODE);
END $$

-- -----------------------------------------------------------------

CREATE PROCEDURE UPDATE_COMPANY_DETAILS(IN COMP_ID INT, IN NEW_COMPANY_NAME VARCHAR(20), IN NEW_EMAIL_ID VARCHAR(25),
								IN NEW_CONTACT_DETAILS BIGINT, IN NEW_STREET VARCHAR(20), IN NEW_CITY VARCHAR(15), IN NEW_ZIPCODE INT(6))
BEGIN
	UPDATE COMPANY
    SET 
		COMPANY_NAME = NEW_COMPANY_NAME,
        EMAIL_ID = NEW_EMAIL_ID,
        CONTACT_DETAILS = NEW_CONTACT_DETAILS,
        STREET = NEW_STREET,
        CITY = NEW_CITY,
        ZIPCODE = NEW_ZIPCODE
	WHERE 
		COMPANY_ID = COMP_ID;
END $$

-- -------------------------------------------------------------------

CREATE PROCEDURE DELETE_COMPANY_DETAILS(IN OLD_COMP_NAME VARCHAR(20))
BEGIN
	DELETE FROM COMPANY
    WHERE COMPANY_NAME = OLD_COMP_NAME;
END $$

-- -------------------------------------------------------------------

CREATE PROCEDURE CHECK_IF_ADMIN_EXISTS(IN EMAIL VARCHAR(25), OUT E_STATUS INT)
BEGIN
		SELECT EXISTS(SELECT EMAIL_ID FROM SYS_ADMIN WHERE EMAIL = EMAIL_ID) INTO E_STATUS;
END $$

-- -------------------------------------------------------------------

CREATE PROCEDURE INSERT_ADMIN(IN NEW_ADMIN_NAME VARCHAR(20), IN NEW_EMAIL_ID VARCHAR(25),
									IN NEW_ADMIN_PASSWORD VARCHAR(30), IN NEW_GENDER CHAR(1), IN NEW_DOB DATE,
                                    IN NEW_STREET VARCHAR(20), IN NEW_CITY VARCHAR(15), IN NEW_ZIPCODE INT(6), IN NEW_CONTACT_DETAILS BIGINT)
BEGIN
	DECLARE NEW_HIRE_DATE DATE;
    SET NEW_HIRE_DATE = CURDATE();
	INSERT INTO SYS_ADMIN(ADMIN_NAME, EMAIL_ID, ADMIN_PASSWORD, GENDER, DOB, STREET, CITY, ZIPCODE, CONTACT_DETAILS, HIRE_DATE)
    VALUES(NEW_ADMIN_NAME, NEW_EMAIL_ID, NEW_ADMIN_PASSWORD, NEW_GENDER, NEW_DOB, NEW_STREET, NEW_CITY, NEW_ZIPCODE, NEW_CONTACT_DETAILS, NEW_HIRE_DATE);
END $$

-- --------------------------------------------------------------------

CREATE PROCEDURE UPDATE_ADMIN_DETAILS(IN AD_ID INT, IN NEW_ADMIN_NAME VARCHAR(20), IN NEW_ADMIN_ID VARCHAR(25),
									IN NEW_ADMIN_PASSWORD VARCHAR(30), IN NEW_DOB DATE,
                                    IN NEW_STREET VARCHAR(20), IN NEW_CITY VARCHAR(15), IN NEW_ZIPCODE INT(6), IN NEW_CONTACT_DETAILS INT(10))
BEGIN
	UPDATE SYS_ADMIN
    SET 
		ADMIN_NAME = NEW_ADMIN_NAME,
        EMAIL_ID = NEW_EMAIL_ID,
        AMDIN_PASSWORD = NEW_ADMIN_PASSWORD,
        DOB = NEW_DOB,
        STREET = NEW_STREET,
        CITY = NEW_CITY,
        ZIPCODE = NEW_ZIPCODE,
        ADMIN_DETAILS = NEW_ADMIN_DETAILS
	WHERE 
		ADMIN_ID = AD_ID;
END $$

-- ---------------------------------------------------------------------

CREATE PROCEDURE DELETE_ADMIN_DETAILS(IN OLD_AD_ID VARCHAR(20))
BEGIN
	DELETE FROM SYS_ADMIN
    WHERE ADMIN_ID = OLD_AD_ID;
END $$

-- ----------------------------------------------------------------------

CREATE PROCEDURE CHECK_IF_CITY_EXISTS(IN NEW_CITY_CODE VARCHAR(10), IN NEW_CITY_NAME VARCHAR(15), IN NEW_AIRPORT VARCHAR(50), OUT E_STATUS INT)
BEGIN
		SELECT EXISTS(SELECT * FROM CITY WHERE CITY_CODE = NEW_CITY_CODE AND CITY_NAME = NEW_CITY_NAME AND NEW_AIRPORT = AIRPORT) INTO E_STATUS;
END $$

-- ----------------------------------------------------------------------

CREATE PROCEDURE INSERT_CITY_DETAILS(IN NEW_CITY_CODE VARCHAR(10), IN NEW_CITY_NAME VARCHAR(15), IN NEW_ZIPCODE INT(6), IN NEW_AIRPORT VARCHAR(50))
BEGIN
	INSERT INTO CITY
	VALUES (NEW_CITY_CODE, NEW_CITY_NAME, NEW_ZIPCODE, NEW_AIRPORT);
END $$

-- ----------------------------------------------------------------------

CREATE PROCEDURE UPDATE_CITY_DETAILS(IN OLD_CITY_CODE VARCHAR(10), IN NEW_CITY_CODE VARCHAR(10), IN NEW_CITY_NAME VARCHAR(15), IN NEW_ZIPCODE INT(6), IN NEW_AIRPORT VARCHAR(50))
BEGIN
	UPDATE CITY
	SET
		CITY_CODE = NEW_CITY_CODE,
		CITY_NAME = NEW_CITY_NAME,
		ZIPCODE = NEW_ZIPCODE,
		AIRPORT = NEW_AIRPORT
    WHERE
		CITY_CODE = OLD_CITY_CODE;
END $$

-- ---------------------------------------------------------------------

CREATE PROCEDURE DELETE_CITY_BY_AIRPORT(IN OLD_AIRPORT VARCHAR(50))
BEGIN
	DELETE FROM CITY
    WHERE AIRPORT = OLD_AIRPORT;
END $$

-- ---------------------------------------------------------------------

CREATE PROCEDURE DELETE_CITY_BY_NAME(IN OLD_CITY_NAME VARCHAR(50))
BEGIN
	DELETE FROM CITY
    WHERE CITY_NAME = OLD_CITY_NAME;
END $$

-- --------------------------------------------------------------------

CREATE PROCEDURE CHECK_IF_ROUTE_EXISTS(IN START_CITY_CODE VARCHAR(10), IN DEST_CITY_CODE VARCHAR(10), OUT E_STATUS INT)
BEGIN
		SELECT EXISTS(SELECT * FROM ROUTE WHERE START_CITY = START_CITY_CODE AND DEST_CITY = DEST_CITY_CODE) INTO E_STATUS;
END $$

-- ----------------------------------------------------------------------

CREATE PROCEDURE INSERT_ROUTE(IN SOURCE_CITY VARCHAR(10), IN DESTINATION_CITY VARCHAR(10), IN FLIGHT_TIME TIME)
BEGIN
	INSERT INTO ROUTE(START_CITY, DEST_CITY, TIME_TAKEN)
    VALUES (SOURCE_CITY, DESTINATION_CITY, FLIGHT_TIME);
END $$

-- --------------------------------------------------------------------

CREATE PROCEDURE UPDATE_ROUTE(IN SOURCE_CITY VARCHAR(10), IN DESTINATION_CITY VARCHAR(10), IN FLIGHT_TIME TIME)
BEGIN
	UPDATE CITY
    SET 
		TIME_TAKEN = FLIGHT_TIME
	WHERE
		SOURCE_CITY = START_CITY AND DESTINATION_CITY = DEST_CITY;
END $$

-- --------------------------------------------------------------------

CREATE PROCEDURE DELETE_ROUTE(IN SOURCE_CITY VARCHAR(10), IN DESTINATION_CITY VARCHAR(10))
BEGIN
	DELETE FROM ROUTE
    WHERE START_CITY = SOURCE_CITY AND DEST_CITY = DESTINATION_CITY;
END $$

-- ---------------------------------------------------------------------

CREATE PROCEDURE CHECK_IF_FLIGHT_EXISTS(IN FLIGHT_ID VARCHAR(10), OUT E_STATUS INT)
BEGIN
		SELECT EXISTS(SELECT FLIGHT_NO FROM FLIGHT WHERE FLIGHT_NO = FLIGHT_ID) INTO E_STATUS;
END $$

-- ---------------------------------------------------------------------

CREATE PROCEDURE INSERT_FLIGHT_DETAILS(IN FLIGHT_ID VARCHAR(10), IN START_TIME TIME, IN ROUTE_NO INT, IN TERMINAL INT, IN COST FLOAT, 
									   IN BAGGAGE_WEIGHT INT, IN FIRSTCLASS INT, IN ECONOMY INT, IN BUSINESS INT, IN PREMIUM INT, IN COMP_ID INT)
BEGIN
	INSERT INTO FLIGHT
    VALUES (FLIGHT_ID, START_TIME, ROUTE_NO, TERMINAL, COST, BAGGAGE_WEIGHT, FIRSTCLASS, ECONOMY, BUSINESS, PREMIUM, COMP_ID);
END $$

-- ---------------------------------------------------------------------

CREATE PROCEDURE UPDATE_FLIGHT_DETAILS(IN FLIGHT_ID VARCHAR(10), IN START_TIME TIME, IN ROUTE_NO INT, IN TERMINAL INT, IN COST FLOAT, 
									   IN BAGGAGE_WEIGHT INT, IN COMP_ID INT)
BEGIN
	UPDATE FLIGHT
    SET
		DEPARTURE_TIME = START_TIME,
        ROUTE_ID= ROUTE_NO,
        TERMINAL_NO = TERMINAL,
        PRICE = COST,
        BAGGAGE_ALLOWANCE = BAGGAGE_WEIGHT,
        NO_OF_FIRSTCLASS_SEATS = FIRSTCLASS,
        NO_OF_ECONOMY_SEATS = ECONOMY,
        NO_OF_BUSINESS_SEATS = BUSINESS,
        NO_OF_PREMIUM_SEATS = PREMIUM,
        COMPANY_ID = COMP_ID
	WHERE
		FLIGHT_NO = FLIGHT_ID;
END $$

-- --------------------------------------------------------------------

CREATE PROCEDURE DELETE_FLIGHT(IN FLIGHT_ID VARCHAR(10))
BEGIN
	DELETE FROM FLIGHT
    WHERE FLIGHT_NO = FLIGHT_ID;
END $$

-- ---------------------------------------------------------------------

CREATE PROCEDURE UPDATE_PRICE_FACTOR(IN FIRSTCLASS FLOAT, IN ECONOMY FLOAT, IN BUSINESS FLOAT, IN PREMIUM FLOAT)
BEGIN
	UPDATE PRICE_FACTOR
    SET 
		FIRSTCLASS_FACTOR = FIRSTCLASS,
        ECONOMY_FACTOR = ECONOMY,
        BUSINESS_FACTOR = BUSINESS,
        PREMIUM_FACTOR = PREMIUM;
END $$

-- ---------------------------------------------------------------------

CREATE PROCEDURE CHECK_IF_JOURNEY_EXISTS(IN FLIGHT_ID VARCHAR(10), IN JOURNEYDATE DATE, OUT E_STATUS INT)
BEGIN
		SELECT EXISTS(SELECT * FROM JOURNEY_FLIGHT WHERE FLIGHT_NO = FLIGHT_ID AND JOURNEY_DATE = JOURNEYDATE) INTO E_STATUS;
END $$

-- ---------------------------------------------------------------------

CREATE PROCEDURE INSERT_JOURNEY_DETAILS(IN JOURNEYDATE DATE, IN FLIGHT_ID VARCHAR(10))
BEGIN
	DECLARE FIRSTCLASS INT;
    DECLARE ECONOMY INT;
    DECLARE BUSINESS INT;
    DECLARE PREMIUM INT;
    
    SELECT NO_OF_FIRSTCLASS_SEATS, NO_OF_ECONOMY_SEATS, NO_OF_BUSINESS_SEATS, NO_OF_PREMIUM_SEATS 
    INTO FIRSTCLASS, ECONOMY, BUSINESS, PREMIUM
    FROM FLIGHT 
    WHERE FLIGHT_NO = FLIGHT_ID;
    
	INSERT INTO JOURNEY_FLIGHT(JOURNEY_DATE, AVAILABLE_FIRSTCLASS_SEATS, AVAILABLE_ECONOMY_SEATS, AVAILABLE_BUSINESS_SEATS, AVAILABLE_PREMIUM_SEATS, FLIGHT_NO)
    VALUES ( JOURNEYDATE, FIRSTCLASS, ECONOMY, BUSINESS, PREMIUM, FLIGHT_ID);
END $$

-- ------------------------------------------------------------------------
		
CREATE PROCEDURE CHANGE_JOURNEY_STATUS(IN JOURNEY INT, IN STAT INT)
BEGIN
	UPDATE JOURNEY_FLIGHT
    SET
		JOURNEY_STATUS = STAT
	WHERE 
		JOUNEY_ID = JOURNEY;
END $$

-- -----------------------------------------------------------------------

CREATE PROCEDURE FETCH_JOURNEY_ID( IN JOURNEYDATE DATE, IN FLIGHTID INT, OUT ID INT)
BEGIN
	SELECT JOURNEY_ID INTO ID
    FROM JOURNEY_FLIGHT
    WHERE FLIGHT_NO = FLIGHTID AND JOURNEY_DATE = JOURNEYDATE;
END $$

-- ------------------------------------------------------------------------ 

CREATE PROCEDURE INSERT_FLIGHT_BOOKING(IN JOURNEYID INT, IN CUST_ID INT, IN COST FLOAT, 
										IN SEATTYPE VARCHAR(15), IN SEAT VARCHAR(10))
BEGIN
	DECLARE BOOKING_DATE DATE;
    SET BOOKING_DATE = CURDATE();
	INSERT INTO BOOKS_FLIGHT
    VALUES (JOURNEYID, CUST_ID, BOOKING_DATE, COST, SEATTYPE, SEAT);
END $$

        






    



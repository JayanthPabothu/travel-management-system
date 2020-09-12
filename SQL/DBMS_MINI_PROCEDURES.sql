USE TMS;

DELIMITER $$
CREATE PROCEDURE UPDATE_CUST_DETAILS(IN CUST_ID INT, IN NEW_CUSTOMER_NAME VARCHAR(20), IN NEW_EMAIL_ID VARCHAR(25),
									IN NEW_CUSTOMER_PASSWORD VARCHAR(30), IN NEW_DOB DATE,
                                    IN NEW_STREET VARCHAR(20), IN NEW_CITY VARCHAR(15), IN NEW_ZIPCODE INT(6), IN NEW_CONTACT_DETAILS INT)
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






CREATE PROCEDURE UPDATE_ADMIN_DETAILS(IN AD_ID INT, IN NEW_ADMIN_NAME VARCHAR(20), IN NEW_ADMIN_ID VARCHAR(25),
									IN NEW_ADMIN_PASSWORD VARCHAR(30), IN NEW_GENDER CHAR(1), IN NEW_DOB DATE,
                                    IN NEW_STREET VARCHAR(20), IN NEW_CITY VARCHAR(15), IN NEW_ZIPCODE INT(6), IN NEW_CONTACT_DETAILS INT(10))
BEGIN
	UPDATE SYS_ADMIN
    SET 
		ADMIN_NAME = NEW_ADMIN_NAME,
        EMAIL_ID = NEW_EMAIL_ID,
        AMDIN_PASSWORD = NEW_ADMIN_PASSWORD,
        GENDER = NEW_GENDER,
        DOB = NEW_DOB,
        STREET = NEW_STREET,
        CITY = NEW_CITY,
        ZIPCODE = NEW_ZIPCODE,
        ADMIN_DETAILS = NEW_ADMIN_DETAILS
	WHERE 
		ADMIN_ID = AD_ID;
END $$




CREATE PROCEDURE INSERT_CAR(IN CAR_ID VARCHAR(10), IN MOD_NAME VARCHAR(20), IN START_T TIME, IN DAYS VARCHAR(50), IN ROUT_ID INT,
							IN CITY_HIERAR INT, IN COMP_ID INT, IN AMT_ID INT, IN SEATS INT)
BEGIN
	INSERT INTO VEHICLE(VEHICLE_ID, MODEL_NAME, START_TIME, DAY_SET, ROUTE_ID, CITY_HIERARCHY, COMPANY_ID, AMENITY_ID)
						VALUES (CAR_ID, MOD_NAME, START_T, DAYS, ROUT_ID, CITY_HIERAR, COMP_ID, AMT_ID);
	INSERT INTO CAR(VEHICLE_ID, NO_OF_SEATS) VALUES (CAR_ID, SEATS);
END $$




CREATE PROCEDURE INSERT_BUS(IN BUS_ID VARCHAR(10), IN MOD_NAME VARCHAR(20), IN START_T TIME, IN DAYS VARCHAR(50), IN ROUT_ID INT,
							IN CITY_HIERAR INT, IN COMP_ID INT, IN AMT_ID INT, IN SEAT_SEATS INT, IN SLEEP_SEATS INT)
BEGIN
	INSERT INTO VEHICLE(VEHICLE_ID, MODEL_NAME, START_TIME, DAY_SET, ROUTE_ID, CITY_HIERARCHY, COMPANY_ID, AMENITY_ID)
						VALUES (BUS_ID, MOD_NAME, START_T, DAYS, ROUT_ID, CITY_HIERAR, COMP_ID, AMT_ID);
	INSERT INTO BUS(VEHICLE_ID, NO_OF_SEATER_SEATS, NO_OF_SLEEPER_SEATS) VALUES (CAR_ID, SEAT_SEATS, SLEEP_SEATS);
END $$




CREATE PROCEDURE INSERT_FLIGHT(IN FLIGHT_ID VARCHAR(10), IN MOD_NAME VARCHAR(20), IN START_T TIME, IN DAYS VARCHAR(50), IN ROUT_ID INT,
							IN CITY_HIERAR INT, IN COMP_ID INT, IN AMT_ID INT, IN FIRST_SEATS INT, IN ECO_SEATS INT, IN BUSS_SEATS INT, IN PRE_SEATS INT)
BEGIN
	INSERT INTO VEHICLE(VEHICLE_ID, MODEL_NAME, START_TIME, DAY_SET, ROUTE_ID, CITY_HIERARCHY, COMPANY_ID, AMENITY_ID)
						VALUES (FLIGHT_ID, MOD_NAME, START_T, DAYS, ROUT_ID, CITY_HIERAR, COMP_ID, AMT_ID);
	INSERT INTO FLIGHT(VEHICLE_ID, NO_OF_FIRSTCLASS_SEATS, NO_OF_ECONOMY_SEATS, NO_OF_BUSINESS_SEATS, NO_OF_PREMIUM_SEATS) 
					VALUES (FLIGHT_ID, FIRST_SEATS, ECO_SEATS, BUSS_SEATS, PRE_SEATS);
END $$




CREATE PROCEDURE DELETE_VEHICLE(IN DELETE_VEHICLE_ID VARCHAR(10))
BEGIN
	DELETE FROM VEHICLE
	WHERE VEHICLE_ID = DELETE_VEHICLE_ID;
END $$




CREATE PROCEDURE UPDATE_VEHICLE(IN VEH_ID VARCHAR(10), IN START_T TIME, IN DAYS VARCHAR(50), IN ROUT_ID INT,
							IN CITY_HIERAR INT, IN COMP_ID INT, IN AMT_ID INT)
BEGIN
	UPDATE VEHICLE
    SET 
		START_TIME = START_T,
        DAY_SET = DAYS,
        ROUTE_ID = ROUT_ID,
        CITY_HIERARCHY = CITY_HIERAR,
        COMPANY_ID = COMP_ID,
        AMENITY_ID = AMT_ID
	WHERE 
		VEHICLE_ID = VEH_ID;
END $$

CREATE PROCEDURE CHECK_IF_EXISTS(IN EMAIL VARCHAR(25), OUT E_STATUS INT)
BEGIN
		SELECT EXISTS(SELECT EMAIL_ID FROM CUSTOMER WHERE EMAIL = EMAIL_ID) INTO E_STATUS;
END $$

CREATE PROCEDURE CHECK_ROUTE_EXISTS(IN START_C VARCHAR(10), IN DEST_C VARCHAR(10), IN TIME_T TIME, OUT STAT INT)
BEGIN
		SELECT EXISTS(SELECT * FROM ROUTE WHERE START_CITY = START_C AND DEST_CITY = DEST_C AND TIME_TAKEN = TIME_T)
        INTO STAT;


END $$

DELIMITER ;


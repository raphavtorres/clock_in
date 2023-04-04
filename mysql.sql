CREATE TABLE students (
    userID int NOT NULL,
    nameStudent varchar (255),
    presenceStudent int,
    absenceStudent int,
    lateStudent int,
    entrance int,
    exit_amount int,
    rfID varchar(255) NOT NULL,
    PRIMARY KEY (rfID)
);


CREATE TABLE entrance_table (
    idEntrance int NOT NULL AUTO_INCREMENT,
    entrance int,
    timeEntrace TIMESTAMP,
    rfID varchar (255),
    PRIMARY KEY (idEntrance),
    FOREIGN KEY (rfID) REFERENCES students(rfID)
);


CREATE TABLE exit_table (
    idExit int NOT NULL AUTO_INCREMENT,
    exit_amount int,
    timeExit TIMESTAMP,
    rfID varchar (255),
    PRIMARY KEY (idExit),
    FOREIGN KEY (rfID) REFERENCES students(rfID)
);

ALTER TABLE students ADD rfID varchar(255);


INSERT INTO entrance_table (timeEntrace, rfID)
VALUES ("{current_time}, {rfID}");

INSERT INTO exit_table (timeExit, rfID)
VALUES ("{current_time}, {rfID}");
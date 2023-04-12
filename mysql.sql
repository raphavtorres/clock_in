CREATE TABLE students (
    rfID varchar(100) NOT NULL,
    RAStudent int,
    nameStudent varchar (255),
    presenceStudent int,
    absenceStudent int,
    lateStudent int,
    PRIMARY KEY (rfID)
);


CREATE TABLE entrance_table (
    idEntrance int AUTO_INCREMENT,
    timeEntrance TIMESTAMP,
    rfID varchar (100),
    PRIMARY KEY (idEntrance),
    FOREIGN KEY (rfID) REFERENCES students(rfID)
);


CREATE TABLE exit_table (
    idExit int AUTO_INCREMENT,
    timeExit TIMESTAMP,
    rfID varchar (100),
    PRIMARY KEY (idExit),
    FOREIGN KEY (rfID) REFERENCES students(rfID)
);


INSERT INTO entrance_table (timeEntrace, rfID)
VALUES ("{current_time}, {rfID}");

INSERT INTO exit_table (timeExit, rfID)
VALUES ("{current_time}, {rfID}");

INSERT INTO students (rfID, nameStudent, presenceStudent, absenceStudent, lateStudent) VALUES ("0001", "Celso Ricardo", 0, 0, 0);


UPDATE students
SET nameStudent = 'Aprijjas', presenceStudent = 0, lateStudent = 0, absenceStudent = 0
WHERE rfID = '007';


SELECT presenceStudent FROM students WHERE rfID = '123';
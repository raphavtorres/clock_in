CREATE TABLE students (
    rfID varchar(100) NOT NULL,
    RAStudent int NOT NULL,
    nameStudent varchar (255),
    presenceStudent int,
    absenceStudent int,
    lateStudent int,
    PRIMARY KEY (rfID)
);


CREATE TABLE entrance_table (
    idEntrance int NOT NULL AUTO_INCREMENT,
    timeEntrace TIMESTAMP,
    rfID varchar (100),
    PRIMARY KEY (idEntrance),
    FOREIGN KEY (rfID) REFERENCES students(rfID)
);


CREATE TABLE exit_table (
    idExit int NOT NULL AUTO_INCREMENT,
    timeExit TIMESTAMP,
    rfID varchar (100),
    PRIMARY KEY (idExit),
    FOREIGN KEY (rfID) REFERENCES students(rfID)
);


INSERT INTO entrance_table (timeEntrace, rfID)
VALUES ("{current_time}, {rfID}");

INSERT INTO exit_table (timeExit, rfID)
VALUES ("{current_time}, {rfID}");

INSERT INTO students (rfID, nameStudent, presenceStudent, absenceStudent)
VALUES ('123', 'luis raphael', 1, 1);


UPDATE students
SET presenceStudent = 5, absenceStudent = 0
WHERE rfID = '123';

SELECT presenceStudent FROM students WHERE rfID = '123';
CREATE TABLE students (
    userID int NOT NULL,
    nameStudent varchar (255),
    presenceStudent int,
    absenceStudent int,
    lateStudent int,
    entrance int,
    exit_amount int,
    PRIMARY KEY (userID),
    FOREIGN KEY (entrance) REFERENCES entrance_table(idEntrance),
    FOREIGN KEY (exit_amount) REFERENCES exit_table (idExit)
);


CREATE TABLE entrance_table (
    idEntrance int NOT NULL AUTO_INCREMENT,
    entrance int,
    timeEntrace TIMESTAMP,
    PRIMARY KEY (idEntrance)
);


CREATE TABLE exit_table (
    idExit int NOT NULL AUTO_INCREMENT,
    exit_amount int,
    timeExit TIMESTAMP,
    PRIMARY KEY (idExit)
);

ALTER TABLE students ADD rfID varchar(255);
CREATE TABLE IF NOT EXISTS User_Demographics (
    user_id VARCHAR(10),
    age INT,
    gender ENUM('Male', 'Female'),
    interests VARCHAR(100),
    CONSTRAINT pk PRIMARY KEY (user_id)
);
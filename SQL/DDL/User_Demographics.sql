CREATE TABLE IF NOT EXISTS User_Demographics (
    user_id VARCHAR(10),
    age INT,
    gender VARCHAR(10) CHECK (gender IN ('Male', 'Female')),
    interests VARCHAR(100),
    PRIMARY KEY (user_id)
);

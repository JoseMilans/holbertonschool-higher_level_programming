-- Establish a table where its id field must have a default value, ensuring a non-empty field
CREATE TABLE IF NOT EXISTS id_not_null(
    id INT NOT NULL DEFAULT 1,
    name VARCHAR(256)
);



-- DROP DATABASE `tree`;

CREATE DATABASE `tree`;

USE `tree`;

CREATE TABLE `indexed` (
    item_id INT(11) NOT NULL,
    item VARCHAR(255) NOT NULL,
    category INT(11) NOT NULL,
    PRIMARY KEY (item_id)
);

CREATE TABLE `keytree` (
    auto_id INT PRIMARY KEY AUTO_INCREMENT,
    branch INT(11) NOT NULL,
    sub_branch INT(11) NOT NULL,
    tag VARCHAR(255) NOT NULL,
    category INT(11) NOT NULL,
    item VARCHAR(255) NOT NULL,
    item_id INT(11) NOT NULL
);


-- ALTER TABLE `keytree`
-- to drop either of these works
-- DROP CONSTRAINT item_index
-- DROP FOREIGN KEY item_index
-- ADD CONSTRAINT item_index
-- FOREIGN KEY (item_id) REFERENCES indexed(item_id)









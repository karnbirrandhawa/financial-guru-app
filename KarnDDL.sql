SET FOREIGN_KEY_CHECKS=0;
SET AUTOCOMMIT=0;

DROP TABLE IF EXISTS 
	Transactions, Accounts, Household_members_accounts, 
    Budget_categories, Household_members
;

CREATE TABLE Budget_categories (
	category_id INT(11) AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL UNIQUE,
    category_budget DECIMAL(11,2) NOT NULL 
);

CREATE TABLE Accounts (
	account_id INT(11) AUTO_INCREMENT PRIMARY KEY,
    account_name VARCHAR(50) NOT NULL UNIQUE,
    account_number VARCHAR(30) 
);

CREATE TABLE Household_members (
	member_id INT(11) AUTO_INCREMENT PRIMARY KEY,
    member_name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE Transactions (
	transaction_id INT(11) AUTO_INCREMENT PRIMARY KEY, 
    date DATE NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    description VARCHAR(255) NOT NULL, 
    account_id INT(11) NOT NULL, 
    category_id INT(11) NOT NULL,
    FOREIGN KEY (account_id) REFERENCES Accounts(account_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES Budget_categories(category_id) ON DELETE CASCADE
);

CREATE TABLE Household_members_accounts (
	household_members_accounts INT(11) AUTO_INCREMENT PRIMARY KEY,
    account_id INT(11) NOT NULL,
    member_id INT(11) NOT NULL,
    FOREIGN KEY (account_id) REFERENCES Accounts(account_id) ON DELETE RESTRICT,
    FOREIGN KEY (member_id) REFERENCES Household_members(member_id) ON DELETE RESTRICT
);


INSERT INTO Budget_categories (category_name, category_budget)
	VALUES ('Groceries', 800.00)
;
INSERT INTO Budget_categories (category_name, category_budget)
	VALUES ('Entertainment', 600.00)
;
INSERT INTO Budget_categories (category_name, category_budget)
	VALUES ('Rent', 800.00)
;
INSERT INTO Budget_categories (category_name, category_budget)
	VALUES ('Wages', 4000)
;

INSERT INTO Accounts (account_name, account_number)
	VALUES ('Primary Checking', '023456234')
;
INSERT INTO Accounts (account_name)
	VALUES ('Emergency Savings')
;
INSERT INTO Accounts (account_name, account_number)
	VALUES ('House Savings', '5637973246234')
;
INSERT INTO Accounts (account_name, account_number)
	VALUES ('Tiger Fund', NULL)
;

INSERT INTO Household_members (member_name)
	VALUES ('Billy Joe')
;
INSERT INTO Household_members (member_name)
	VALUES ('Mary Jane')
;
INSERT INTO Household_members (member_name)
	VALUES ('Diana Smith')
;
INSERT INTO Household_members (member_name)
	VALUES ('Tiger King')
;

INSERT INTO Transactions (date, amount, description, account_id, category_id)
	VALUES ('2023-07-11', -27.41, 'Piggly Wiggly', 2, 2)
;
INSERT INTO Transactions (date, amount, description, account_id, category_id)
    VALUES ('2023-08-21', -15, 'Bowl-O-Rama', 2, 1)
;
INSERT INTO Transactions (date, amount, description, account_id, category_id)
    VALUES ('2023-08-27', -1600, 'Landlord', 3, 3)
;
INSERT INTO Transactions (date, amount, description, account_id, category_id)
    VALUES ('2022-12-30', 2000, 'From Plants-R-Us', 1, 4)
;

INSERT INTO Household_members_accounts (account_id, member_id)
	VALUES (1,1)
;
INSERT INTO Household_members_accounts (account_id, member_id)
	VALUES (1,2)
;
INSERT INTO Household_members_accounts (account_id, member_id)
	VALUES (2,1)
;

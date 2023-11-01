 
 -- ----------- BUDGET CATEGORIES PAGE -------------- -- 

 -- get budget categories to display on categories.html
SELECT * FROM Budget_categories
;

 -- add new category in categories.html
INSERT INTO Budget_categories (category_name, category_budget)
    VALUES (:category_name_input, :category_budget_input)
;

 -- ----------- HOUSEHOLD MEMBERS PAGE -------------- --

 -- get household members to display on household-members.html
SELECT * FROM Household_members
;

 -- add household members 
INSERT INTO Household_members (member_name)
	VALUES (:member_name_input)
;

 -- get household members to populate dropdown in household-members.html
SELECT member_name
    FROM Household_members
    ORDER BY member_id ASC
;

 -- delete from household members
UPDATE Household_members
SET member_name = :member_name_update 
    WHERE member_id = :member_id_update
;

 -- ----------- HOUSEHOLD_MEMBERS_ACCOUNTS INTERSECTION TABLE QUERIES (M:M RELATIONSHIP) -------------- --

 -- get household members accounts intesection table to display 
SELECT * FROM Household_members_accounts
;

 -- add to household members accounts intersection table
INSERT INTO Household_members_accounts (account_id, member_id)
	VALUES (:account_id_input, :member_id_input)
;

-- delete from household members accounts intersection table
DELETE FROM Household_members_accounts 
    WHERE account_id = :account_id_deletion
    AND member_id = :member_id_deletion
;
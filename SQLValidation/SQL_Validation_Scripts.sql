-- Citizen Services Portal - SQL Validation Scripts

-- 1. Verify user login credentials exist
SELECT * FROM users WHERE username='user1' AND password='Pass123';

-- 2. Verify a new service application is stored for a given user
SELECT * FROM applications WHERE user_id=101;

-- 3. Verify application status is updated correctly
SELECT status FROM applications WHERE application_id=5001;

-- 4. Verify tracking number is generated after submission
SELECT tracking_number FROM applications WHERE application_id=5001;

-- 5. Verify invalid application ID returns no result
SELECT * FROM applications WHERE application_id=9999;

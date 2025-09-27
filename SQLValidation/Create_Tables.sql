
-- Citizen Services Portal Database Schema

-- 1. Users Table (for Login module)
CREATE TABLE Users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    role VARCHAR(20) DEFAULT 'Citizen'
);

-- Insert sample users
INSERT INTO Users (username, password, role) VALUES 
('user1', 'Pass123', 'Citizen'),
('admin', 'AdminPass', 'Admin');

-- 2. Applications Table (for Service Application & Status module)
CREATE TABLE Applications (
    application_id INT PRIMARY KEY AUTO_INCREMENT,
    applicant_name VARCHAR(100) NOT NULL,
    service_type VARCHAR(50) NOT NULL,
    status VARCHAR(20) DEFAULT 'Pending',
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample applications
INSERT INTO Applications (applicant_name, service_type, status) VALUES
('John Doe', 'Passport Renewal', 'Pending'),
('Jane Smith', 'Driving License', 'Approved');

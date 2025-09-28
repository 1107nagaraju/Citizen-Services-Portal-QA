Citizen-Services-Portal–QA Project
📌 Project Overview
This project demonstrates manual and automated testing of a simulated Citizen Services Portal.
The portal allows users to:

Log in securely
Apply for public services (e.g., housing, passport)
Track the status of applications
Generate a tracking number after submission
The project covers test planning, test case design, bug reporting, SQL validation, API testing, and automation scripts.

🛠️ Tools & Technologies
Test Management: Jira, TestRail
Database Testing: MySQL (SQL queries)
API Testing: Postman
Automation: Selenium (Python)
Version Control: Git, GitHub
Reporting: Excel, Word
📂 Project Structure
Citizen-Services-Portal-QA/ ├── README.md ├── TestPlan/ │ └── TestPlan_CitizenPortal.docx ├── TestCases/ │ └── TestCases_CitizenPortal.xlsx ├── BugReports/ │ └── BugReports_CitizenPortal.xlsx ├── TestSummary/ │ └── TestSummaryReport_CitizenPortal.docx ├── SQL_Validation/ │ ├── Create_Tables.sql ├── SQL_Validation_Scripts.sql ├── SQL_TestCases.xlsx └── SQL_Query_Result.png (screenshot from DbGate/MySQL after running queries) ├── API_Tests/ │ └── CitizenPortal_API_Tests.postman_collection.json ├── AutomationScripts/ │ └── Automation_Login_And_Application.py

🚀 How to Run
1. Manual Testing
Review TestPlan, TestCases, and BugReports.
Test cases designed in Excel, defects tracked with sample bug reports.
2. Database Validation
Run SQL scripts in /SQL_Validation/SQL_Validation_Scripts.sql on MySQL database.
Queries validate user login, application storage, status updates, and tracking numbers.
3. API Testing
Import API_Tests/CitizenPortal_API_Tests.postman_collection.json into Postman.
Run requests:
POST /login
POST /applyService
GET /getApplicationStatus/{id}
4. Automation Testing
Install dependencies:
pip install selenium
Run automation script: python AutomationScripts/Automation_Login_And_Application.py

📊 Deliverables

Test Plan (Word)

Test Cases (Excel)

Bug Reports (Excel)

SQL Validation Scripts

API Test Collection (Postman)

Selenium Automation Scripts

Test Summary Report
# Azure CMS – Cloud-Based Article Management System

This project is a **Cloud-based Content Management System (CMS)** developed using **Flask (Python)** and deployed on **Microsoft Azure App Service**. The application allows users to authenticate, create and manage articles, and store content securely in the cloud using Azure services.

The CMS demonstrates how modern web applications can be integrated with cloud infrastructure, including **Azure SQL Database, Azure Storage, and Azure Web App deployment**, along with **logging and authentication features**.

This project was developed as part of the **Azure Applications Project**.

---

# Project Overview

The Azure CMS is a simple yet functional **article management platform** where users can:

- Log in using authentication credentials
- Create new articles
- View previously created articles
- Store article content in a cloud database
- Monitor login activity through application logs

Each article consists of:

- **Title**
- **Author**
- **Body Content**

The article data is stored in an **Azure SQL Database**, while application logs and infrastructure are managed through Azure services.

---

# Technologies Used

The application integrates multiple technologies from web development and cloud computing.

### Backend
- Python 3
- Flask Framework

### Database
- Azure SQL Database
- pyodbc (SQL Server connectivity)

### Cloud Infrastructure
- Microsoft Azure
- Azure App Service
- Azure SQL Server
- Azure Storage Account (Blob Storage endpoints)

### Deployment
- GitHub Repository
- Continuous deployment from GitHub to Azure Web App

### Logging
- Azure Log Stream
- Python logging module

---

# Project Architecture

The architecture of this project follows a simple **three-layer structure**.

### 1. Frontend Layer
HTML templates rendered using Flask's **Jinja2 templating engine**.

Pages include:
- Home page
- Login page
- Dashboard
- Create Article page

### 2. Application Layer
Flask routes handle:

- User login authentication
- Article creation
- Data retrieval from the database
- Session management

### 3. Data Layer
Azure SQL Database stores application data in two tables:

- **users**
- **posts**

The application communicates with the database using **pyodbc**.

---

# Azure Resources Used

The following Azure resources were created to support the application:

- **Resource Group**
- **Azure Web App**
- **Azure SQL Server**
- **Azure SQL Database**
- **Azure Storage Account**

These resources collectively host and manage the CMS application.

---

# Application Features

## User Authentication

The application allows users to log in using credentials stored in the **users table** of the Azure SQL Database.

Example credentials:
Username: admin
Password: admin123


Authentication is handled through a simple **login form and database verification**.

---

## Article Creation

Authenticated users can create new articles through the **Create Post** page.

Each article includes:

- Title
- Author name
- Article content

The data is inserted into the **posts table** in Azure SQL Database.

---

## Article Dashboard

The **Dashboard** page retrieves and displays all articles stored in the database.

Each article shows:

- Title
- Author
- Article body

This demonstrates dynamic database retrieval using Flask.

---

## Application Logging

The application includes logging functionality to track login activity.

Examples of logged events include:
Invalid login attempt
admin logged in successfully


These logs can be viewed in **Azure Log Stream**.

Logging improves application monitoring and helps detect potential security issues.

---

# Project Tasks Completed

The following tasks were completed as part of the project requirements.

## 1. Azure Resource Group Creation

A resource group was created in Azure to contain all resources used by the CMS application.

This group includes:

- Web App
- SQL Server
- SQL Database
- Storage Account

---

## 2. Azure SQL Database Setup

An Azure SQL Database was created containing two tables:

### users table

Stores login credentials for application users.

Example columns:

- id
- username
- password

### posts table

Stores article data.

Example columns:

- id
- title
- author
- body

---

## 3. Azure Storage Blob Endpoint

A storage account was created to demonstrate cloud storage functionality.

Blob endpoints allow files or images to be stored and retrieved from Azure Storage.

Example endpoint:
https://<storageaccount>.blob.core.windows.net/


---

## 4. Azure Web App Deployment

The CMS application was deployed to **Azure App Service**, which hosts the Flask application in the cloud.

Deployment was performed using **GitHub integration**, allowing code updates to automatically redeploy the application.

---

## 5. Logging Implementation

Application logging was implemented using Python’s logging module.

The system logs:

- Successful login attempts
- Invalid login attempts

These logs are viewable through **Azure Log Stream**.

---

# Example Article Creation

To verify that the CMS works correctly, an article was created with the following data:
Title: Hello World!
Author: Jane Doe
Body: My name is Jane Doe and this is my first article!

This article confirms that:

- Data is inserted into Azure SQL Database
- Data is retrieved correctly and displayed on the dashboard

---

# Screenshots Included

The repository contains a **screenshots folder** with evidence of project completion.

Included screenshots:

1. Article successfully created in the CMS
2. Azure Resource Group with all resources
3. SQL database tables and example query
4. Blob storage endpoint
5. Redirect URIs for Microsoft authentication
6. Application log stream showing login attempts

---

# Dependencies

To run the project locally, the following dependencies are required:

- Python 3
- Flask
- pyodbc
- Azure Storage Blob SDK
- Gunicorn

All dependencies are listed in:
requirements.txt

Install dependencies using:
pip install -r requirements.txt

---

# Running the Application Locally

To run the project locally:

1. Clone the repository
git clone https://github.com/Roshni-0523/azure-flask-cms.git

2. Install dependencies
pip install -r requirements.txt

3. Set the required environment variables
DB_SERVER
DB_NAME
DB_USER
DB_PASSWORD

4. Run the Flask application
python app.py

---

# Project Repository

GitHub Repository:
https://github.com/Roshni-0523/azure-flask-cms

---

# Developer

Developed by:

**Roshni Rai**

B.Tech Computer Science and Engineering  
Lovely Professional University

---

# License

This project was developed for educational purposes as part of an Azure cloud computing project.

# Student Transcript Portal

A professional, web-based student transcript management system built with Python (Flask) and SQLite. This application allows for the visualization and management of student grades, attendance, and population statistics across various Master's programs.

## Features

- **Dashboard Overview**: Visual analytics of active populations and overall attendance using dynamic charts.
- **Population Management**: Detailed views of student cohorts (AIS, CS, DSA, ISM, SE).
- **Grade Tracking**: Comprehensive grade reports for individual courses and students.
- **Responsive Design**: Modern, clean UI built with CSS variables and Flexbox/Grid for optimal viewing on all devices.
- **Data Visualization**: Integrated Matplotlib charts for data insights.

## Technology Stack

- **Backend**: Python 3.x, Flask
- **Frontend**: HTML5, CSS3 (Modern Variables & Flexbox), JavaScript
- **Database**: SQL (pymysql/SQLite)
- **Visualization**: Matplotlib

## Project Structure

```
├── server.py              # Main Flask application entry point
├── static/                # Static assets (CSS, JS, Images, Database)
│   ├── common.css         # Main design system and styles
│   ├── last_generation.js # Footer timestamp script
│   └── ...
├── templates/             # HTML Templates (Jinja2)
│   ├── index.html         # Dashboard
│   ├── login.html         # Authentication
│   ├── populations/       # Population detail pages
│   └── grades/            # Grade detail pages
└── README.md              # Project documentation
```

## Setup & Installation

1.  **Prerequisites**: Ensure Python 3.x is installed on your system.
2.  **Database Setup**:
    - Locate `db.zip` in the `static` folder.
    - Extract the contents and execute the `.sql` files to initialize your database.
    - Update the database connection settings in `server.py` if necessary.
3.  **Install Dependencies**:
    ```bash
    pip install flask pymysql matplotlib
    ```
4.  **Run the Application**:
    ```bash
    python server.py
    ```
5.  **Access**: Open your browser and navigate to `http://localhost:5000` (or the port specified in the console).

## Usage

- **Home**: View the overview of all programs and attendance stats.
- **Populations**: Click on a program name to view the list of students and courses for that cohort.
- **Grades**: Navigate to a specific course to view detailed grade breakdowns.

## License

This project is for educational purposes.

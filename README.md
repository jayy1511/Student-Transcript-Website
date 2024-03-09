# Student Transcript Website

## Introduction

This project aims to create a static student transcript website using Python (with Flask), HTML, CSS, JavaScript, and SQL. It provides an overview of the project structure, code explanation, instructions on how to run it, and a conclusion.

## Page Description

The website consists of multiple pages:
- **Welcome Page**: Provides an overview of the project.
- **Population Page**: Displays a list of active populations, which are clickable, leading to the population page for each group. This page has two sections: Students and Courses. The Students section contains a table with information about students, while the Courses section lists all courses and their subjects. Both students and courses are clickable, leading to the grades page, which displays each student's grades in the particular course.
- **Grades Page**: Shows the grades of students in specific courses.
- **Navigation**: Each page includes a clickable "Home" link at the top to return to the Welcome page.

## Code Explanation

The project comprises four main components: Python, HTML, CSS, JavaScript, and SQL.

- **HTML and CSS**: The main `index.html` file serves as the welcome page, while other HTML files are created for the population and grades pages. Data is injected into these HTML files using Flask. CSS files are organized into separate files for each page and a common file for shared styles.
- **Python (Flask)**: Python scripts handle database connection using pymysql and execute queries using Flask. Routes are defined for each page of the website.
- **Chart**: Matplotlib is used for generating charts, which are integrated into the `index.html` page.
- **Last Website Generation**: JavaScript is utilized for the last website generation function.

## How to Run it

1. Update the database connection in the `server.py` file.
2. Run the `server.py` script.
3. Follow the link provided in the output after running the Python file.

Ensure that the `static` folder contains CSS files, JavaScript files, and images used in the website, while the `templates` folder contains all HTML templates. These folders should be placed in the `src` folder in a zip file. Avoid putting anything in the `site` folder to maintain consistency in URLs across HTML templates and Python files.

## Conclusion

While this may not be the most efficient approach, creating this website using Flask was a valuable learning experience. It provided insights into Python development with Flask and enhanced understanding of web development fundamentals. Despite its simplicity, the process contributed to skill development and understanding of web technologies. 


<?php
// Include the database connection file
require_once '../Database/db.php'; // Adjust path as needed

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Retrieve and sanitize POST data
    $course_code = htmlspecialchars(trim($_POST['course_code']));
    $course_name = htmlspecialchars(trim($_POST['course_name']));
    $course_description = htmlspecialchars(trim($_POST['course_description']));

    // Check if any field is empty
    if (empty($course_code) || empty($course_name) || empty($course_description)) {
        echo "All fields are required.";
        exit();
    }

    // Prepare the SQL query
    $query = "INSERT INTO Courses (course_code, course_name, course_description) VALUES (?, ?, ?)";
    $stmt = $conn->prepare($query);

    // Bind parameters and execute the query
    if ($stmt) {
        $stmt->bind_param("sss", $course_code, $course_name, $course_description);
        
        if ($stmt->execute()) {
            // Redirect to the courses page showing the updated list
            header("Location: ../path/to/coursesDetails.html"); // Adjust path as needed
            exit();
        } else {
            echo "Error: Could not add the course. " . $stmt->error;
        }

        // Close the statement
        $stmt->close();
    } else {
        echo "Error: Could not prepare the SQL statement.";
    }

    // Close the database connection
    $conn->close();
} else {
    echo "Invalid request method.";
}
?>

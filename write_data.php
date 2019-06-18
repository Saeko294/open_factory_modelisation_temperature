<?php

    // Prepare variables for database connection

    $dbusername = "";  // enter database username
    $dbpassword = "";  // enter database password
    $server = "localhost"; // IMPORTANT: if you are using XAMPP enter "localhost", but if you have an online website enter its address, ie."www.yourwebsite.com"

    // Connect to your database

    $dbconnect = mysqli_connect( $server, $dbusername, $dbpassword, 'dbname');

    // Prepare the SQL statement

    $req = "INSERT INTO temperature (temp, temp_2, temp_3, temp_4, temp_5) VALUES ('".$_GET["value"]."','".$_GET["value_2"]."','".$_GET["value_3"]."','".$_GET["value_4"]."','".$_GET["value_5"]."')";

    // Execute SQL statement

    $dbconnect->query($req);


?>

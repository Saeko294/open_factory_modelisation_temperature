<?php

    // Varaiables pour la connection à la base de données

    $dbusername = "enzo";  // enter database username, I used "arduino" in step 2.2
    $dbpassword = "dadada";  // enter database password, I used "arduinotest" in step 2.2
    $server = "localhost"; // IMPORTANT: if you are using XAMPP enter "localhost", but if you have an online website enter its address, ie."www.yourwebsite.com"

    // Connection à la base de données

    $dbconnect = mysqli_connect( $server, $dbusername, $dbpassword, 'arduino');

    // Préparer la requête SQL
    $id_boite = filter_var($_GET["value"], FILTER_SANITIZE_STRING);
    $temp = filter_var($_GET["value_2"], FILTER_SANITIZE_STRING);
    $req = "INSERT INTO tempe (id_boite, temp) VALUES ('".$id_boite."','".$temp."')";
    filter_input(INPUT_GET, "s", FILTER_SANITIZE_STRING);
    // Executer la requête SQL

    $dbconnect->query($req);


?>

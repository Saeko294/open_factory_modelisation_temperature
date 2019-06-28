<?php
	$url=$_SERVER['REQUEST_URI'];
	header("Refresh: 30; URL=$url");  // Refresh the webpage every 30 seconds
	/* Database connection settings */
	$host = 'localhost';
	$user = '';
	$pass = '';
	$db = '';
	$mysqli = new mysqli($host,$user,$pass,$db,8080) or die($mysqli->error);

	$data1 = '';
	$data2 = '';
	$data3 = '';
	$data4 = '';
	$data5 = '';

	$data_time = '';

	//query to get data from the table
	$sql = "SELECT * FROM tempe WHERE id_boite = 1 ";
    $result = mysqli_query($mysqli, $sql);

	//loop through the returned data
	while ($row = mysqli_fetch_array($result)) {

		$data1 = $data1 . '"'. $row['temp'].'",';
		$data_time = $data_time . '"'. $row['time'] .'",';
	}

	$sql = "SELECT * FROM tempe WHERE id_boite = 2 ";
    $result = mysqli_query($mysqli, $sql);

	//loop through the returned data
	while ($row = mysqli_fetch_array($result)) {

		$data2 = $data2 . '"'. $row['temp'].'",';
	}

	$sql = "SELECT * FROM tempe WHERE id_boite = 3 ";
		$result = mysqli_query($mysqli, $sql);

	//loop through the returned data
	while ($row = mysqli_fetch_array($result)) {

		$data3 = $data3 . '"'. $row['temp'].'",';
	}
	$sql = "SELECT * FROM tempe WHERE id_boite = 4 ";
		$result = mysqli_query($mysqli, $sql);

	//loop through the returned data
	while ($row = mysqli_fetch_array($result)) {

		$data4 = $data4 . '"'. $row['temp'].'",';
	}
	$sql = "SELECT * FROM tempe WHERE id_boite = 5 ";
		$result = mysqli_query($mysqli, $sql);

	//loop through the returned data
	while ($row = mysqli_fetch_array($result)) {

		$data5 = $data5 . '"'. $row['temp'].'",';
	}

	$data1 = trim($data1,",");
	$data2 = trim($data2,",");
	$data3 = trim($data3,",");
	$data4 = trim($data4,",");
	$data5 = trim($data5,",");

	$data_time = trim($data_time,",");
?>

<!DOCTYPE html>
<html>
	<head>
    	<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.2/Chart.bundle.min.js"></script>
		<title>Temperature</title>

		<style type="text/css">
			body{
				font-family: Arial;
			    margin: 80px 100px 10px 100px;
			    padding: 0;
			    color: white;
			    text-align: center;
			    background: #555652;
			}

			.container {
				color: #E8E9EB;
				background: #222;
				border: #555652 1px solid;
				padding: 10px;
			}
		</style>

	</head>

	<body>
		<a href="index_2.php" target="_blank"><input type="button" value="Température moyenne"></a>
	    <div class="container">
	    <h1>CAPTEUR DE TEMPÉRATURE</h1>
			<canvas id="chart" style="width: 100%; height: 65vh; background: #222; border: 1px solid #555652; margin-top: 10px;"></canvas>

			<script>
				var ctx = document.getElementById("chart").getContext('2d');
    			var myChart = new Chart(ctx, {
        		type: 'line',
		        data: {
		            labels: [<?php echo $data_time; ?>],
		            datasets:
		            [{
		                label: 'Capteur 1',
		                data: [<?php echo $data1; ?>],
		                backgroundColor: 'transparent',
		                borderColor:'rgba(255,99,132)',
		                borderWidth: 3
		            },

		            {
		            	label: 'Capteur 2',
		                data: [<?php echo $data2; ?>],
		                backgroundColor: 'transparent',
		                borderColor:'rgba(0,255,255)',
		                borderWidth: 3
		            },
								{
		                label: 'Capteur 3',
		                data: [<?php echo $data3; ?>],
		                backgroundColor: 'transparent',
		                borderColor:'rgba(155, 89, 182)',
		                borderWidth: 3
		            },
								{
		                label: 'Capteur 4',
		                data: [<?php echo $data4; ?>],
		                backgroundColor: 'transparent',
		                borderColor:'rgba(230, 126, 34)',
		                borderWidth: 3
		            },
								{
		                label: 'Capteur 5',
		                data: [<?php echo $data5; ?>],
		                backgroundColor: 'transparent',
		                borderColor:'rgba(41, 128, 185)',
		                borderWidth: 3
		            },

							]
		        },

		        options: {
		            scales: {scales:{yAxes: [{beginAtZero: false}], xAxes: [{autoskip: true, maxTicketsLimit: 20}]}},
		            tooltips:{mode: 'index'},
		            legend:{display: true, position: 'top', labels: {fontColor: 'rgb(255,255,255)', fontSize: 16}}
		        }
		    });
			</script>
	    </div>

	</body>
</html>

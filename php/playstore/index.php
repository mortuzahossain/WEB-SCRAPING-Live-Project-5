<?php

include 'db_config.php';

$sql = "SELECT * FROM playstore";
$result = mysqli_query($con,$sql);

while ($row = mysqli_fetch_assoc($result)) {
    $data[] =$row;
}


?>

<!DOCTYPE html>
<html>
<head>
	<title>OUR Own Playstore</title>
	<link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="css/style.css">
</head>
<body>


    <div class="container text-center header">
        <h1>OUR Own Playstore</h1>
    </div>


    <div class="container main-content text-center">
        

<?php
    foreach ($data as $key) {
?>

        <div class="col-md-3 single-app">
            
            <a href="<?php echo 'https://play.google.com/' . $key['url'] ; ?>"><img src="<?php echo $key['image'] ; ?>"> </a>
            <h2><?php echo $key['name'] ; ?></h2>
            <a href="<?php echo $key['developerurl'] ; ?>"><h3><?php echo $key['developer'] ; ?></h3></a>
           
        </div>

<?php
    }
?>

    </div>


    <div class="text-center footer">
        <p>Developed By <a href="http://www.facebook.com/mdmortuza.hossain">Md Mortuza Hossain</a></p>
    </div>




    <script type="text/javascript" src="js/jquery-3.3.1.js"></script>
    <script type="text/javascript" src="js/bootstrap.min.js"></script>
</body>
</html>
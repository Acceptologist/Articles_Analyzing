<?php
include_once $_SERVER['DOCUMENT_ROOT'].'/findhouse.com/PHP/init.php';
?>
<!DOCTYPE>
<html>
<head>
	<title>404 Error</title>
	<link rel="stylesheet" type="text/css" href="<?php echo HeaderCSS; ?>">
	<link rel="stylesheet" type="text/css" href="<?php echo CenterCSS; ?>">
	<link rel="stylesheet" type="text/css" href="<?php echo FooterCSS; ?>">
	<link rel="icon" type="image/JPG" href="<?php echo LOGO; ?>">

	<script src="<?php echo JavaScript; ?>jquery-3.3.1.js"></script>
    <script src="<?php echo JavaScript; ?>js.cookie.js"></script>

    <script src="<?php echo JavaScript; ?>DropBox.js"></script>
    <script src="<?php echo JavaScript; ?>SetCookie.js"></script>
</head>
<body style="text-align: center;">
	<p>Error in Requesting Page</p>
	<p>May Be This Page Not Found</p>
	<p>Please Try in Another Time <a href="<?php echo MainPage; ?>">Go To Main Page</a></p>
</body>
</html>
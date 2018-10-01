<?php
	session_start();

		$username = $_POST['username'];
		$password = $_POST['password'];
	
		if($username=="lanka" && $password=="1234"){ 
			header('Location: index.html');
		} else {
			header('Location: login_error.php');
		}
?>
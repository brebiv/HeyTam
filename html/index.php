<!doctype html>
<html>
<head>
	<meta charset="utf-8">
	<title>Main</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <link href="style.css" rel="stylesheet" type="text/css">
	<link href="opacity.css" rel="stylesheet" type="text/css">
	<link href="header.css" rel="stylesheet" type="text/css">
    <script>
        $(document).ready(function () {
            $('header')
                .animate({opacity: 1}, 1400)
            $('.quote')
                .animate({opacity: 1}, 1600)
            $('.hello')
                .animate({opacity: 1}, 1600)
        });
    </script>
</head>

<body class="main">
	<header>
        <div class="logo">
            <div class="logo_inner">
                <a href="#"><img src="logo.png"></a>
            </div>
        </div>
        <nav>
            <ul>
                <li><a href="news/news.php" class="nav_button">News</a></li>
                <li><a href="programs/progs.html" class="nav_button">Programs</a></li>
                <li><a href="about/about.html" class="nav_button">About us</a></li>
                <li><a href="#" class="nav_button">Exit</a></li>
            </ul>
        </nav>
    </header>
    <?php require_once 'data.php'?>
    <div class="quote"><p><?php
            $rand = $quotes[array_rand($quotes)];
            $rand->printQuote()
            ?><br>
        </p><p class="author"><?php $rand->printAuthor() ?></p>
	</div>
	<div class="hello">
		<h1>Добро пожаловать.</h1>
		<script src="script.js"></script>
		<p>
			IT - для каждого!<br>
			Множество полезных программ на все случаи жизни!<br>
			<br>
			HeyTam - присоединяйся!<br>
		</p>
	</div>
</body>
</html>

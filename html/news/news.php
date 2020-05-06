<!DOCTYPE html>
<html>
    <head>
        <title>HeyTam - News</title>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
        <script src="script.js"></script>
        <link href="news.css" rel="stylesheet" type="text/css">
        <link href="header.css" rel="stylesheet" type="text/css">
        <link href="opacity.css" rel="stylesheet" type="text/css">
        <meta charset="utf-8">
        <script>
            $(document).ready(function () {
                $('header')
                    .animate({opacity: 1}, 500)
                $('.main')
                    .animate({opacity: 1}, 500)
            });
    </script>
        <?php require_once 'data_news.php'?>
    </head>
    <body>  
        <header>
            <div class="logo">
                <div class="logo_inner">
                    <a href="../index.php"><img src="logo.png"></a>
                </div>
            </div>
            <nav>
                <ul>
                    <li><a href="#" class="nav_button">News</a></li>
                    <li><a href="../programs/progs.html" class="nav_button">Programs</a></li>
                    <li><a href="../about/about.html" class="nav_button">About us</a></li>
                    <li><a href="#" class="nav_button">Exit</a></li>
                </ul>
            </nav>
        </header>
        <div class="main">      
            <?php require 'article.php'; ?>
        </div>
    </body>
</html>
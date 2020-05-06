<!DOCTYPE html>
<html>
    <head>
        <title>HeyTam - News</title>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
        <script src="script.js"></script>
        <link href="news.css" rel="stylesheet" type="text/css">
        <link href="header.css" rel="stylesheet" type="text/css">
        <meta charset="utf-8">
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
            <div class="content">
                <div class="border"><h1>Новости</h1></div>
                <div class="article">
                    <div class="preview">
                        <img src="1.jpg">
                    </div>
                    <div class="title">
                        <h1>Багамские острова</h1>
                    </div>
                    <div class="short_content">
                        <p>
                            Сегодня на богамских островах жить стало еще лучше!<br>
                            Отныне стоимость бунгало составляет 300 тыс. $!<br>
                            Это на 53% дешевле чем вчера.
                            Площадь бунгало 50 кв. м!<br>(Возле океана)
                        </p>
                    </div>
                    <div class="time">
                        <p>20.07.2019</p>
                    </div>
                </div>
                <div class="article">
                    <div class="preview">
                        <img src="2.jpg">
                    </div>
                    <div class="title">
                        <h1>Кровавый закат на Богамах уничтожил 7 острова!!!</h1>
                    </div>
                    <div class="short_content">
                        <p>
                            Вчера в 13:33 стало известо об ужасное трагедии.<br>
                            Из-за того что цвет неба стал кроваво-красным многие кораллы были уничтожоны.<br>
                            В следстии чего 7 островов погрузились под воду!
                        </p>
                    </div>
                    <div class="time">
                        <p>19.07.2019</p>
                    </div>
                </div>
                <?php require 'article.php'; ?>
            </div>
        </div>
    </body>
</html>
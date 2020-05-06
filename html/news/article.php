<div class="content">
    <div class="top"><h1>Новости</h1></div>
<?php 
    $articles = get_articles();
    foreach ($articles as $article): ?>
                <div class="article">
                    <div class="preview">
                        <img src="<?php echo $article->preview; ?>">
                    </div>
                    <div class="title">
                        <h1><?php echo $article->title; ?></h1>
                    </div>
                    <div class="short_content">
                        <p>
                            <?php echo $article->short_content; ?>
                        </p>
                    </div>
                    <div class="time">
                        <p><?php echo $article->date; ?></p>
                    </div>
                </div>
<?php endforeach; ?>

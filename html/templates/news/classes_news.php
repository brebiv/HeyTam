<?php

class Article{
    public $id;
    public $title;
    public $date;
    public $short_content;
    public $content;
    public $author_name;
    public $preview;
    public $status;

    function __construct($row)
    {
        $this->id = $row['id'];
        $this->title = $row['title'];
        $this->date = $row['date'];
        $this->short_content = $row['short_content'];
        $this->content = $row['content'];
        $this->author_name = $row['author_name'];
        $this->preview = $row['preview'];
        $this->status = $row['status'];
    }

    public function printTitle(){
        echo $this->title;
    }

    public function printPreview(){
        echo $this->preview;
    }
}
<?php

class Quote{

    public $id;
    public $author;
    public $quote;

    function __construct($row)
    {
        $this->id = $row['id'];
        $this->quote = $row['quote'];
        $this->author = $row['author'];
    }

    public function printQuote()
    {
        echo $this->quote;
    }

    public function printAuthor()
    {
        echo $this->author;
    }
}
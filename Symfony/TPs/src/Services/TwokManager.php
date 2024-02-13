<?php

namespace App\Services;

use App\Entity\Twok;

class TwokManager
{
    public function __construct(private readonly string $path)
    {

    }

    public function getTwokById(int $id) : ?Twok{
        $jsonString = file_get_contents($this->path);
        $jsonData = json_decode($jsonString, true);

        foreach ($jsonData as $twok){
            if($twok['id']==$id){
                return new Twok($twok['id'],$twok['author'],$twok['content'],$twok['created_at']);
            }
        }

        return Null;
    }

    public function addTwok(Twok $twok): bool{
        $jsonString = file_get_contents($this->path);
        $jsonData = json_decode($jsonString, true);
        $jsonString = json_encode($jsonData,$twok);
        file_put_contents($this->path, $jsonString);
        return true;
    }

}
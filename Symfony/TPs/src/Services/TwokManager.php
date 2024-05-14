<?php

namespace App\Services;

use App\Entity\Twok;
use Symfony\Component\Serializer\Encoder\JsonEncoder;
use Symfony\Component\Serializer\Encoder\XmlEncoder;
use Symfony\Component\Serializer\Normalizer\ObjectNormalizer;
use Symfony\Component\Serializer\Serializer;

class TwokManager
{
    public function __construct(private readonly string $path,private readonly EntityManager $mgr)
    {
        $encoders = [new XmlEncoder(), new JsonEncoder()];
        $normalizers = [new ObjectNormalizer()];
        $serializer = new Serializer($normalizers, $encoders);
    }

    public function getTwoks() : mixed
    {
        $jsonString = file_get_contents($this->path);
        return json_decode($jsonString, true);
    }

    public function importTwoks(): mixed
    {

        $encoders = [new XmlEncoder(), new JsonEncoder()];
        $normalizers = [new ObjectNormalizer()];
        $serializer = new Serializer($normalizers, $encoders);

        $listTwoks = $this->getTwoks();
        foreach ($listTwoks as $twok){
            $twokObject = $serializer->deserialize($jsonData,Twok::class,'json');
            $this->mgr->persist($twokObject);
            $this->mgr->flush();
        }
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
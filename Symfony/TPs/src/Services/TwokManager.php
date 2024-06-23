<?php

namespace App\Services;

use App\Entity\Twok;
use Symfony\Component\Serializer\Encoder\JsonEncoder;
use Symfony\Component\Serializer\Encoder\XmlEncoder;
use Symfony\Component\Serializer\Normalizer\ObjectNormalizer;
use Symfony\Component\Serializer\Serializer;
use Doctrine\ORM\EntityManager;

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
        return $this->mgr->getRepository(Twok::class)->findAll();
        
    }

    // public function importTwoks(): void
    // {
    //     $jsonString = file_get_contents($this->path);
    //     $jsonData = json_decode($jsonString, true);
    //     $encoders = [new XmlEncoder(), new JsonEncoder()];
    //     $normalizers = [new ObjectNormalizer()];
    //     $serializer = new Serial/ContainerVoizer($normalizers, $encoders);

    //     $listTwoks = $this->getTwoks();
    //     foreach ($listTwoks as $twok){
    //         $twokObject = $serializer->deserialize($jsonData,Twok::class,'json');
    //         $this->mgr->persist($twokObject);
    //         $this->mgr->flush();
    //     }
    //     return;
    // }

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
        $this->mgr->persist($twok);
        $this->mgr->flush();
        return true;
    }

}
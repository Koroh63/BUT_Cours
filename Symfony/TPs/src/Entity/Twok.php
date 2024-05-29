<?php

namespace App\Entity;

use App\Repository\TwokRepository;
use Doctrine\ORM\Mapping as ORM;
use Symfony\UX\Turbo\Attribute\Broadcast;
use ApiPlatform\Metadata\ApiRessource;


#[ORM\Entity(repositoryClass: TwokRepository::class)]
#[Broadcast]
class Twok
{
    public function __construct(int $id,string $auteur,string $message, string $date)
    {
        $this->id = $id;
        $this->auteur = $auteur;
        $this->message = $message;
        $this->date = $date;

    }

    #[ORM\Id]
    #[ORM\Column]
    private ?int $id = null;

    #[ORM\Column(length: 255, nullable: true)]
    private ?string $auteur = null;

    #[ORM\Column(length: 255, nullable: true)]
    private ?string $message = null;

    #[ORM\Column(length: 255, nullable: true)]
    private ?string $date = null;

    public function getId(): ?int
    {
        return $this->id;
    }

    public function getAuteur(): ?string
    {
        return $this->auteur;
    }

    public function setAuteur(?string $auteur): static
    {
        $this->auteur = $auteur;

        return $this;
    }

    public function getMessage(): ?string
    {
        return $this->message;
    }

    public function setMessage(?string $message): static
    {
        $this->message = $message;

        return $this;
    }

    public function getDate(): ?string
    {
        return $this->date;
    }

    public function setDate(?string $date): static
    {
        $this->date = $date;

        return $this;
    }
}

<?php

namespace App\Controller;

use App\Entity\Twok;
use App\Services\TwokManager;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

class TweetTokController extends AbstractController
{
    #[Route('/home', name: 'app_tweet_tok')]
    public function index(): Response
    {
        return $this->render('tweet_tok/index.html.twig', [
            'message' => "Bienvenue dans le home ! C'est le home ... Voilà Voilà ..."
        ]);
    }

    #[Route('/home/{id}',requirements: ['page' => '\d+'])]
    public function showTwok(int $id,TwokManager $mgr): Response
    {
        $twok = $mgr->getTwokById($id);
        if($twok!=Null){
            return $this->render('tweet_tok/showTwok.html.twig', [
                'message' => $twok->getMessage(),
                'auteur' => $twok->getAuteur(),
                'date' => $twok->getDate()
            ]);
        }
        return $this->render('tweet_tok/showTwok.html.twig', [
            'message' => 'Twok inconnu',
            'auteur' => 'None',
            'date' => 'Never'
        ]);
    }

    #[Route('/home/{twok}', methods: ['PUT'],priority: 2)]
    public function addTwok(Twok $twok,TwokManager $mgr) : Response
    {
        $mgr->addTwok($twok);
        return $this->render('tweet_tok/index.html.twig', [
            'message' => "Twok Ajouté !"
        ]);
    }
}

<?php

namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

class TweetTokController extends AbstractController
{
    #[Route('/tweet/tok', name: 'app_tweet_tok')]
    public function index(): Response
    {
        return $this->render('tweet_tok/index.html.twig', [
            'controller_name' => 'TweetTokController',
        ]);
    }
}

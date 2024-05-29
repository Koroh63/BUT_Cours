<?php

namespace App\Controller;

use App\Entity\Twok;
use App\Services\TwokManager;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;
use Symfony\Component\HttpFoundation\Request;

use App\Form\TwokFormType;



class TweetTokController extends AbstractController
{
    #[Route('/home', name: 'app_tweet_tok')]
    public function index(TwokManager $mgr): Response
    {
        $twoks = $mgr->getTwoks();
        return $this->render('tweet_tok/index.html.twig', [
            'message' => "Bienvenue dans le home ! C'est le home ... Voilà Voilà ...",
            'twoks' => $twoks
        ]);
    }

    #[Route('/import')]
    public function import(TwokManager $mgr): Response
    {
        // $mgr->importTwoks();
        return $this->render('tweet_tok/index.html.twig', [
            'message' => "Twok Ajouté !"
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
        }else{
            return $this->render('tweet_tok/showTwok.html.twig', [
                'message' => 'Twok inconnu',
                'auteur' => 'None',
                'date' => 'Never'
            ]);
        }
    }

    #[Route('/home/{twok}', methods: ['POST'],priority: 2)]
    public function addTwok(Twok $twok,TwokManager $mgr) : Response
    {
        $mgr->addTwok($twok);
        return $this->render('tweet_tok/index.html.twig', [
            'message' => "Twok Ajouté !"
        ]);
    }

    #[Route('/twok/add', methods: ['GET','POST'])]
    public function getForm(Request $request,TwokManager $mgr) : Response
    {
        $form = $this->createForm(TwokFormType::class);
        
        $form->handleRequest($request);
        
        if($form->isSubmitted() && $form->isValid()){
            $twok = $form->getData();
            $mgr->addTwok(new Twok($twok->getId, $twok->getNom(),$twok->getMessage(),$twok->getDate()));
            return $this->redirectToRoute('home');
        }

        return $this->render('tweet_tok/formTwok.html.twig',[
            'form'=> $form->createView(),
        ]);
    }
}

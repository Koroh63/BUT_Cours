<?php

namespace App\Twig;

use Twig\Extension\AbstractExtension;
use Twig\TwigFilter;

class AppExtension extends AbstractExtension
{

    public function getFilters(): array
    {
        return [
            new TwigFilter('summarize',[$this,'summarizeString'])
        ];
    }

    public function summarizeString(string $message,int $length): string
    {
        if(strlen($message)> $length){
            return substr($message,0,$length) . '...';
        }else{
            return $message;
        }
    }
}
<?php

namespace ContainerQ3xg0Dp;

use Symfony\Component\DependencyInjection\Argument\RewindableGenerator;
use Symfony\Component\DependencyInjection\ContainerInterface;
use Symfony\Component\DependencyInjection\Exception\RuntimeException;

/**
 * @internal This class has been auto-generated by the Symfony Dependency Injection Component.
 */
class getQuoteControllerService extends App_KernelTestDebugContainer
{
    /**
     * Gets the public 'App\Controller\QuoteController' shared autowired service.
     *
     * @return \App\Controller\QuoteController
     */
    public static function do($container, $lazyLoad = true)
    {
        include_once \dirname(__DIR__, 3).'/TP1/vendor/symfony/framework-bundle/Controller/AbstractController.php';
        include_once \dirname(__DIR__, 3).'/TP1/src/Controller/QuoteController.php';

        $container->services['App\\Controller\\QuoteController'] = $instance = new \App\Controller\QuoteController(($container->privates['.debug.http_client'] ?? self::get_Debug_HttpClientService($container)));

        $instance->setContainer((new \Symfony\Component\DependencyInjection\Argument\ServiceLocator($container->getService ??= $container->getService(...), [
            'form.factory' => ['privates', 'form.factory', 'getForm_FactoryService', true],
            'http_kernel' => ['services', 'http_kernel', 'getHttpKernelService', false],
            'parameter_bag' => ['privates', 'parameter_bag', 'getParameterBagService', false],
            'request_stack' => ['services', 'request_stack', 'getRequestStackService', false],
            'router' => ['services', 'router', 'getRouterService', false],
            'security.authorization_checker' => ['privates', 'security.authorization_checker', 'getSecurity_AuthorizationCheckerService', false],
            'security.csrf.token_manager' => ['privates', 'security.csrf.token_manager', 'getSecurity_Csrf_TokenManagerService', true],
            'security.token_storage' => ['privates', 'security.token_storage', 'getSecurity_TokenStorageService', false],
            'serializer' => ['privates', 'serializer', 'getSerializerService', false],
            'twig' => ['privates', 'twig', 'getTwigService', false],
            'web_link.http_header_serializer' => ['privates', 'web_link.http_header_serializer', 'getWebLink_HttpHeaderSerializerService', false],
        ], [
            'form.factory' => '?',
            'http_kernel' => '?',
            'parameter_bag' => '?',
            'request_stack' => '?',
            'router' => '?',
            'security.authorization_checker' => '?',
            'security.csrf.token_manager' => '?',
            'security.token_storage' => '?',
            'serializer' => '?',
            'twig' => '?',
            'web_link.http_header_serializer' => '?',
        ]))->withContext('App\\Controller\\QuoteController', $container));

        return $instance;
    }
}

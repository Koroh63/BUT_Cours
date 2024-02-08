<?php

namespace ContainerQ3xg0Dp;

use Symfony\Component\DependencyInjection\Argument\RewindableGenerator;
use Symfony\Component\DependencyInjection\ContainerInterface;
use Symfony\Component\DependencyInjection\Exception\RuntimeException;

/**
 * @internal This class has been auto-generated by the Symfony Dependency Injection Component.
 */
class getHttpClient_Messenger_PingWebhookHandlerService extends App_KernelTestDebugContainer
{
    /**
     * Gets the private 'http_client.messenger.ping_webhook_handler' shared service.
     *
     * @return \Symfony\Component\HttpClient\Messenger\PingWebhookMessageHandler
     */
    public static function do($container, $lazyLoad = true)
    {
        include_once \dirname(__DIR__, 3).'/TP1/vendor/symfony/http-client/Messenger/PingWebhookMessageHandler.php';

        return $container->privates['http_client.messenger.ping_webhook_handler'] = new \Symfony\Component\HttpClient\Messenger\PingWebhookMessageHandler(($container->privates['.debug.http_client'] ?? self::get_Debug_HttpClientService($container)));
    }
}

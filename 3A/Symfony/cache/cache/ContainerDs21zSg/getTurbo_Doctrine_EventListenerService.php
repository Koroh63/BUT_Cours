<?php

namespace ContainerDs21zSg;

use Symfony\Component\DependencyInjection\Argument\RewindableGenerator;
use Symfony\Component\DependencyInjection\ContainerInterface;
use Symfony\Component\DependencyInjection\Exception\RuntimeException;

/**
 * @internal This class has been auto-generated by the Symfony Dependency Injection Component.
 */
class getTurbo_Doctrine_EventListenerService extends App_KernelTestDebugContainer
{
    /**
     * Gets the private 'turbo.doctrine.event_listener' shared service.
     *
     * @return \Symfony\UX\Turbo\Doctrine\BroadcastListener
     */
    public static function do($container, $lazyLoad = true)
    {
        include_once \dirname(__DIR__, 3).'/TP1/vendor/symfony/ux-turbo/src/Doctrine/BroadcastListener.php';

        return $container->privates['turbo.doctrine.event_listener'] = new \Symfony\UX\Turbo\Doctrine\BroadcastListener(($container->privates['turbo.broadcaster.action_renderer'] ?? $container->load('getTurbo_Broadcaster_ActionRendererService')), NULL);
    }
}

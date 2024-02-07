<?php

namespace ContainerQ3xg0Dp;

use Symfony\Component\DependencyInjection\Argument\RewindableGenerator;
use Symfony\Component\DependencyInjection\ContainerInterface;
use Symfony\Component\DependencyInjection\Exception\RuntimeException;

/**
 * @internal This class has been auto-generated by the Symfony Dependency Injection Component.
 */
class getTurbo_Broadcaster_ActionRendererService extends App_KernelTestDebugContainer
{
    /**
     * Gets the private 'turbo.broadcaster.action_renderer' shared service.
     *
     * @return \Symfony\UX\Turbo\Broadcaster\TwigBroadcaster
     */
    public static function do($container, $lazyLoad = true)
    {
        include_once \dirname(__DIR__, 3).'/TP1/vendor/symfony/ux-turbo/src/Broadcaster/BroadcasterInterface.php';
        include_once \dirname(__DIR__, 3).'/TP1/vendor/symfony/ux-turbo/src/Broadcaster/TwigBroadcaster.php';

        return $container->privates['turbo.broadcaster.action_renderer'] = new \Symfony\UX\Turbo\Broadcaster\TwigBroadcaster(($container->privates['turbo.broadcaster.action_renderer.inner'] ?? $container->load('getTurbo_Broadcaster_ActionRenderer_InnerService')), ($container->privates['twig'] ?? self::getTwigService($container)), ['App\\Entity\\' => 'broadcast/'], ($container->privates['turbo.id_accessor'] ?? $container->load('getTurbo_IdAccessorService')));
    }
}

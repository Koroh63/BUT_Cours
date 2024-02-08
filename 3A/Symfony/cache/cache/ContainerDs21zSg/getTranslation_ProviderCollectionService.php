<?php

namespace ContainerDs21zSg;

use Symfony\Component\DependencyInjection\Argument\RewindableGenerator;
use Symfony\Component\DependencyInjection\ContainerInterface;
use Symfony\Component\DependencyInjection\Exception\RuntimeException;

/**
 * @internal This class has been auto-generated by the Symfony Dependency Injection Component.
 */
class getTranslation_ProviderCollectionService extends App_KernelTestDebugContainer
{
    /**
     * Gets the private 'translation.provider_collection' shared service.
     *
     * @return \Symfony\Component\Translation\Provider\TranslationProviderCollection
     */
    public static function do($container, $lazyLoad = true)
    {
        include_once \dirname(__DIR__, 3).'/TP1/vendor/symfony/translation/Provider/TranslationProviderCollection.php';

        return $container->privates['translation.provider_collection'] = ($container->privates['translation.provider_collection_factory'] ?? $container->load('getTranslation_ProviderCollectionFactoryService'))->fromConfig([]);
    }
}

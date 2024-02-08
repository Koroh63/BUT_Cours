<?php

namespace ContainerDs21zSg;

use Symfony\Component\DependencyInjection\Argument\RewindableGenerator;
use Symfony\Component\DependencyInjection\ContainerInterface;
use Symfony\Component\DependencyInjection\Exception\RuntimeException;

/**
 * @internal This class has been auto-generated by the Symfony Dependency Injection Component.
 */
class getForm_RegistryService extends App_KernelTestDebugContainer
{
    /**
     * Gets the private 'form.registry' shared service.
     *
     * @return \Symfony\Component\Form\FormRegistry
     */
    public static function do($container, $lazyLoad = true)
    {
        include_once \dirname(__DIR__, 3).'/TP1/vendor/symfony/form/FormRegistryInterface.php';
        include_once \dirname(__DIR__, 3).'/TP1/vendor/symfony/form/FormRegistry.php';

        return $container->privates['form.registry'] = new \Symfony\Component\Form\FormRegistry([($container->privates['form.extension'] ?? $container->load('getForm_ExtensionService'))], ($container->privates['form.resolved_type_factory'] ?? $container->load('getForm_ResolvedTypeFactoryService')));
    }
}

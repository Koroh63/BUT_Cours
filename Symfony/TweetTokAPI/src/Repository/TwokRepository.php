<?php

namespace App\Repository;

use App\Entity\Twok;
use Doctrine\Bundle\DoctrineBundle\Repository\ServiceEntityRepository;
use Doctrine\Persistence\ManagerRegistry;

/**
 * @extends ServiceEntityRepository<Twok>
 *
 * @method Twok|null find($id, $lockMode = null, $lockVersion = null)
 * @method Twok|null findOneBy(array $criteria, array $orderBy = null)
 * @method Twok[]    findAll()
 * @method Twok[]    findBy(array $criteria, array $orderBy = null, $limit = null, $offset = null)
 */
class TwokRepository extends ServiceEntityRepository
{
    public function __construct(ManagerRegistry $registry)
    {
        parent::__construct($registry, Twok::class);
    }

//    /**
//     * @return Twok[] Returns an array of Twok objects
//     */
//    public function findByExampleField($value): array
//    {
//        return $this->createQueryBuilder('t')
//            ->andWhere('t.exampleField = :val')
//            ->setParameter('val', $value)
//            ->orderBy('t.id', 'ASC')
//            ->setMaxResults(10)
//            ->getQuery()
//            ->getResult()
//        ;
//    }

//    public function findOneBySomeField($value): ?Twok
//    {
//        return $this->createQueryBuilder('t')
//            ->andWhere('t.exampleField = :val')
//            ->setParameter('val', $value)
//            ->getQuery()
//            ->getOneOrNullResult()
//        ;
//    }
}

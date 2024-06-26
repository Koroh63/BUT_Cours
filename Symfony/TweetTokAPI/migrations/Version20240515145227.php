<?php

declare(strict_types=1);

namespace DoctrineMigrations;

use Doctrine\DBAL\Schema\Schema;
use Doctrine\Migrations\AbstractMigration;

/**
 * Auto-generated Migration: Please modify to your needs!
 */
final class Version20240515145227 extends AbstractMigration
{
    public function getDescription(): string
    {
        return '';
    }

    public function up(Schema $schema): void
    {
        // this up() migration is auto-generated, please modify it to your needs
        $this->addSql('DROP TABLE messenger_messages');
        $this->addSql('CREATE TEMPORARY TABLE __temp__twok AS SELECT id, auteur, message, date FROM twok');
        $this->addSql('DROP TABLE twok');
        $this->addSql('CREATE TABLE twok (id INTEGER NOT NULL, auteur VARCHAR(255) DEFAULT NULL, message VARCHAR(255) DEFAULT NULL, date VARCHAR(255) DEFAULT NULL, PRIMARY KEY(id))');
        $this->addSql('INSERT INTO twok (id, auteur, message, date) SELECT id, auteur, message, date FROM __temp__twok');
        $this->addSql('DROP TABLE __temp__twok');
    }

    public function down(Schema $schema): void
    {
        // this down() migration is auto-generated, please modify it to your needs
        $this->addSql('CREATE TABLE messenger_messages (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, body CLOB NOT NULL COLLATE "BINARY", headers CLOB NOT NULL COLLATE "BINARY", queue_name VARCHAR(190) NOT NULL COLLATE "BINARY", created_at DATETIME NOT NULL, available_at DATETIME NOT NULL, delivered_at DATETIME DEFAULT NULL)');
        $this->addSql('CREATE INDEX IDX_75EA56E016BA31DB ON messenger_messages (delivered_at)');
        $this->addSql('CREATE INDEX IDX_75EA56E0E3BD61CE ON messenger_messages (available_at)');
        $this->addSql('CREATE INDEX IDX_75EA56E0FB7336F0 ON messenger_messages (queue_name)');
        $this->addSql('CREATE TEMPORARY TABLE __temp__twok AS SELECT id, auteur, message, date FROM twok');
        $this->addSql('DROP TABLE twok');
        $this->addSql('CREATE TABLE twok (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, auteur VARCHAR(255) DEFAULT NULL, message VARCHAR(255) DEFAULT NULL, date VARCHAR(255) DEFAULT NULL)');
        $this->addSql('INSERT INTO twok (id, auteur, message, date) SELECT id, auteur, message, date FROM __temp__twok');
        $this->addSql('DROP TABLE __temp__twok');
    }
}

#include <stdio.h>
#include <stdlib.h>
#include <sys/shm.h>
#include <sys/ipc.h>
#include <sys/stat.h>
#include <unistd.h>
#include <sys/types.h>
#include <errno.h>
#include <pthread.h>
#include <semaphore.h>

#define TAILLE 5 //tampon circulaire de taille 5

struct tampon {
  char zone[TAILLE];
  unsigned int lecture;
  unsigned int ecriture;
  sem_t r;
  sem_t w;
  sem_t mutex;

};

int main()
{
    char c;
    int segment_id;
    struct tampon * t;
    printf("Write a character to put : \n");
    scanf("%c", &c);

    segment_id = shmget (ftok("~",geteuid()), sizeof(struct tampon),S_IRUSR | S_IWUSR );

    if (segment_id == -1) {
        perror("erreur création segment");
        exit(errno);
    }


    /* Attache le segment de mémoire partagée. */
    t = (struct tampon*)  shmat (segment_id, 0, 0);
    sem_wait(&t->w);
    sem_wait(&t->mutex);

    t->zone[t->ecriture] = c;
    t->ecriture  = ( t->ecriture + 1 ) % 5;

    sem_post(&t->mutex);
    sem_post(&t->r);

}
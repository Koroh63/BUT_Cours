#include <stdio.h>
#include <stdlib.h>
#include <sys/shm.h>
#include <sys/ipc.h>
#include <sys/stat.h>
#include <unistd.h>
#include <sys/types.h>
#include <errno.h>
#include <pthread.h>
#include <sys/sem.h>
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


int main ()
{

  int segment_id;
  struct tampon * t;
  /* Alloue le segment de mémoire partagée. */
  /* la clef est générée avec le répertoire HOME et le numéro UID */
  segment_id = shmget (ftok("~",geteuid()), sizeof(struct tampon),
                       IPC_CREAT | IPC_EXCL | S_IRUSR | S_IWUSR);

  if (segment_id == -1) {
          perror("erreur création segment");
          exit(errno);
  }
  /* Attache le segment de mémoire partagée. */
  t = (struct tampon*)  shmat (segment_id, 0, 0);

  /* Init valeurs tampon */
  if (sem_init(&(t->r),1,0)) {
    perror("erreur création semaphore lecture");
    exit(errno);
  }
  if (sem_init(&(t->w),1,TAILLE)) {
    perror("erreur création semaphore lecture");
    exit(errno);
  }
  if (sem_init(&(t->mutex),1,1)) {
    perror("erreur création semaphore lecture");
    exit(errno);
  }

  printf("le SHM n° %d a été créé. Vous pouvez maintenant jouer avec des producteurs et consommateurs\n",segment_id);

  /* Détache le segment de mémoire partagée. */
  shmdt (t);

  /* mais ne le libère pas pour que les producteurs et consommateurs l'utilisent grâce à la clef  */
 // shmctl (segment_id, IPC_RMID, 0);

  return 0;
}
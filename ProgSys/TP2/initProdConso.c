#include <stdio.h>
#include <stdlib.h>
#include <sys/shm.h>
#include <sys/ipc.h>
#include <sys/stat.h>
#include <unistd.h>
#include <sys/types.h>
#include <errno.h>


#define TAILLE 5 //tampon circulaire de taille 5

struct tampon {
  char zone[TAILLE];
  unsigned int lecture;
  unsigned int ecriture;
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
  t->lecture=0;
  t->ecriture=0;

  printf("le SHM n° %d a été créé. Vous pouvez maintenant jouer avec des producteurs et consommateurs\n",segment_id);

  /* Détache le segment de mémoire partagée. */
  shmdt (t);

  /* mais ne le libère pas pour que les producteurs et consommateurs l'utilisent grâce à la clef  */
 // shmctl (segment_id, IPC_RMID, 0);

  return 0;
}
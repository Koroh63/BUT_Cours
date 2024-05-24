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

#define TAILLE 5 //tampon circulaire de taille 5

struct tampon {
  char zone[TAILLE];
  unsigned int lecture;
  unsigned int ecriture;
}; 

int main()
{
    char c;
    int segment_id;
    struct tampon * t;

    segment_id = shmget (ftok("~",geteuid()), sizeof(struct tampon),S_IRUSR | S_IWUSR);

    if (segment_id == -1) {
        perror("erreur création segment");
        exit(errno);
    }
    
    t = (struct tampon*)  shmat (segment_id, 0, 0);

    c=t->zone[t->lecture];
    t->lecture = ( t->lecture + 1 ) % 5;

    printf("Character putted is : %s \n",&c);

}
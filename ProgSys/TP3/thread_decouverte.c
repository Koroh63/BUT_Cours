#include <pthread.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/syscall.h>
#include <stdlib.h>

#define VALEUR 50

void* thread_function (void* arg)
{
  int* v=(int*)arg;
 int i,cpt=0;
  printf ( "Le pid du thread fils est %d\n", (int) getpid ());
  printf("le tid du thread fils est %d\n",syscall(SYS_gettid));
  printf("l'id du thread fils est %lu\n", pthread_self());


  
  /* Boucle de  VALEUR/2 +1 à VALEUR */
  for(i=*v/2+1 ; i<=VALEUR ; i++)
  {
         cpt++; printf("f:%d\n",i);
  }
  puts("Vous avez 10 secondes pour faire un ps -elf");
  sleep(10);
  exit(2);
}

int main ()
{
  int v=VALEUR,i,ret;

  pthread_t thread;
  printf( "Le pid du processus principal est %d\n",(int)getpid());
  printf("le tid du thread principal est %d\n",syscall(SYS_gettid));
  printf("l'id du thread principal est %lu\n", pthread_self());
  pthread_create (&thread, NULL, &thread_function, (void *) &v);
  
  
  /* Boucle de 0 à VALEUR/2 */
  for(i=0 ; i<v/2 ; i++)
          printf("p:%d\n",i);
  pthread_join(thread,(void*) &ret);
  printf("le thread fils a retourné %d\n", ret);
  return 0;
}
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <time.h>
#include <unistd.h>
#include <pthread.h>

#define N_INF 50
#define N_SUP 100
#define TIMEOUT 20
#define LG 80
#define M_MAX 10

struct param {
    unsigned int t;
    int randNum;
};

pthread_mutex_t lock; // Declare the mutex

void* compteArebours(void* arg) {
    struct param *params = (struct param*) arg;
    sleep(params->t);
    puts("Temps écoulé ! Désolé ! C'est perdu !");
    exit(0);
}

void* modifierNbreMystere(void* arg) {
    struct param *params = (struct param*) arg;
    unsigned int duree = params->t / 3;
    unsigned int n;
    for (unsigned int i = 1; i < 3; i++) {
        n = rand() % M_MAX + 1;
        sleep(duree);
        pthread_mutex_lock(&lock); // Lock the mutex before modifying params
        if (rand() % 2) {
            printf("\nLe nombre mystère a été augmenté de %u\n", n);
            params->randNum += n;
        } else {
            printf("\nLe nombre mystère a été diminué de %u\n", n);
            params->randNum -= n;
        }
        pthread_mutex_unlock(&lock); // Unlock the mutex after modifying params
    }
    pthread_exit(NULL);
}

int main(int argc, char* argv[]) {
    srand(time(NULL));  // Seed the random number generator

    unsigned int proposition = 0;
    unsigned int temps = TIMEOUT;
    char ligne[LG];
    int r;

    if (argc == 2) {
        if (sscanf(argv[1], "%u", &temps) != 1) {
            temps = TIMEOUT; // Use default time if parameter is incorrect
        }
    }

    int randNum = rand() % (N_SUP - N_INF + 1) + N_INF;
    struct param params;
    params.randNum = randNum;
    params.t = temps;

    pthread_mutex_init(&lock, NULL); // Initialize the mutex

    pthread_t threadRand;
    pthread_t threadTime;

    pthread_create(&threadTime, NULL, compteArebours, (void*)&params);
    pthread_create(&threadRand, NULL, modifierNbreMystere, (void*)&params);

    printf("Trouvez un entier positif entre %u et %u\n", N_INF, N_SUP);
    printf("Vous avez %u secondes ! Bonne chance\n", temps);

    do {
        printf("Quelle est votre proposition ? : ");
        fgets(ligne, LG, stdin);
        r = sscanf(ligne, "%u", &proposition);
        if (r == 1) {
            pthread_mutex_lock(&lock); // Lock the mutex before accessing params
            if (proposition > params.randNum) {
                puts("Trop grand !");
            } else if (proposition < params.randNum) {
                puts("Trop petit !");
            } else {
                pthread_mutex_unlock(&lock); // Unlock the mutex before breaking
                break;
            }
            pthread_mutex_unlock(&lock); // Unlock the mutex after accessing params
        }
    } while (proposition != params.randNum);

    puts("Bravo ! C'est gagné !");


    pthread_mutex_destroy(&lock); // Destroy the mutex

        exit(0);
}

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include "cards.h"

// Initialize the deck
void initialize_deck(Card deck[]) {
    const char *suits[] = {"H", "D", "C", "S"};
    const char *ranks[] = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"};
    
    int i, j, k;
    for (k = 0; k < 8; k++) {
        for (i = 0; i < 4; i++) {
            for (j = 0; j < 13; j++) {
                int idx = k * 52 + i * 13 + j;
                deck[idx].suit = suits[i];
                deck[idx].rank = ranks[j];
                deck[idx].value = 1; // 2-10, J=12, Q=13, K=14, A=15 (adjust as needed)
            }
        }
    }
}

// Shuffle the deck
void shuffle_deck(Card deck[]) {
    for (int i = 0; i < 416; i++) {
        int r = rand() % 416;
        Card temp = deck[i];
        deck[i] = deck[r];
        deck[r] = temp;
    }
}

// Print the deck
void print_deck(Card deck[]) {
    for (int i = 0; i < 416; i++) {
        printf("%s of %s\n", deck[i].rank, deck[i].suit);
    }
}




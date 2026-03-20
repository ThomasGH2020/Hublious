#include <stdio.h>
#include "cards.h"
#include <stdlib.h>
#include <time.h>
#include <string.h>

void print_hand(Card deck[], int currentCard);
void print_card(Card card);

int main(void) {
    Card deck[416];
    srand(time(NULL));

    initialize_deck(deck);
    shuffle_deck(deck);
    int currentCard = 0;
    while (currentCard < 416) {
        printf("%d ",currentCard);
        print_hand(deck,currentCard);

        currentCard += 4;
    }
}

void print_hand(Card deck[], int currentCard) {
    print_card(deck[currentCard]);
    printf(" ");
    print_card(deck[currentCard+2]);
    printf(", ");
    print_card(deck[currentCard+1]);
    printf(" ");
    print_card(deck[currentCard+3]);
    printf("\n");
}

void print_card(Card card) {
    printf("%s%s",card.rank,card.suit);
}
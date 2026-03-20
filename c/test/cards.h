// Define structures for the card and deck
typedef struct {
    const char *suit;
    const char *rank;
    int value; // 1 if card is yet to be played, -1 if card has been played
} Card;

void initialize_deck(Card deck[]);
void shuffle_deck(Card deck[]);
void print_deck(Card deck[]);
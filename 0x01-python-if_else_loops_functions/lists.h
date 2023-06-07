#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>
#include <stdio.h>

listint_t *create_node(int number);
listint_t *insert_node(listint_t **head, int number);
#endif

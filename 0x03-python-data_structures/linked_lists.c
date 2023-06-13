#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

/**
 * print_listint - prints elements of list
 * @head: pointer to h
 *
 * Return:  nodes number
 */

size_t print_listint(const listint_t *h)
{
    ssize_t n;
    const listint_t *current;
    current = h;
    n = 0;

    while (current != NULL)
    {
        printf("%d", current->n);
        current = current->next;
        n++;
    }
    printf("\n");
    return (n);
}

/**
 * add_nodeint_end - adds nodes to list
 * @head: pointer to head
 * @n: number of nodes added
 *
 * Return:  nodes number
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
    listint_t *new_node;
    listint_t *current;
    current  = *head;

    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return (NULL);

    new_node->n = n;
    new_node->next = NULL;
	
    if (*head == NULL)
	*head = new_node; 
    else
    {
        while (current->next != NULL)
        {
            current = current->next;
        }
            current->next = new_node;
    }
        return (new_node);
}


/**
 * free_listint - frees elements of list
 * @head: pointer to head
 *
 * Return:  nodes number
 */

void free_listint(listint_t *head)
{
 listint_t *current;
    listint_t *next;
    current = head;

    while (current != NULL)
    {
        current = next;
	next = current->next;
        free(current);
    }
}


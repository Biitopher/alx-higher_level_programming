#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

/**
 * reverseList - reverse all elements of list
 * @head: pointer to head
 *
 * Return:  nodes number 
 */

listint_t *reverseList(listint_t *head)
{
    listint_t *prev = NULL;
    listint_t *current = head;
    listint_t *next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    return (prev);
}

/**
 * is_palindrome - function that checks if list is palindrome
 * @head: pointer to head
 *
 * Return: nodes number
 */

int is_palindrome(listint_t **head)
{
listint_t *slow;
listint_t *fast;
listint_t *prev;
listint_t *mid;
if (*head == NULL)
{
return (1);
}
slow = *head;
fast = *head;
while (fast != NULL && fast->next != NULL)
{
slow = slow->next;
fast = fast->next->next;
}
prev = reverseList(slow);
mid = *head;
while (prev != NULL)
{
if (mid->n != prev->n)
{
return (0);
}
mid = mid->next;
prev = prev->next;
}
return (1);
}

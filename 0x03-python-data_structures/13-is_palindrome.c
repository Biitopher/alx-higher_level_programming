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
 * print_listint - prints elements of list
 * @head: pointer to h
 *
 * Return:  nodes number
 */

size_t print_listint(const listint_t *h)
{
    size_t size = 0;
    const listint_t *current = h;

    while (current != NULL)
    {
        printf("%d ", current->h);
        current = current->next;
        size++;
    }
    printf("\n");
    return (size);
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
    listint_t n;
        if (*head == NULL)
    {
        *head = new_node;
    }
    else
    {
        listint_t *current = *head;
        
        while (current->next != NULL)
        {
            current = current->next;
        }
            current->next = new_node;
    }
        return (n);

/**
 * free_listint - frees elements of list
 * @head: pointer to head
 *
 * Return:  nodes number 
 */

void free_listint(listint_t *head)
{
 listint_t *current = head;
    listint_t *next;

    while (current != NULL)
    {
        next = current->next;
        free(current);
        current = next;
    }
}

/**
 * is_palindrome - function that checks if list is palindrome
 * @head: pointer to head
 *
 * Return: nodes number
 */

int is_palindrome(listint_t **head)
{
 listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev = NULL;
    listint_t *mid = NULL;
    int isPalindrome = 1;

    if (*head == NULL || (*head)->next == NULL)
    {
        return (isPalindrome); 

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev = slow;
        slow = slow->next;
    }

    if (fast != NULL)
    {
        mid = slow;
        slow = slow->next;
    }

    prev->next = NULL;
    listint_t *current = slow;
    listint_t *next = NULL;
    prev = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    {
    return (0);
    }
    }

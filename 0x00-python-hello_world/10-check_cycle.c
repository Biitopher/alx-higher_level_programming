#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: list to be linked
 * Return: 0 on fail and 1 on success
 */

int check_cycle(listint_t *list)
{
	listint_t *start = list;
	listint_t *end = list;

	if (!list)
		return (0);
	while(start && end && end ->next)
	{
		start = start->next;
		end = end->next->;
		if (start == end)
			return (1);
	}
	return (0);
}


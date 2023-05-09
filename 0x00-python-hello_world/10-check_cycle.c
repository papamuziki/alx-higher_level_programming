#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to list elements
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slw = list;
	listint_t *fst = list;

	if (!list)
		return (0);

	while(slw && fst && fst->next)
	{
		fst = fst->next->next;
		slw = slw->next;

		if(slw == fst)
			return (-1);
	}
	return (0);
}

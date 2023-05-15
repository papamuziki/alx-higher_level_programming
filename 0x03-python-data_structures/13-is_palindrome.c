#include "lists.h"

/**
 * list_length - finds the length of a list
 * @head - 
 *
 * Return: Length of a list
 */
int list_length(listint_t *head)
{
	int length;

	for (length = 0; head; length++)
		head = head->next;
	return (length);
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int m;
	int len;
	int half_list;
	int *full_list;
	listint_t *tmp = *head;

	if(!head)
		return (1);

	len = list_length(tmp);
	full_list = malloc(sizeof(int) * len);
	if (!full_list)
		return (1);

	for (m = 0; tmp; m++)
	{
		full_list[m] = tmp->n;
		tmp = tmp->next;
	}

	half_list = m / 2;

	for (m = 0; m < half_list; m++)
	{
		if (full_list[m] != full_list[len - (m + 1)])
			return (0);
		else
			continue;
	}
	return (1);

}

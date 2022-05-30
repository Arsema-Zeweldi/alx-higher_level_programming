#include "lists.h"

/**
 * check_cycle - checks for a cycle
 * @list: list to check
 * Return: int
 */
int check_cycle(listint_t *list)
{
	listint_t *current;

	if (list == NULL)
		return (0);

	current = list->next;

	while (current != NULL)
	{
		if (current == list)
			return (1);
		current = current->next;
	}

	return (0);
}

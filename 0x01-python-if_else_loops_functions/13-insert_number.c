#include "lists.h"

/**
 * insert_node - inserts a new node
 *
 * @head: head
 * @number: index
 *
 * Return: listint_t
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *hd;
	listint_t *hd_tmp;

	hd = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	while (hd != NULL)
	{
		if (hd->n > number)
			break;
		hd_tmp = hd;
		hd = hd->next;
	}

	new->n = number;
	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
	}
	else
	{
		new->next = hd;
		if (hd == *head)
			*head = new;
		else
			hd_tmp->next = new;
	}
	return (new);
}

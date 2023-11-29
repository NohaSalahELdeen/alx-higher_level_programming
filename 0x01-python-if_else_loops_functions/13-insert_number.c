#include "lists.h"
/**
  * insert_node -  inserts a number into a sorted singly linked list.
  * @head: pointer point to the list.
  * @number: number to insert.
  * Return: the address of the new node, or NULL if it failed.
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *insert_new, *ptr;

	if (*head == NULL)
		return (NULL);

	insert_new = malloc(sizeof(listint_t));
	if (insert_new == NULL)
		return (NULL);

	insert_new->n = number;
	insert_new->next = NULL;

	ptr = *head;
	while (ptr != NULL && ptr->next->n < number)
		ptr = ptr->next;
	insert_new->next = ptr->next;
	ptr->next = insert_new;

	return (insert_new);
}

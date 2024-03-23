#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to pointer.
 * @number: number to insert in the node.
 * Return: the address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *ptr;

	ptr = *head;
	if (head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
		*head = new_node;

	if (number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		while (ptr->next != NULL && ptr->next->n < number)
			ptr = ptr->next;
		new_node->next = ptr->next;
		ptr->next = new_node;
	}
	return (*head);
}

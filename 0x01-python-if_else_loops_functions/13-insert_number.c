#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer of the head of the list
 * @number: integer to be inserted
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node, *current, *prev;

    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return (NULL);

    new_node->n = number;
    new_node->next = NULL;

    current = *head;
    prev = NULL;

    while (current != NULL && current->n < number)
    {
        prev = current;
        current = current->next;
    }

    if (prev == NULL)
    {
        new_node->next = *head;
        *head = new_node;
    }
    else
    {
        new_node->next = prev->next;
        prev->next = new_node;
    }

    return (new_node);
}
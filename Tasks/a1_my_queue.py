"""
My little Queue
"""
from typing import Any

l2 = [2,4,6,7]

def enqueue(elem: Any) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    global l
    l2.append(elem)

    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if no elements.

    :return: dequeued element
    """
    global l2
    if len(l2) == 0:
        return None
    else:
        start = l2[0]
        l2.pop(0)
        return start


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    global l2
    if ind > len(l2)-1:
        return None
    else:
        return l2[ind]



def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    global l2
    l2 = []
    return None

if __name__ == "__main__":
    clear()
    print(l2)
class ListNode:

    def __init__(self, value):
        self.value = value
        self.next = None


def merge(list1: ListNode | None, list2: ListNode | None):
    if list1 is None and list2:
        return list2
    elif list1 and list2 is None:
        return list1
    elif list1 is None and list2 is None:
        return None

    if list1.value <= list2.value:
        result_head = list1
        list1 = list1.next
    else:
        result_head = list2
        list2 = list2.next

    current = result_head
    while list1 and list2:
        if list1.value <= list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    current.next = list1 or list2
    return result_head


def merge_dummy(list1: ListNode | None, list2: ListNode | None):
    dummy = ListNode(None)
    current = dummy
    while list1 and list2:
        if list1.value <= list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    current.next = list1 or list2
    return dummy.next






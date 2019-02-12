def FetchOneRow(Table, Args):
    try:
        result = Table.objects.get(Args)
    except Table.DoesNotExist:
        return [0]
    else:
        return [1, result]


def FetchAllRows(Table, Args):
    result = Table.objects.filter(Args)
    if not result:
        return [0]
    else:
        return [1, result]

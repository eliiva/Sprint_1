types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

def delete_dobbles(tickets):
    for i in range(1, len(tickets)):
        for ticket_to_check in tickets[i]:
            for j in range(i+1, len(tickets)+1):
                for ticket_delete_candidate in tickets[j]:
                    if ticket_to_check == ticket_delete_candidate:
                        tickets[j].remove(ticket_delete_candidate)
    return tickets

def get_tickets_by_type(types, tickets):
    tickets_by_type = {}
    filtered_tickets = delete_dobbles(tickets)
    for i in range(1, len(types)+1):
        tickets_by_type[types[i]] = filtered_tickets[i]
    return tickets_by_type

print(get_tickets_by_type(types, tickets))
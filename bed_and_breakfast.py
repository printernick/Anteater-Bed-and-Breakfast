import datetime
from collections import defaultdict

def add_reservation(res, start, end, conf_count, instructions) -> None:

    ind_reservation = []
    

    ind_reservation.append(start)
    ind_reservation.append(end)
    ind_reservation.append(' '.join(instructions[4:]))
    ind_reservation.append(conf_count)
    res[instructions[1]].append(ind_reservation)
    print(
        'Reserving room {room} for {name} - - Confirmation #{num} \n \
(arriving {arrive}, departing {depart})'.format(
                room = instructions[1],
                name = ' '.join(instructions[4:]),
                num = conf_count,
                arrive = '{}/{}/{}'.format(
                    start.month, start.day, start.year),
                depart = '{}/{}/{}'.format(
                    end.month, end.day, end.year)))

def reservation_leave_before_msg(start_date, end_date, list_of_instr) -> None:
    print(
        "Sorry, can't reserve room {rm} ({arri} to {depart}); \n\
    can't leave before you arrive.".format(
    rm = list_of_instr[1],
    arri = '{}/{}/{}'.format(
        start_date.month, start_date.day, start_date.year),
    depart = '{}/{}/{}'.format(
        end_date.month, end_date.day, end_date.year)))

def reservation_same_day_msg(start_date, end_date, list_of_instr) -> None:
    print(
        "Sorry, can't reserve room {rm} ({arri} to {depart}); \n\
    can't arrive and leave on the same day.".format(
    rm = list_of_instr[1],
    arri = '{}/{}/{}'.format(
        start_date.month, start_date.day, start_date.year),
    depart = '{}/{}/{}'.format(
        end_date.month, end_date.day, end_date.year)))

def no_reservation_num_msg(list_of_instr) -> None:
    print(
        "Sorry, can't cancel reservation; no confirmation number {}" \
        .format(list_of_instr[1]))

def count_reservations(reservations: dict) -> int:
    counter = 0
    for key in reservations:
        for ind_reservations in reservations[key]:
            counter += 1
    return counter

def print_reservations_for_room(list_of_instr: list, reservations: defaultdict) -> None:
    print(
        'Reservations for room {}:'.format(list_of_instr[1]))
    for arrival, depart, guest, num in reservations[list_of_instr[1]]:
        print(
            '   {:>2}/{:>2}/{:>4} to {:>2}/{:>2}/{:>4}:  {}'.format(
                arrival.month, arrival.day, arrival.year, \
                depart.month, depart.day, depart.year, guest))

def print_reservations_for_guest(list_of_instr: list, reservations: defaultdict) -> None:
    name = ' '.join(list_of_instr[1:])
    print(
        'Reservations for {}:'.format(name))
    for key in reservations:
        for arrival, depart, guest, num in reservations[key]:
            if name == guest:
                print(
                    '   {:>2}/{:>2}/{:>4} to {:>2}/{:>2}/{:>4}:  room {}'.format(
                        arrival.month, arrival.day, arrival.year, \
                        depart.month, depart.day, depart.year, key))

def print_list_arrivals(list_of_instr: list, reservations: defaultdict) -> None:
    month, day, year = list_of_instr[1].split('/')
    date = datetime.date(int(year), int(month), int(day))
    
    print(
        'Guests arriving on {}/{}/{}:'.format(date.month, date.day, date.year))
    for key in reservations:
        for arrival, depart, guest, num in reservations[key]:
            if date == arrival:
                print(
                    '   {} (room {})'.format(guest, key))
                
def print_list_departures(list_of_instr: list, reservations: defaultdict) -> None:
    month, day, year = list_of_instr[1].split('/')
    date = datetime.date(int(year), int(month), int(day))
    
    print(
        'Guests departing on {}/{}/{}:'.format(date.month, date.day, date.year))
    for key in reservations:
        for arrival, depart, guest, num in reservations[key]:
            if date == depart:
                print(
                    '   {} (room {})'.format(guest, key))

def print_list_free_bedrooms(list_of_instr: list, reservations: defaultdict) -> None:
    month, day, year = list_of_instr[1].split('/')
    start_date = datetime.date(int(year), int(month), int(day))
                
    month, day, year = list_of_instr[2].split('/')
    end_date = datetime.date(int(year), int(month), int(day))
    print(
        'Bedrooms free between {}/{}/{} to {}/{}/{}:'.format(
            start_date.month, start_date.day, start_date.year,
            end_date.month, end_date.day, end_date.year))
    for key in reservations:
        for arrival, departure, guest, conf in reservations[key]:
            if start_date < departure and end_date > arrival:
                break
        else:
            print(' ', key)

def print_list_occupied_bedrooms(list_of_instr: list, reservations: defaultdict) -> None:
    month, day, year = list_of_instr[1].split('/')
    start_date = datetime.date(int(year), int(month), int(day))
                
    month, day, year = list_of_instr[2].split('/')
    end_date = datetime.date(int(year), int(month), int(day))
    print(
        'Bedrooms occupied between {}/{}/{} to {}/{}/{}:'.format(
            start_date.month, start_date.day, start_date.year,
            end_date.month, end_date.day, end_date.year))
    for key in reservations:
        for arrival, departure, guest, conf in reservations[key]:
            if start_date < departure and end_date > arrival:
                print(' ', key)

def order_by_arrival_date(reservations: dict) -> None:
    arrival_dates = []
    for rm in reservations:
        for arrival, departure, guest, conf in reservations[rm]:
            arrival_dates.append(arrival)
    return sorted(arrival_dates)

def bed_and_breakfast(file: str) -> None:
    instructions = open(file, 'r')
    bedrooms = []
    reservations = defaultdict(list)
    conf_counter = 0
    
    for line in instructions:
        list_of_instr = " ".join(line.split()).split()
        if list_of_instr[0].lower() == 'nb' or list_of_instr[0].lower() == 'ab':
            if list_of_instr[1] not in bedrooms:
                bedrooms.append(list_of_instr[1])
                reservations[list_of_instr[1]] = []
            else:
                print(
                    "Sorry, can't add room {} again; it's already on the list." \
                    .format(list_of_instr[1]))
                
        elif list_of_instr[0].lower() == 'lb':
            print('Number of bedrooms in service: ' + str(len(bedrooms)))
            print('------------------------------------')
            if len(bedrooms) >= 1:
                for room in sorted(bedrooms):
                    print(room)
                    
        elif list_of_instr[0].lower() == 'pl':
            print(' '.join(list_of_instr[1:]))
            
        elif list_of_instr[0].lower() == 'db':
            if list_of_instr[1] not in bedrooms:
                print(
                    "Sorry, can't delete room {}; it is not in service now" \
                    .format(list_of_instr[1]))
            else:
                bedrooms.remove(list_of_instr[1])
                if list_of_instr[1] in reservations:
                    for arrival, departure, guest, conf in reservations[list_of_instr[1]]:
                        print(
                            'Deleting room {rm} forces cancellation of this reservation: \n\
   {name} arriving {arr} and departing {dep} (Conf. #{conf})'.format(
       rm = list_of_instr[1],
       name = guest,
       arr = '{}/{}/{}'.format(
            arrival.month, arrival.day, arrival.year),
       dep = '{}/{}/{}'.format(
            departure.month, departure.day, departure.year),
       conf = conf))
                    reservations.pop(list_of_instr[1])
                
        elif list_of_instr[0].lower() == 'rr':
            if list_of_instr[1] not in bedrooms:
                print("Sorry; can't reserve room {}; room not in service" \
                      .format(list_of_instr[1]))
            else:
                month, day, year = list_of_instr[2].split('/')
                start_date = datetime.date(int(year), int(month), int(day))
                
                month, day, year = list_of_instr[3].split('/')
                end_date = datetime.date(int(year), int(month), int(day))

                if start_date > end_date:
                    reservation_leave_before_msg(start_date, end_date, list_of_instr)

                elif start_date == end_date:
                    reservation_same_day_msg(start_date, end_date, list_of_instr)

                elif list_of_instr[1] in reservations:
                    for arrival, departure, guest, num in reservations[list_of_instr[1]]:
                        if start_date <= departure and end_date > arrival:
                            print(
                                "Sorry, can't reserve room {rm} ({start} to {end}); \n\
   it's already booked (Conf. #{conf})".format(
       rm = list_of_instr[1],
        start = '{}/{}/{}'.format(
            start_date.month, start_date.day, start_date.year),
        end = '{}/{}/{}'.format(
            end_date.month, end_date.day, end_date.year),
       conf = num))
                            break
                    else:
                        conf_counter += 1
                    
                        add_reservation(
                            reservations, start_date, end_date, conf_counter, list_of_instr)
                    
                else:
                    conf_counter += 1
                    
                    add_reservation(
                        reservations, start_date, end_date, conf_counter, list_of_instr)
                    
        elif list_of_instr[0].lower() == 'lr':
            print(
                'Number of reservations: {} \n\
No. Rm. Arrive      Depart     Guest \n\
------------------------------------------------'.format(count_reservations(reservations)))
            list_of_ordered_arrivals = order_by_arrival_date(reservations)
            while len(list_of_ordered_arrivals) != 0:
                for rm in reservations:
                    for arrival, depart, guest, num in reservations[rm]:
                        if len(list_of_ordered_arrivals) >= 1:
                            if arrival == list_of_ordered_arrivals[0]:
                                print(
                                    '{conf}  {rm}  {arr}  {dep}  {guest}'.format(
                                        conf = num,
                                        rm = rm,
                                        arr = '{:>2}/{:>2}/{:>4}'.format(
                                            arrival.month, arrival.day, arrival.year),
                                        dep = '{:>2}/{:>2}/{:>4}'.format(
                                            depart.month, depart.day, depart.year),
                                        guest = guest))
                                if len(list_of_ordered_arrivals) >= 1:
                                    del list_of_ordered_arrivals[0]
                    
        elif list_of_instr[0].lower() == 'dr':
            for key in reservations:
                for ind_reservation in reservations[key]:
                    if int(list_of_instr[1]) in ind_reservation:
                        reservations[key].remove(ind_reservation)
                        
            else:
                no_reservation_num_msg(list_of_instr)

        elif list_of_instr[0].lower() == 'rb':
            print_reservations_for_room(list_of_instr, reservations)

        elif list_of_instr[0].lower() == 'rg':
            print_reservations_for_guest(list_of_instr, reservations)

        elif list_of_instr[0].lower() == 'la':
            print_list_arrivals(list_of_instr, reservations)

        elif list_of_instr[0].lower() == 'ld':
            print_list_departures(list_of_instr, reservations)

        elif list_of_instr[0].lower() == 'lf':
            print_list_free_bedrooms(list_of_instr, reservations)

        elif list_of_instr[0].lower() == 'lo':
            print_list_occupied_bedrooms(list_of_instr, reservations)

    instructions.close()
                    

if __name__ == '__main__':
    #bed_and_breakfast('sample1.txt')
    #bed_and_breakfast('sample2.txt')
    #bed_and_breakfast('sample3.txt')
    #bed_and_breakfast('sample4.txt')
    bed_and_breakfast('sample5.txt')

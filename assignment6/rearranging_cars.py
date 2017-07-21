
class Movement(object):
    """This class stores information about one movement,
    i.e. a car moving from position *fro* to position *to*.
    """

    def __init__(self, car, fro, to):
        self.car = car
        self.fro = fro
        self.to = to

    def print_movement(self):
        print("Move car %s from %s to %s" %(self.car, self.fro, self.to))

def rearrange(current_permutation, final_permutation):
    """Rearrange the cars so that their positions are in accordance to
    final_permutation.

    Args:
        current_permutation: the initial car permutation in the parking lot.
        final_permutation: the desired permutation.

    Returns:
        movements: a list of Movement objects. Represents the consecutive
                   movements needed to rearrange the cars from current_permutation
                   to final_permutation.
    """
    car_to_pos = dict(zip(current_permutation,
                          list(range(len(current_permutation)))
                         )
                     )
    movements = list()
    for pos, desired_car in enumerate(final_permutation):
        if desired_car != current_permutation[pos] and desired_car != 0:
            movements_one_car = rearrange_one_car(car_to_pos, current_permutation, desired_car, pos)
            movements.extend(movements_one_car)
    return movements

def rearrange_one_car(car_to_pos, current_permutation, car, pos):
    """Rearrange *car* from its current position to *pos*.

    Args:
        car_to_pos: a dict structure where key = car and value = position of the car.
        current_permutation: a list representing how the car is arranged right now.
                             Note that it is modified in this method.
        car: the car that shall be at position pos.
        pos: the target position of *car*.

    Returns:
        movements_one_car: a list of Movement required to move *car* to *pos*.
    """
    current_car = current_permutation[pos]
    movements_one_car = list()
    if current_car != 0:
        movements_one_car.append(switch_position_with_zero(car_to_pos,
                                                           current_permutation,
                                                           current_car
                                                          )
                                )
    movements_one_car.append(switch_position_with_zero(car_to_pos, current_permutation, car))
    return movements_one_car

def switch_position_with_zero(car_to_pos, current_permutation, c1):
    """Returns the movement needed to switch position of cars c1 and 0.
    Modifies car_to_pos and current_permutation on the go.
    """
    c1_current_pos, zero_current_pos = car_to_pos[c1], car_to_pos[0]
    current_permutation[c1_current_pos] = 0
    current_permutation[zero_current_pos] = c1
    car_to_pos[c1], car_to_pos[0] = zero_current_pos, c1_current_pos
    return Movement(c1, c1_current_pos, zero_current_pos)

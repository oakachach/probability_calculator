import random
import copy

class Hat :
    def __init__(self, **number_of_balls) :
        self.contents = list()
        for key, value in number_of_balls.items() :
            for i in range(0, value) :
                self.contents.append(key)
        
    
    def draw(self, number_of_balls_to_draw) :
        removed_balls = list()
        for i in range(0, number_of_balls_to_draw) :
            try :
                list_index = self.contents.index(random.choice(self.contents))
                removed_balls.append(self.contents.pop(list_index))
            except :
                break
        
        return removed_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments) :
    successful_experiments = 0
    balls_drawn = list()
    ball_list = copy.copy(hat.contents)
    expected_list = dict_to_array(expected_balls)
    for i in range(0, num_experiments) :
        balls_drawn = get_balls_drawn(num_balls_drawn, ball_list)
        if have_same_elements(balls_drawn, expected_list) :
            successful_experiments += 1

        # Resetting lists for next attempt.
        balls_drawn = list()
        ball_list = copy.copy(hat.contents)
    
    print()
    return successful_experiments / num_experiments


def have_same_elements(parent_array, son_array) :
    same_element = False
    for i in son_array :
        for j in parent_array :
            if i == j :
                same_element = True
                element_to_pop = j
                break
                
        if same_element == False :
            return False
        else :
            parent_array.pop(parent_array.index(element_to_pop))
            same_element = False

    return True
        

def dict_to_array(_dictionary) :
    array = list()
    for key, value in _dictionary.items() :
            for i in range(0, value) :
                array.append(key)

    return array


def get_balls_drawn(_num_balls_drawn, _ball_list) :
    _balls_drawn = list()
    for j in range(0, _num_balls_drawn) :
        try :
            list_index = _ball_list.index(random.choice(_ball_list))
            _balls_drawn.append(_ball_list.pop(list_index))
        except :
            break
    
    return _balls_drawn
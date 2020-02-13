class Fitness:

    def __init__(self, individual):
        self.individual = individual

        self.top_speed = 0.1
        self.position = (0, -0.8)

        # Uncomment for 2nd grade curve example
        # for 2nd_grade_curve
        # self.position = (-1.415, -1.0)

        size = individual.get_gene_length()
        self.positions = [None for i in range(size + 2)]
        self.positions[0] = self.position
        self.fitness = 0

        for i in range(size):
            current_position = self.positions[i]
            action = individual.get_gene(i)
            next_position = (current_position[0] + action.get_x() * self.top_speed, current_position[1] + action.get_y() * self.top_speed)
            self.positions[i + 1] = next_position
            if self.is_outside(next_position):
                break
            self.fitness = self.get_distance(next_position, (0, -0.8))
            self.fitness = next_position[1]

    def get_first_position(self):
        return self.positions[0]

    def get_last_position(self):
        for position in reversed(self.positions):
            if self.is_outside(position) == False:
                return position

    def is_outside(self, point):
        if point is None:
            return True
        # Uncomment for 2nd grade curve example
        # return is_polynomial_grade_2(point)
        dist = point[0] ** 2 / 2.5 + point[1] ** 2 / 1
        if dist < 0.36:
            return True
        if dist > 1:
            return True
        return False

    def is_polynomial_grade_2(self, point):
        func = (point[0]**2) * -1 + 1
        return abs(point[1]-func) > 0.4

    def get_score(self):
        return self.fitness

    def score(self, position):
        if position[0] < 0 and position[1] < 0:
            return 40 - self.get_distance(position, (-1.3, 0))
        elif position[0] < 0 and position[1] > 0:
            return 40 * 2 - self.get_distance(position, (0, 0.8))
        elif position[1] > 0:
            return 40 * 3 - self.get_distance(position, (1.3, 0))
        else:
            return 40 * 4 - self.get_distance(position, (0, 0.8))

    def get_distance(self, point_a, point_b):
        x = point_a[0] - point_b[0]
        y = point_a[1] - point_b[1]
        x = x ** 2
        y = y ** 2
        return x + y


from student_database import set_student, set_rating


def add_student():
    """Получение данных ученика от учителя и их передача для записи"""
    metric = input('Введите данные (Фамилия, Имя, класс через пробел): ').split(' ')
    set_student(metric)


    def put_rating():
        """Получение данных оценки от учителя и их предача для записи"""
        last_name = input('Введи Фамилию ученика: ')
        lesson = input('Введи название урока: ')
        rating = input('Введи оценку или несколько оценок через пробел: ')
        set_rating(last_name, lesson, rating)
        
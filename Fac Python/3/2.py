def person(name, sname, y_bir, city, email, phone):
    print(f'Имя: {name}, Фамилия: {sname} год рождения: {y_bir} Город проживания: {city}'
          f'E-mail: {email} номер телефона: {phone}')


if __name__ == "__main__":
    person(name='Loh', sname='lohovic', y_bir='1900', city='Moscow',
           email='asdadd@maa.ru', phone='+712345678910')

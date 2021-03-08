import json
import random


BRANCH_NAMES = ('Libertex', 'Epam', 'Google', 'Yandex', 'Gismart',
                'Innovise', 'PandaDoc', 'ITechArt', 'Itransition', 'Aras')

FIRST_NAMES = ('Wade', 'Dave', 'Seth', 'Ivan', 'Riley', 'Gilbert', 'Jorge', 'Dan', 'Brian', 'Roberto', 'Ramon',
              'Miles', 'Liam', 'Nathaniel', 'Ethan', 'Lewis', 'Milton', 'Claude', 'Joshua', 'Glen', 'Harvey',
              'Blake', 'Antonio', 'Connor', 'Julian', 'Aidan', 'Harold', 'Conner', 'Peter', 'Hunter', 'Eli',
              'Alberto', 'Carlos', 'Shane', 'Aaron', 'Marlin', 'Paul', 'Ricardo', 'Hector', 'Alexis', 'Adrian',
              'Kingston', 'Douglas', 'Gerald', 'Joey', 'Johnny', 'Charlie', 'Scott', 'Martin', 'Tristin', 'Troy',
              'Tommy', 'Rick', 'Victor', 'Jessie', 'Neil', 'Ted', 'Nick', 'Wiley', 'Morris', 'Clark', 'Stuart',
              'Orlando', 'Keith', 'Marion', 'Marshall', 'Noel', 'Everett', 'Romeo', 'Sebastian', 'Stefan', 'Robin',
              'Clarence', 'Sandy', 'Ernest', 'Samuel', 'Benjamin', 'Luka', 'Fred', 'Albert', 'Greyson', 'Terry',
              'Cedric', 'Joe', 'Paul', 'George', 'Bruce', 'Christopher', 'Mark', 'Ron', 'Craig', 'Philip', 'Jimmy',
              'Arthur', 'Jaime', 'Perry', 'Harold', 'Jerry', 'Shawn', 'Walter')

LAST_NAMES = ('Adams', 'Allen', 'Anderson', 'Armstrong', 'Atkinson', 'Bailey', 'Baker', 'Ball', 'Barker', 'Barnes',
              'Bell', 'Bennett', 'Booth', 'Bradley', 'Brooks', 'Brown', 'Burton', 'Butler', 'Campbell', 'Carter',
              'Chapman', 'Clarke', 'Cole', 'Collins', 'Cook', 'Cooper', 'Corbyn', 'Cox', 'Davidson', 'Davies',
              'Dawson', 'Dixon', 'Edwards', 'Elliott', 'Evans', 'Fisher', 'Fletcher', 'Ford', 'Foster', 'Fox',
              'Gibson', 'Graham', 'Grant', 'Gray', 'Green', 'Griffiths', 'Hall', 'Hamilton', 'Harris', 'Harrison',
              'Harvey', 'Henderson', 'Hill', 'Holmes', 'Howard', 'Hughes', 'Hunt', 'Hunter', 'Jackson', 'James',
              'Jenkins', 'Johnson', 'Johnston', 'Jones', 'Kelly', 'Kennedy', 'King', 'Knight', 'Lawrence', 'Lee',
              'Lewis', 'Lloyd', 'Marshall', 'Martin', 'Mason', 'Matthews', 'McDonald', 'Miller', 'Mitchell', 'Moore',
              'Morgan', 'Morris', 'Morrison', 'Murphy', 'Murray', 'Owen', 'Palmer', 'Parker', 'Payne', 'Pearce',
              'Pearson', 'Perry', 'Phillips', 'Powell', 'Price', 'Reid', 'Reynolds', 'Richards', 'Richardson',
              'Roberts')

POSITION_TITLES = ('Python', 'JAVA', 'FrontEnd', '.NET', 'Tester', 'Business Analyst', 'Project Manager', 'CEO', 'HR')


with open('branches.json', 'w') as json_file:
    result = []
    for i in BRANCH_NAMES:
        data = {}
        data['branch_name'] = i
        data['facade_image'] = 'default.jpg'
        data['longitude'] = random.uniform(0, 80)
        data['latitude'] = random.uniform(0, 80)
        result.append(data)
    json.dump(result, json_file)


def create_person(last_name):
    hundred = []
    for i in FIRST_NAMES:
        position_title = random.choice(POSITION_TITLES)
        person = {'last_name': last_name, 'first_name': i, 'position_title': position_title}
        hundred.append(person)
    return hundred


with open('persons.json', 'w') as file:
    result = []
    for i in LAST_NAMES:
        data = create_person(i)
        result += data
    json.dump(result, file)


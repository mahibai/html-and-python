from matplotlib import container
from browser import document ,html

container = document['container']
todo_list = html.H1("My to do list:")
container <= todo_list
items = ['go to school','eat dinner','watch tv']
for item in items:
    container <= html.LI(item)
from turing_machine_file import TuringMachine

T2 = TuringMachine()

# T2.run('task3.json', 'abcxbca')
# T2.run('task3.json', 'axaa')

# T2.run('task4.json', '[(23,4)#2,3,4]') #akceptuj
# T2.run('task4.json', '[#23,') #odrzuc
# T2.run('task4.json', '[#2,3,4]') #akceptuj
# T2.run('task4.json', '[(3,2),(2,4)#2,3,4]') #akceptuj

# T2.run('palindrome.json', ' baabaab ')
T2.run('palindrome.json', ' abba ')
# T2.run('palindrome.json', ' ababab ')

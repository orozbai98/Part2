def receive_complain (x):
    with open(f'google_{x}.txt', 'a') as file:
        file.write(input('Give your complain here: '))
        print('Thank you!')

greetings = input('Say "Hello" ').lower().strip()
if greetings == 'hello':
    print("""Hello! Pls, choice your office: 
Kazakstan
Paris
UAR
Kyrgyzstan
San-Francisco
Germany
Moscow
Sweden""")
    answer = input('').lower().strip()

    if answer == 'kazakstan':
            receive_complain(answer)
    elif answer == 'paris':
            receive_complain(answer)
    elif answer == 'uar':
        receive_complain(answer)
    elif answer == 'kyrgyzstan':
        receive_complain(answer)
    elif answer == 'san-francisco':
        receive_complain(answer)
    elif answer == 'germany':
        receive_complain(answer)
    elif answer == 'moscow':
        receive_complain(answer)
    elif answer == 'sweden':
        receive_complain(answer)
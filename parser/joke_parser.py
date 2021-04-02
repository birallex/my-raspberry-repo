import requests

jokes = set()

for i in range(1000):
    print("Запрос " + str(i) + " начат успешно")
    joke = requests.get('https://tproger.ru/wp-content/plugins/citation-widget/get-quote.php')
    jokes.add(joke.text)

with open('jokes.txt', 'w') as text:
    counter = 0
    for original_joke in jokes:
        counter += 1
        original_joke = str(counter) + ': ' + original_joke + '\n'
        print(original_joke)
        text.write(original_joke)


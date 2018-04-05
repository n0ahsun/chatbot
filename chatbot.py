import apiai
import json

print('What do you want to say?')
while True:
    try:
        ai = apiai.ApiAI('658c6fd924ff44d19f4c40e8a833f9bd')
        request = ai.text_request()
        request.session_id = 'a249db19-3a6f-4f05-bfe2-6faab2f1b97e'
        request.query = input()
        response = request.getresponse()
        source = json.loads(response.read())
        try:
            print(source['result']['fulfillment']['speech'])
        except:
            print(source['result']['fulfillment']['messages'][0]['speech'])
    except(KeyboardInterrupt, EOFError, SystemExit):
        break


import prsaw
from prsaw import RandomStuff

api_key = "8HnGpUQX67lr"
rs = RandomStuff(api_key = api_key)

while True:
    user_input = input("> ")
    response = rs.get_ai_response(user_input)
    print(response)

rs.close()

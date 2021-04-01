import prsaw
from prsaw import RandomStuff

rs = RandomStuff()

while True:
    user_input = input("> ")
    response = rs.get_ai_response(user_input)
    print(response)

rs.close()

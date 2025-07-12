unicorns = [{"color": "pink"}, {"color": "blue"}, {"color": "sparkly"}]
def unicorns_to_rainbow(unicorns: list[dict]) -> list[str]:

    for i in unicorns:
        print(f'🌈 Rainbow unicorn of color {i['color']}')

unicorns_to_rainbow(unicorns)


# результат:
# [
#   "🌈 Rainbow unicorn of color pink",
#   "🌈 Rainbow unicorn of color blue",
#   "🌈 Rainbow unicorn of color sparkly"
# ]

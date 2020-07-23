# Generate html file from research

def format_HTML(lst):
    HIER = ['~', '-', '*', '^', '?']

    return_string = ''
    for i in lst:
        if i[0] == "[Live Action]":
            return_string += '<h1 id="live-action">\n\t\tLive Action\n\t</h1>\n'
            rid = 'video'

        elif i[0] == "[Anime]":
            return_string += '\t<h1 id="anime">\n\t\tAnime\n\t</h1>\n'
            rid = 'animation'

        elif i[0] == "[Comic]":
            return_string += '\t<h1 id="comic">\n\t\tComic\n\t</h1>\n'
            rid = 'text'

        elif i[0] == "[Game]":
            return_string += '\t<h1 id="game">\n\t\tGames\n\t</h1>\n'
            rid = 'vidya'

        for x in range(len(i)-1):
            line = i[x+1]

            if x == len(i) - 2:
                nex = '?'
            else:
                nex = i[x+2][0]

            tag = line[0]
            name, link = line[2:].split(' | ')

            if tag == '^':
                return_string += f'\t<h2>{name}</h2>\n'

            elif link == 'none':
                return_string += f'\t<li>{name}</li>\n'

            else:
                return_string += f'\t<li><a href="{link}" target="blank" id="{rid}">{name}</a></li>\n'

            if HIER.index(nex) > HIER.index(tag):
                return_string += '</ul>\n' * (HIER.index(nex) - HIER.index(tag))

            elif HIER.index(nex) < HIER.index(tag):
                return_string += '<ul>\n'

    return return_string

def main():
    # open research file
    with open('research.txt', 'r') as f:
        research = f.read().split('\n')

    with open('template.txt', 'r') as f:
        template = f.read().split('<@FILLER>')

    # remove all blanks
    research = list(filter(lambda x: x, research))

    live_i = research.index('[Live Action]')
    ani_i = research.index('[Anime]')
    com_i = research.index('[Comic]')
    game_i = research.index('[Game]')

    cat = sorted([live_i, ani_i, com_i, game_i, len(research)])

    r = []
    for i in range(0, len(cat) - 1):
        r.append(research[cat[i]: cat[i+1]])

    html = format_HTML(r)
    template.insert(1, html)

    html = ''.join(template)

    with open('index.html', 'w') as f:
        f.write(html)

main()

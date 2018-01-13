def getTimeRange(length):
    start = (length / 2) - 5
    end = (length / 2) + 5
    return (start,end)


def videoPlayer(response):
    response.write('''
<audio id="audio-player" controls>
    <source src="music.mp3" type="audio/mpeg">
</audio>
''')

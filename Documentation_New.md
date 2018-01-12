# Team Five Documentation
---
## Template Language

The engine is the `templatingParser.py` file. You should include this file in your python files using `import templatingEngine` at the top of your file. This is assuming that the engine is in the same directory as your own Python file. If you need to be in a different directory and still access the engine, talk to Jack or James (tutor).

To then use the engine, you call `templatingEngine.translateToHTML("filename", {context})` replacing _filename_ with the filename of the html you want to parse, **relative to the `templatingParser.py` file.** Context is a dictionary of all the variables you want to be able to use in your html file.

This function then returns a **string**. This is the completed html which should be returned as the page response.

### Syntax

### `{{ expr }}`

This will output the result of a python expression.
E.g.
>````html
<h1>{{ Person.name }}<h1>
````

### `{% include <path> %}`
This will include another HTML file in place of this line.
E.g.
>````
{% include header.html %}
````


### `{% if <statement> %} X {% end if %}`
This will act as an if statement block. X will only be executed if the statement evaluates to true.
E.g.
>````
{% if Person.hasFriends %}
   {{ Person.name }} has {{ len(Person.friends) }} friends!
{% end if %}
````


### `{% for <var> in <iterator> %} X {% end for %}`
This will act as an for statement block. X will executed (and therefore printed/repeated) a number of times. `var` Loops through the iterator, just like a regular for loop in Python.
E.g.
>````html
{% for friend in Person.friends %}
   <li class=’friend’>
      {% include friend.html %}
   </li>
{% end for %}
 ````

---

## Interacting with the Database:

If a function has //<function name>// it is not planed to be in the mvp of the product.


Person.name()
Returns the current users username (Str)

Database.name_find(<Str>)
Returns if that username (<Str>) is in the database (Bool)
E.g.
>>>Person.nameFind(“James”)
True


Person.good(<Str>)
Returns a list of what Music this user (<Str>) have upvoted (list of str)
E.g.
>>>Person.good(“James”)
[“Music1”,”Music2”]


Person.bad(<Str>)
Returns a list of what Music this user (<Str>) has downvoted (list of str)
E.g.
>>>Person.bad(“James”)
[“Music3”,”Music4”]


Person.find_song(<Str1>, <Str2>)
Returns if the user (<Str1>) has voted on this song (<Str2>) (Bool)
E.g.
>>>Person.findSong(“James”, “Music1”)
True




Music
A class that contains the Music, and the Music’s tags, name, album, and //other metadata//


//Music.album(<Str>)//
Returns the album of the song imputed (Str)
E.g.
>>>Music.album(“Music2”)
“Music2 album”


Music.artist(<Str>)
Returns the album of the song imputed (Str)
E.g.
>>>Music.artist(“Music2”)
“Dave Songwriter”


//Music.title()//
Returns the name of the song that is playing (Str)


//Music.tags(<Str>)//
Returns a list of the songs (<Str>) tags (list of str)
E.g.
>>>Music.tags(“Music1”)
[“Rock”,”Pop”]


Music.rand_music()
Returns a random song (file)


Music.Music(<Str>)
Returns a song of the name inputted (file)
E.g.
>>>Music.Music(“Music2”)
Music2.mp3 (or something like that)

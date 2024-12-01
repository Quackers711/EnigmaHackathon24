# Enigma Hackathon 2024 - 1st December 2024
We were given a case related to christmas. Santa claus had accidentally deleted the entire database of christmas cards!
We were then given the task to create a new service to create christmas cards.

This Hackathon only lasted about 4 hours.

I started off the Hackathon by brainstorming a few ideas and wrote them down below.

## Ideas
* Flask frontend with database.
* Leet speak converter on christmas cards - A funny twist to make it more than just a card generator.
* Page to see all cards.
* Page to create a card.
* Some sort of images on the cards.
* A "Drillenisse" (elf) that randomly steals letters from the christmas cards - Another twist to expand the "lore" behind the case.

## Implementation
I started off by implementing a simple Flask frontend with the basic route I would need:
* `/cards` - To display the christmas cards from the database.
* `/cards/create` - To create a christmas cards.
* `/` - A simple home/landing page with a small introduction to the project.

After I had the routes set up I made some basic HTML templates for each route with the needed fields, forms  and buttons.

Then, I integrated it with a Database using SQLite and setup the logic to save and load christmas cards.

With all the basic functionality done I took some time to focus on making the frontend HTML look somewhat nice.
At this point I still had about an hour left of the Hackathon and had already implemented most of my ideas.
This is where I suddenly got the funny idea of adding the "drillenisse" twist to the website.

I found a fitting image online and implemented the needed Javascript to make the gnome/elf randomly appear on the screen.
From there I made it steal a random selection of characters from each christmas card and only return them if clicked.

## Lore & Presentation
The entire website played quite nicely into the narrative given that santa had lost his database. It gave him a new system to use with some interesting functionality. Furthermore, it also expanded upon the lore because the new database had been "infected" by the "drillenisse" (elf). Santa must now constantly catch the elf to stop it from stealing all the letters from his precious christmas cards.


## Tech Stack Used
* Python 3.12.3 with Flask
* JS & HTML
* SQLite
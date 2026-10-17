Paradox Peddler

A terminal time-travel trading game written in Python.

You're a merchant with a time machine. Buy cheap in one era, sell high in another, and try not to break history. Every sale leaves a ripple, and the ripples add up.

Status: early design phase. The first playable version is not out yet. This README describes where the game is headed.

The idea
Trade across time. The same item is worth wildly different amounts in different eras. A smartphone is junk in the far future and priceless in ancient Egypt.
Your sales change history. Sell something out of its time and that era is different the next time you visit. Maybe it now craves your goods, maybe its economy is a mess.
Paradoxes push back. Risky sales raise a paradox meter. The higher it gets, the weirder things become: prices scramble, eras close, time cops show up. You can lower it, but it costs you.
One more run. A run ends when the timeline collapses or you go broke. Your score is what you earned before that. Could you have squeezed in one more risky sale?
Planned eras

The first version starts small, with three eras. More come later.

Era	Status
Dinosaur Age	Planned
Ancient Egypt	Planned
Far Future	Planned
Medieval Castle Times	Next batch

Each era is designed around a big gap in what's valuable, so there's always a profitable (and risky) trip to take.

Built to be changed

This game is meant to be extended by anyone. The goal is that adding content is as easy as adding a few lines of text:

New eras
New items and their prices
New random events
New paradox effects

The game rules live in the Python code. The content (eras, items, events) will live in separate, plain files so you can add to the game without digging through the code. A short guide on how to do it will be added once the first version exists.

Roadmap
 Milestone 1: three eras, a handful of items, buying and selling with different prices per era
 Milestone 2: the paradox meter and its effects
 Milestone 3: ripples, so selling in an era changes it for later
 Milestone 4: random events and a clear end-of-run score
 Later: more eras, more items, anything the community wants to add
Running the game

You'll need Python 3. Run instructions will be added when the first playable version is ready.

Contributing

Ideas, new eras, funny items, and bug reports are all welcome. Open an issue to suggest something, or fork the project and make your own version.

License

Released under the MIT License. You're free to use, change, share, and even sell your own version. See the LICENSE file for details.

Credits

Created by madebynova. Built as a way to learn Python by making something fun.

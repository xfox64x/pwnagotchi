#### Your arrogance blinds you.
Added all of my fixes and plugins from my other repo, to this one.

I guess this is also where my fork significantly diverges from the original. I've added logic to multithread and queue events for plugins. It's been noted that the way pwnagotchi handles tasking events on the plugins causes everything to slow, depending on the collective speed of the plugins, because they were being processed serially. The `pwnagotchi/plugins/__init__.py` has been updated to create a thread-managed queue for each event type, for each plugin. When an event is processed on all plugins containing a function definition for the event, it gets added to the back of a queue for processing that specific type of event on a valid plugin. Moving forward, this should have little, if any, impact on my future development efforts because I fully expect evilsocket to put out their own multithreaded version soon, but I can't be bothered to follow arbitrary style guides for free.


## License

`pwnagotchi` is made with ♥  by [@evilsocket](https://twitter.com/evilsocket) and the [amazing dev team](https://github.com/evilsocket/pwnagotchi/graphs/contributors). It is released under the GPL3 license.

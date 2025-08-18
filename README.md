# Simple connect four CI APP

Simple python app for playing connect four in the CLI.

First player is a person, second player is an agent that competes against them. The human agent can quit at any time. The game continues until there is a winner or the board is full.

## Dev note
I am not a python developer and I have only used it a handful of times. That said I used this take-home exercise as an opportunity to learn. That's why you'll see some strange patterns here or missing concepts (e.g. `__init__.py`, I only just learned about it). I'm a PHP dev and so I emulated the language patterns I use day to day. I have to say though, after playing with python over the weekend I have come to really like it. I'll definitely continue using it.

## Implementation
This has been built in Python 3.13.6 and runs in a docker container.

## Launching
You can launch by calling the following in the installed directory:

Build the docker image:
> docker build -t connect_four .

Start the container, download deps and connect
> docker run -v .:/app -it connect_four

At the end this will connect to the container from which you can run the game or tests.

To launch the game from the shell enter the following:
> python src/main.py

## Testing
There is a suite of tests. Mostly unit tests with a high level acceptance test to drive the CLI app and prove it works as expected.

To run enter `pytest` in the container.

## Architecture
I went with simple domain and controller separation, with a ports and adapters mindset. Domain is the core concepts excluding input or output mechansims. The controllers handle inputs and outputs and drive the domain logic, in this case a CLI controller. The design is intended to make other types of controllers easy to implement, such as a HTTP API.

## Improvements
If I had more time I'd introduce an application layer, specifically a service called `GameService` that would remove some of the business logic from the controller (such as selecting the next player). This would also make introducing a new controller type even easier and make unit testing controllers more viable.

I'd extract the board searching logic from the board and move that into another class, as that class is getting quite big and the search logic is its own thing.

I've left the agent concept lose and decoupled. It would be very easy to create different types of agent, which are composed of layered strategies. E.g. you could make "sore loser" agent that quits once it's realised you're going to win after its move no matter what.

Finally I'd introduce a repository for saving in progress games. It would be nice to be able to quit and continue a game.
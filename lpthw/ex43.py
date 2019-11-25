from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("this scene is not yet configured.")
        print("subclass it and implement enter().")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print tout the last scene
        current_scene.enter()




class Death(Scene):

    quips = [
        "you died. You kinda suck at this.",
        "who is smarter",
        "such a luster",
        "you're worse than your Dad's jokes."

    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips) - 1)])
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
            the gothons of planet
            destroyed your entire crew.
            your last mission
            bomb from where
            blow the ship

            you's running
            armory when
            filled body
            atout to pull a weapon.
            """))
        action = input("> ")

        if action == 'shoot !':
            print(dedent("""
                    quick on the draw
                    lottery again
                    no lottery anymore
                    really no lottery
                    this is completely no lottery
                    bought lottery
                    and last lottery
                    lottery no more
                    """))
            return 'death'

        elif action == "dodge!":
            print(dedent("""
                    like a world class boxer
                    slide alright
                    past your head
                    wall and wall
                    build more cities
                    again more buildings
                    """))
            return 'death'

        elif action == 'tell a joke':
            print(dedent("""
            lucky for you
            shools again
            what's that
            this is nothing
            gut
            gut again
            morning of morning
            """))
            return 'laser_weapon_armory'

        else:
            print("does not compute!")
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
              you do a dive
              the room of yours
              quiet very quiet
              the room to find
              there is a keyboard
              get the bomb out now
              the lock
              code is broke
              """))

        code = f"{randint(1, 9)}{randint(1, 9)}{randint(1, 9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZEDDD!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
            the container
            gas out
            your can to
            right spot.
            """))
            return 'death'


class TheBridge(Scene):

    def enter(self):
        print(dedent("""
              you burst to
              under arm
              take control of
              clown costumes
              weapons again
              arm and army
              """))

        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""
                  in a panic model
                  make a leap
                  shoots you now
                  find another life
                  discarm you now
                  blow up the city
                  """))
            return 'death'

        elif actio == "slowly place the bomb":
            print(dedent("""
                  you point your blaster
                  hands up
                  inch back
                  place the bomb
                  blaster it
                  punch it
                  get out now
                  you run
                  """))

            return 'escape_pod'
        else:
            print("does not compute!")
            return "the_bridge"


class EscapePod(Scene):

    def enter(self):
        print(dedent("""
              you rush
              the escape pod
              like hardly any other
              clear of enterprise
              escape pods again
              damaged already
              5 pods totoal
              """))

        good_pod = randint(1,5)
        guess = input("[pod #]> ")


        if int(guess) != good_pod:
            print(dedent("""
                  you jump inot pod
                  the pod escape
                  implodes
                  jam jelly
                  """))

            return 'death'
        else:
            print(dedent("""
                  you jump again
                  the pod easy
                  planet below
                  back and see
                  bright star
                  time
                  """))

            return 'finished'

class Finished(Scene):

    def enter(self):
        print("you won! good job")
        return 'finished'

class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

from goblin import Goblin
from hero import hero

ARENA_NAME = "The Iron Square"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to the spectatcular {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Yo Gabba Gabba")
    goblinTwo= Goblin("Teletubby")
    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print(f"{goblinTwo.name} enters the arena with {goblinTwo.health} health.")

    print("But no hero has answered the call... yet.")


    Hero=hero("Eren Yager")
    print(f"{hero.name} enters the arena with{hero.health} health>")

if __name__ == "__main__":
    main()

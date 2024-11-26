from rlsdk_python import RLSDK, EventTypes
import sys

# Utwórz instancję SDK
rlsdk = RLSDK()

# Funkcja do wywołania przy każdym ticku gracza
def on_tick(event):
    game_event = rlsdk.get_game_event()
    if game_event:
        cars = game_event.get_cars()
        for car in cars:
            pri = car.get_pri()
            player_name = pri.get_player_name()
            x, y, z = car.get_location().get_xyz()
            print(f"{player_name} znajduje się na współrzędnych {x}, {y}, {z}")

# Subskrybuj wydarzenie tick gracza
rlsdk.event.subscribe(EventTypes.ON_PLAYER_TICK, on_tick)

# Oczekuj na zakończenie działania
sys.stdin.read()

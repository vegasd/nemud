import logging

# FIXME: all text should be outside of here
WELCOME = """Типа приветствие
пыщ пыщ ололо
ты попал в какой-то MUD"""

class Room:
    pass

class Item:
    pass

class Character:
    pass


startroom = Room()

class Player(Character):
    def __init__(self, connection):
        self.connection = connection
        self.room = startroom
        self.inventory = []
        self.mes = self.connection.mes
        self.protocol = self.connection.protocol
        self.iden = self.connection.iden


class Game():
    def __init__(self):
        self.players = {}

        self.log = logging.getLogger('game')
        self.log.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.log.addHandler(ch)
        self.debug = self.log.debug
        self.info = self.log.info
        self.warning = self.log.warning
        self.error = self.log.error
        self.critical = self.log.critical

    def new_player(self, con):
        self.info("New player joined: {}".format(con.iden))
        p = Player(con)
        self.players[con.iden] = p
        self.info("{} added to players list. {} players now.".format(p.iden, len(self.players)))
        p.mes(WELCOME)

    def process_command(self, player, command):
        self.debug("{} send command: {}".format(player.iden, command))
        
        # TODO: command processing.
        # Make plugin system for languages (start with russian)
        # DEBUG:
        player.mes("You entered "+command)


game = Game()

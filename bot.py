#!/usr/bin/env python3

# XMPP (Jabber) frontend for new mud engine

from sleekxmpp import ClientXMPP

from game import game


# FIXME: to config
# {{{ config ==================================================================
BOT_JID = "newmud@jabber.ru"
BOT_PASSWORD = "publicpwd"
# }}} config ==================================================================


class XMPPConnection:
    def __init__(self, jid):
        self.protocol = "xmpp"
        self.iden = jid

    def mes(self, m):
        bot.send_message(self.iden, m)

class MUDBot(ClientXMPP):
    def __init__(self, jid, password):
        super().__init__(jid, password)
        self.add_event_handler('session_start', self.start)
        self.add_event_handler('message', self.message_handler)

    def start(self, event):
        self.send_presence()
        self.get_roster()

    def message_handler(self, msg):
        frm = msg['from'].bare
        if frm in game.players:
            player = game.players[frm]
            game.process_command(player, msg['body'])
        else:
            game.new_player(XMPPConnection(frm))


game.info("Starting XMPP bot")
bot = MUDBot(BOT_JID, BOT_PASSWORD)
bot.register_plugin('xep_0030') # Service Discovery
bot.register_plugin('xep_0199') # Ping 
if bot.connect():
    game.info("XMPP bot connected")
    bot.process(block=True)
    game.info("Done")
else:
    game.error("XMPP bot unable to connect")

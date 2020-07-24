from errbot import BotPlugin, botcmd

class Opa(BotPlugin):
    """'Opa' plugin for Errbot"""

    @botcmd
    def opa(self, msg, args):
        """Say Opa"""
        return "Opa {}".format(msg.frm)
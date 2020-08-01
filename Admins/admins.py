import re

from errbot import BotPlugin, botcmd

class Admins(BotPlugin):
    """'Admins' plugin for Errbot"""

    @botcmd
    def admins(self, msg, args):
        """List bot admins"""
        return self.bot_config.BOT_ADMINS
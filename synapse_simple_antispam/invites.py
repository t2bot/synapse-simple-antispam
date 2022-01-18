class AntiSpamInvites:
    def __init__(self, config, api):
        self._blocked_homeservers = config.get("blocked_homeservers", [])
        api.register_spam_checker_callbacks(
            user_may_invite=self.user_may_invite,
        )

    def user_may_invite(self, inviter_user_id, invitee_user_id, room_id):
        for bad_hs in self._blocked_homeservers:
            if inviter_user_id.endswith(":" + bad_hs):
                return False # not allowed
        return True # allowed

    @staticmethod
    def parse_config(config):
        return config # no parsing needed

import re

class AntiSpamHomeserverMessages:
    def __init__(self, config, api):
        self._blocked_homeservers = config.get("blocked_homeservers", [])
        self._soft_fail = config.get("soft_fail", False)
        api.register_spam_checker_callbacks(
            check_event_for_spam=self.check_event_for_spam,
        )

    async def check_event_for_spam(self, event):
        for bad_hs in self._blocked_homeservers:
            if event.sender.endswith(":" + bad_hs):
                if self._soft_fail:
                    event.internal_metadata.soft_failed = True
                return True # not allowed (spam)
        return False # not spam

    @staticmethod
    def parse_config(config):
        return config # no parsing needed


class AntiSpamText:
    def __init__(self, config, api):
        self._blocked_texts = config.get("blocked_messages", [])
        self._soft_fail = config.get("soft_fail", False)
        api.register_spam_checker_callbacks(
            check_event_for_spam=self.check_event_for_spam,
        )

    async def check_event_for_spam(self, event):
        for msg in self._blocked_texts:
            if event.content.get("body", "") == msg:
                if self._soft_fail:
                    event.internal_metadata.soft_failed = True
                return True # not allowed (spam)
        return False # not spam

    @staticmethod
    def parse_config(config):
        return config # no parsing needed


class AntiSpamRegex:
    def __init__(self, config, api):
        self._blocked_texts = [re.compile(v) for v in config.get("blocked_messages", [])]
        self._soft_fail = config.get("soft_fail", False)
        api.register_spam_checker_callbacks(
            check_event_for_spam=self.check_event_for_spam,
        )

    async def check_event_for_spam(self, event):
        for msg in self._blocked_texts:
            if msg.search(event.content.get("body", "")):
                if self._soft_fail:
                    event.internal_metadata.soft_failed = True
                return True # not allowed (spam)
        return False # not spam

    @staticmethod
    def parse_config(config):
        return config # no parsing needed

# synapse-simple-antispam
A simple spam checker module for Synapse to block invites from unwanted homeservers


## Installation

In your Synapse python environment:
```bash
pip install git+https://github.com/t2bot/synapse-simple-antispam#egg=synapse-simple-antispam
```

Then add to your `homeserver.yaml`:
```yaml
modules:
  # Module to block invites from listed homeservers
  - module: "synapse_simple_antispam.AntiSpamInvites"
    config:
      # A list of homeservers to block invites from.
      blocked_homeservers:
        - badcorp.example.org
        - evil.example.com
  # Module to block messages from listed homeservers
  - module: "synapse_simple_antispam.AntiSpamHomeserverMessages"
    config:
      # If true, the blocked messages will be soft failed by synapse.
      # Soft failing can help prevent messages from going down sync streams.
      soft_fail: false
      # A list of homeservers to block messages from.
      blocked_homeservers:
        - badcorp.example.org
        - evil.example.com
  # Module to block messages with the given text
  - module: "synapse_simple_antispam.AntiSpamText"
    config:
      # If true, the blocked messages will be soft failed by synapse.
      # Soft failing can help prevent messages from going down sync streams.
      soft_fail: false
      blocked_messages:
        - "This is spam. Spammy spam spam."
  # Module to block messages with the given text regexes
  - module: "synapse_simple_antispam.AntiSpamRegex"
    config:
      # If true, the blocked messages will be soft failed by synapse.
      # Soft failing can help prevent messages from going down sync streams.
      soft_fail: false
      blocked_messages:
        - "spam"  # "spam" anywhere in the message
        - "sp[am]+" # "spammmm", "spaaaammmmm", etc
```

Synapse will need to be restarted to apply the changes. To modify the list of homeservers,
update the config and restart Synapse.

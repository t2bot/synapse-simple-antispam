# synapse-simple-antispam
A simple spam checker module for Synapse to block invites from unwanted homeservers


## Installation

In your Synapse python environment:
```bash
pip install git+https://github.com/t2bot/synapse-simple-antispam#egg=synapse-simple-antispam
```

Then add to your `homeserver.yaml`:
```yaml
spam_checker:
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
      # A list of homeservers to block messages from.
      blocked_homeservers:
        - badcorp.example.org
        - evil.example.com
  # Module to block messages with the given text
  - module: "synapse_simple_antispam.AntiSpamText"
    config:
      blocked_messages:
        - "This is spam. Spammy spam spam."
  # Module to block messages with the given text regexes
  - module: "synapse_simple_antispam.AntiSpamRegex"
    config:
      blocked_messages:
        - "*spam*"
```

Synapse will need to be restarted to apply the changes. To modify the list of homeservers,
update the config and restart Synapse.

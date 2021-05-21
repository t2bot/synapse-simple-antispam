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
  - module: "synapse_simple_antispam.AntiSpamInvites"
    config:
      # A list of homeservers to block invites from.
      blocked_homeservers:
        - badcorp.example.org
        - evil.example.com
      # Set to true to block messages from the above homeservers as well
      block_messages: true
```

Synapse will need to be restarted to apply the changes. To modify the list of homeservers,
update the config and restart Synapse.

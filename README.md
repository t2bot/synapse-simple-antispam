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
  module: "synapse_simple_antispam.AntiSpamInvites"
  config:
    # A list of homeservers to block invites from.
    blocked_homeservers:
      - badcorp.example.org
      - evil.example.com
```

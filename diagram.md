```mermaid
sequenceDiagram
    Player->>+Monster: Player rolls initiative (rolls same amount of D6s(6 sided dice) as initiative)
    Monster->>+Player: Monster rolls initiative (rolls same amount of D6s as initiative)
    Player->>+Monster: Player wins initiative and begins the fight
    Player->>+Monster: Player can attack or flee. Player fights (rolls same amount of D6s as attack)
    Monster->>+Monster: Checks if dexterity is higher than players roll (higher)
    Player->>+Monster: Misses attack
    Monster->>+Player: Monster attacks (rolls same amount of D6s as attack)
    Player->>+Player: checks dexterity (lower)
    Monster->>+Player: Attack hits
    Player->>+Player: Loses 1 Health
    Player->>+Monster: Player Attack (rolls dice)
    Monster->>+Monster: Checks dexterity (lower)
    Player->>+Monster: Attack hits
    Monster->>+Monster: loses 1 Health
    Monster->>+Player: Monster attacks (rolls dice)
    Player->>+Player: Checks dexterity (higher)
    Monster->>+Player: Misses attack
    Player->>+Monster: Player can attack or flee (Player tries to flee)
    Player->>+Player: Checks if able to flee (dexterity * 10 = X%)
    Player->>+Monster: Player flees
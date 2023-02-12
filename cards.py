"""
content of the file
    A tuple of all cards ordered by the number of the cards

deck : tuple
    A deck consists of a tuple of cards.
    The deck is represented as a tuple of tuples (cards) from top (start=0) to bottom (end=len(deck)-1).

card : tuple
    A card consists of a tuple of one header (dict) and four sections.

header (to the card) : dict
    The card header (dict) identifies and specifies the card and contains the following keys:
    - name : str ('warrior', 'ogre', 'huntress', 'vampire', 'pyromancer', 'spider')
    - type : str ('hero', 'monster')
    - number : int, the card number

section : tuple
    A section consists of a list of one header and one or more rows (of actions).

header (to the section) : dict
    The section header (dict) identifies and specifies the section and contains the following keys:

    - section : str ('A', 'B', 'C', 'D')
    - life : str ('healthy', 'wounded', 'exhausted')
    - feature : set of str (optional)
    - reaction : str (optional)
    - shield : str (optional)
    - other named feature : str (optional)

row (of actions) : tuple
    A row of actions consists of a tuple of consecutive actions.
    Do not forget to nest also single actions by using additional comma, ((str, int, str),)

action : tuple(str, int, str)
    An action is a tuple of an action (str), range or number of positions (int) and target side (str).
    The second and/or the third element may be None, depending on the action.
    The following action names are recognised (as expected by the end of the development):

    - hit
    - rotate
    - delay
    - delay ally
    - delay hero
    - quicken
    - quicken ally
    - quicken enemy
    - pull
    - pull ally
    - pull enemy
    - push
    - push ally
    - push enemy
    - heal
    - rotate
    - maneuver
    - arrow
    - inspire
    - revive
    - teleport ally
    - teleport enemy
    - teleport any
    - fireball
    - ablaze
    - condition, this is a special action
        for which the second item in the tuple is a list of actions:
        example (condition, (('fire', 2, 'ally'), ('ablaze', None, 'enemy'), ('hit', 2, 'enemy'),))

    The following targets are recognised
    - 'enemy'
    - 'ally'
    - 'any'
    - 'both' (for 'teleport')
"""

cards = {1: {  # card 1
    'header': dict(name='warrior', type='hero'),
    'A': (
        dict(life='healthy'),
        (('hit', 2, 'enemy'),),
        (('delay', 2, 'any'), ('rotate', None, 'self'),)
    ),
    'B': (
        dict(life='healthy', shield='rotate'),
        (('delay', 1, 'any'), ('hit', 2, 'enemy'),),
        (('delay', 2, 'any'),)
    ),
    'C': (
        dict(life='exhausted'),
        (('hit', 2, 'enemy'), ),
        (('delay', 2, 'any'), )
    ),
    'D': (
        dict(life='wounded'),
        (('hit', 4, 'enemy'),),
        (('quicken', 2, 'any'),)
    )
}, 2: {
    'header': dict(name='warrior', type='hero'),
    'A': (
        dict(life='healthy'),
        (('hit', 2, 'enemy'), ('rotate', None, 'self'),),
        (('delay', 2, 'any'),)
    ),
    'B': (
        dict(life='healthy', shield='rotate'),
        (('heal', None, 'ally'), ('rotate', None, 'self'),),
        (('quicken', 2, 'any'),)
    ),
    'C': (
        dict(life='exhausted'),
        (('quicken', 2, 'any'),),
        (('delay', 2, 'any'),)
    ),
    'D': (
        dict(life='wounded'),
        (('heal', None, 'ally'), ('rotate', None, 'self'),),
        (('delay', 3, 'any'),)
    )
}, 3: {
    'header': dict(name='warrior', type='hero'),
    'A': (
        dict(life='healthy'),
        (('delay', 2, 'any'), ('rotate', None, 'self'),),
        (('quicken', 2, 'any'), ('rotate', None, ),)
    ),
    'B': (
        dict(life='healthy'),
        (('hit', 4, 'enemy'), ('hit', 4, 'enemy'), ('rotate', None, 'self'),)
    ),
    'C': (
        dict(life='exhausted'),
        (('quicken', 2, 'any'),),
        (('delay', 2, 'any'),)
    ),
    'D': (
        dict(life='wounded'),
        (('hit', 4, 'enemy'),),
        (('delay', 1, 'any'),)
    )
}, 4: {
    'header': dict(name='warrior', type='hero'),
    'A': (
        dict(life='healthy', shield='rotate'),
        (('hit', 4, 'enemy'),),
        (('quicken', 2, 'any'),)
    ),
    'B': (
        dict(life='healthy'),
        (('hit', 2, 'enemy'),),
        (('delay', 1, 'any'), ('quicken', 1, 'any'), ('rotate', None, 'self'),)
    ),
    'C': (
        dict(life='wounded'),
        (('hit', 4, 'enemy'),),
        (('quicken', 1, 'any'),)
    ),
    'D': (
        dict(life='exhausted'),
        (('hit', 2, 'enemy'),),
        (('heal', None, 'ally'),)
    )
}, 5: {
    'header': dict(name='warrior', type='hero'),
    'A': (
        dict(life='healthy', shield='rotate'),
        (('quicken', 2, 'any'), ('hit', 2, 'enemy'),)
    ),
    'B': (
        dict(life='healthy'),
        (('hit', 2, 'enemy'), ('rotate', None, 'self'),),
        (('quicken', 2, 'any'), ('rotate', None, 'self'),)
    ),
    'C': (
        dict(life='wounded'),
        (('delay', 3, 'any'), ('hit', 2, 'enemy'), ('hit', 2, 'enemy'), ('rotate', None, 'self'),),
        (('quicken', 2, 'any'),)
    ),
    'D': (
        dict(life='exhausted'),
        (('hit', 4, 'enemy'),),
        (('quicken', 1, 'any'),)
    )
}, 6: {  # card 6
    'header': dict(name='ogre', type='monster'),
    'A': (
        dict(life='healthy'),
        (('pull', 5, 'enemy'), ('hit', 1, 'enemy'), ('rotate', None, 'self'),)
    ),
    'B': (
        dict(life='healthy', shield='rotate'),
        (('hit', 4, 'enemy'), ('push', 3, 'enemy'),),
    ),
    'C': (
        dict(life='exhausted'),
        (('hit', 5, 'enemy'),),
    ),
    'D': (
        dict(life='wounded', feature={'heavy'}, shield={}),
        (('hit', 0, 'enemy'), ('hit', 0, 'enemy'), ('rotate', None, 'self'),),
    )
}, 7: {
    'header': dict(name='ogre', type='monster'),
    'A': (
        dict(life='healthy', feature={'heavy'}),
        (('hit', 4, 'enemy'), ('rotate', None, 'self'),),
    ),
    'B': (
        dict(life='healthy', shield='rotate'),
        (('heal', None, 'ally'), ('rotate', None, 'self'),),
        (('hit', 7, 'enemy'), ('rotate', None, 'self'),)
    ),
    'C': (
        dict(life='exhausted'),
        (('hit', 5, 'enemy'), ('pull', 4, 'ally'),),
    ),
    'D': (
        dict(life='wounded'),
        (('push', 3, 'enemy'), ('hit', 5, 'enemy'),)
    )
}, 8: {
    'header': dict(name='ogre', type='monster'),
    'A': (
        dict(life='healthy'),
        (('hit', 4, 'enemy'), ('rotate', None, 'self'),),
    ),
    'B': (
        dict(life='healthy', feature={'heavy'}),
        (('heal', None, 'ally'), ('rotate', None, 'self'),),
        (('hit', 5, 'enemy'), ('rotate', None, 'self'),)
    ),
    'C': (
        dict(life='exhausted'),
        (('pull', 6, 'enemy'), ('hit', 1, 'enemy'),),
    ),
    'D': (
        dict(life='wounded'),
        (('pull', 4, 'enemy'), ('hit', 1, 'enemy'),)
    )
}, 9: {
    'header': dict(name='ogre', type='monster'),
    'A': (
        dict(life='healthy'),
        (('push', 3, 'enemy'), ('push', 3, 'enemy'), ('rotate', None, 'self'),)
    ),
    'B': (
        dict(life='healthy', reaction=('shield', 'rotate'),),
        (('hit', 5, 'enemy'), ('rotate', None, 'self'),),
    ),
    'C': (
        dict(life='exhausted', feature={'heavy'}),
        (('hit', 0, 'enemy'),),
    ),
    'D': (
        dict(life='wounded'),
        (('heal', None, 'ally'), ('heal', None, 'ally'), ('heal', None, 'ally'), ('rotate', None, 'self'),),
        (('pull', 5, 'ally'),)
    )
}, 10: {
    'header': dict(name='huntress', type='hero'),
    'A': (
        dict(life='healthy', feature={'trap'}),
        (('arrow', 1, 'enemy'), ('rotate', None, 'self'),),
        (('delay', 2, 'ally'), ('maneuver', None, 'ally'),)
    ),
    'B': (
        dict(life='healthy', feature={'trap'}),
        (('quicken', 2, 'enemy'), ('maneuver', None, 'ally'), ('rotate', None, 'self'),),
        (('heal', None, 'ally'),)
    ),
    'C': (
        dict(life='exhausted', feature={'trap'}),
        (('maneuver', None, 'ally'),),
        (('hit', 1, 'enemy'),),
        (('delay', 1, 'any'),)
    ),
    'D': (
        dict(life='wounded', feature={'trap'}),
        (('arrow', 2, 'enemy'),),
        (('maneuver', None, 'ally'),),
        (('quicken', 1, 'any'),)
    )
}, 11: {
    'header': dict(name='huntress', type='hero'),
    'A': (
        dict(life='healthy', dodge='rotate'),
        (('arrow', 1, 'enemy'), ('rotate', None, 'self'),),
        (('quicken', 2, 'enemy'), ('maneuver', None, 'ally'), ('rotate', None, 'self'),),
        (('hit', 1, 'enemy'), ('rotate', None, 'self'),)
    ),
    'B': (
        dict(life='healthy'),
        (('delay', 2, 'hero'),),
        (('quicken', 2, 'enemy'),),
        (('maneuver', None, 'ally'), ('maneuver', None, 'ally'),)
    ),
    'C': (
        dict(life='wounded'),
        (('hit', 1, 'enemy'), ('hit', 1, 'enemy'), ('rotate', None, 'self'),),
        (('quicken', 2, 'enemy'), ('maneuver', None, 'ally'),)
    ),
    'D': (
        dict(life='exhausted'),
        (('hit', 1, 'enemy'), ('maneuver', None, 'ally'), ('delay', 2, 'hero'),)
    )
}, 12: {
    'header': dict(name='huntress', type='hero'),
    'A': (
        dict(life='healthy', dodge='rotate'),
        (('maneuver', None, 'ally'), ('quicken', 2, 'enemy'), ('rotate', None, 'self'),),
        (('delay', 1, 'any'), ('rotate', None, 'self'),)
    ),
    'B': (
        dict(life='healthy', feature={'trap'}),
        (('arrow', 2, 'enemy'),),
        (('delay', 2, 'hero'), ('maneuver', None, 'ally'),)
    ),
    'C': (
        dict(life='wounded', feature={'trap'}),
        (('delay', 2, 'hero'), ('arrow', 1, 'enemy'),),
        (('maneuver', None, 'ally'),)
    ),
    'D': (
        dict(life='exhausted', feature={'trap'}),
        (('delay', 2, 'hero'), ('quicken', 2, 'enemy'),),
        (('maneuver', None, 'ally'), ('hit', 1, 'enemy'),)
    )
}, 13: {
    'header': dict(name='huntress', type='hero'),
    'A': (
        dict(life='healthy', feature={'trap'}),
        (('maneuver', None, 'ally'), ('rotate', None, 'self'),),
        (('hit', 1, 'enemy'),),
        (('delay', 1, 'any'),)
    ),
    'B': (
        dict(life='healthy'),
        (('arrow', 1, 'enemy'), ('rotate', None, 'self'),),
        (('maneuver', None, 'ally'), ('hit', 1, 'enemy'), ('rotate', None, 'self'),),
        (('quicken', 2, 'enemy'),)
    ),
    'C': (
        dict(life='exhausted', feature={'trap'}),
        (('arrow', 1, 'enemy'),),
        (('maneuver', None, 'ally'),),
        (('delay', 1, 'any'),)
    ),
    'D': (
        dict(life='wounded'),
        (('arrow', 1, 'enemy'),),
        (('quicken', 2, 'enemy'), ('maneuver', None, 'ally'),)
    )
}, 14: {
    'header': dict(name='huntress', type='hero'),
    'A': (
        dict(life='healthy', dodge='rotate'),
        (('arrow', 1, 'enemy'), ('rotate', None, 'self'),),
        (('quicken', 2, 'enemy'), ('rotate', None, 'self'),)
    ),
    'B': (
        dict(life='healthy'),
        (('arrow', 2, 'enemy'),),
        (('delay', 2, 'hero'), ('maneuver', None, 'ally'),),
        (('heal', None, 'ally'),)
    ),
    'C': (
        dict(life='wounded', feature={'trap'}),
        (('delay', 2, 'hero'), ('quicken', 2, 'enemy'),),
        (('maneuver', None, 'ally'), ('hit', 1, 'enemy'),)
    ),
    'D': (
        dict(life='exhausted'),
        (('arrow', 1, 'enemy'),),
        (('delay', 2, 'hero'),),
        (('heal', None, 'ally'),)
    )
}, 15: {
    'header': dict(name='vampire', type='monster'),
    'A': (
        dict(life='healthy'),
        (),
        ()
    ),
    'B': (
        dict(life='healthy'),
        (),
        (),
        ()
    ),
    'C': (
        dict(life='wounded'),
        (),
        ()
    ),
    'D': (
        dict(life='exhausted'),
        (),
        (),
        ()
    )
}, 16: {
    'header': dict(name='vampire', type='monster'),
    'A': (
        dict(life='healthy'),
        (),
        ()
    ),
    'B': (
        dict(life='healthy'),
        (),
        (),
        ()
    ),
    'C': (
        dict(life='wounded'),
        (),
        ()
    ),
    'D': (
        dict(life='exhausted'),
        (),
        (),
        ()
    )
}, 17: {
    'header': dict(name='vampire', type='monster'),
    'A': (
        dict(life='healthy'),
        (),
        ()
    ),
    'B': (
        dict(life='healthy'),
        (),
        (),
        ()
    ),
    'C': (
        dict(life='wounded'),
        (),
        ()
    ),
    'D': (
        dict(life='exhausted'),
        (),
        (),
        ()
    )
}, 18: {
    'header': dict(name='vampire', type='monster'),
    'A': (
        dict(life='healthy'),
        (),
        ()
    ),
    'B': (
        dict(life='healthy'),
        (),
        (),
        ()
    ),
    'C': (
        dict(life='wounded'),
        (),
        ()
    ),
    'D': (
        dict(life='exhausted'),
        (),
        (),
        ()
    )
}, 19: {
    'header': dict(name='pyromancer', type='hero'),
    'A': (
        dict(life='healthy'),
        (),
        ()
    ),
    'B': (
        dict(life='healthy'),
        (),
        (),
        ()
    ),
    'C': (
        dict(life='wounded'),
        (),
        ()
    ),
    'D': (
        dict(life='exhausted'),
        (),
        (),
        ()
    )
}, 20: {
    'header': dict(name='pyromancer', type='hero'),
    'A': (
        dict(life='healthy'),
        (),
        ()
    ),
    'B': (
        dict(life='healthy'),
        (),
        (),
        ()
    ),
    'C': (
        dict(life='wounded'),
        (),
        ()
    ),
    'D': (
        dict(life='exhausted'),
        (),
        (),
        ()
    )
}, 21: {
    'header': dict(name='pyromancer', type='hero'),
    'A': (
        dict(life='healthy'),
        (),
        ()
    ),
    'B': (
        dict(life='healthy'),
        (),
        (),
        ()
    ),
    'C': (
        dict(life='wounded'),
        (),
        ()
    ),
    'D': (
        dict(life='exhausted'),
        (),
        (),
        ()
    )
}, 22: {
    'header': dict(name='pyromancer', type='hero'),
    'A': (
        dict(life='healthy'),
        (),
        ()
    ),
    'B': (
        dict(life='healthy'),
        (),
        (),
        ()
    ),
    'C': (
        dict(life='wounded'),
        (),
        ()
    ),
    'D': (
        dict(life='exhausted'),
        (),
        (),
        ()
    )
}, 23: {
    'header': dict(name='pyromancer', type='hero'),
    'A': (
        dict(life='healthy'),
        (),
        ()
    ),
    'B': (
        dict(life='healthy'),
        (),
        (),
        ()
    ),
    'C': (
        dict(life='wounded'),
        (),
        ()
    ),
    'D': (
        dict(life='exhausted'),
        (),
        (),
        ()
    )
}, 24: {
    'header': dict(name='spider', type='monster'),
    'A': (
        dict(life='healthy'),
        (),
        ()
    ),
    'B': (
        dict(life='healthy'),
        (),
        (),
        ()
    ),
    'C': (
        dict(life='wounded'),
        (),
        ()
    ),
    'D': (
        dict(life='exhausted'),
        (),
        (),
        ()
    )
}, 25: {
    'header': dict(name='spider', type='monster'),
    'A': (
        dict(life='healthy'),
        (),
        ()
    ),
    'B': (
        dict(life='healthy'),
        (),
        (),
        ()
    ),
    'C': (
        dict(life='wounded'),
        (),
        ()
    ),
    'D': (
        dict(life='exhausted'),
        (),
        (),
        ()
    )
}, 26: {
    'header': dict(name='spider', type='monster'),
    'A': (
        dict(life='healthy'),
        (),
        ()
    ),
    'B': (
        dict(life='healthy'),
        (),
        (),
        ()
    ),
    'C': (
        dict(life='wounded'),
        (),
        ()
    ),
    'D': (
        dict(life='exhausted'),
        (),
        (),
        ()
    )
}, 27: {
    'header': dict(name='spider', type='monster'),
    'A': (
        dict(life='healthy'),
        (),
        ()
    ),
    'B': (
        dict(life='healthy'),
        (),
        (),
        ()
    ),
    'C': (
        dict(life='wounded'),
        (),
        ()
    ),
    'D': (
        dict(life='exhausted'),
        (),
        (),
        ()
    )
}, 28: {
    'header': dict(name='werewolf', type='monster'),
    'A': (
        dict(life='healthy'),
        (),
        ()
    ),
    'B': (
        dict(life='healthy'),
        (),
        (),
        ()
    ),
    'C': (
        dict(life='wounded'),
        (),
        ()
    ),
    'D': (
        dict(life='exhausted'),
        (),
        (),
        ()
    )
}, 29: {
    'header': dict(name='werewolf', type='monster'),
    'A': (
        dict(life='healthy'),
        (),
        ()
    ),
    'B': (
        dict(life='healthy'),
        (),
        (),
        ()
    ),
    'C': (
        dict(life='wounded'),
        (),
        ()
    ),
    'D': (
        dict(life='exhausted'),
        (),
        (),
        ()
    )
}, 30: {
    'header': dict(name='werewolf', type='monster'),
    'A': (
        dict(life='healthy'),
        (),
        ()
    ),
    'B': (
        dict(life='healthy'),
        (),
        (),
        ()
    ),
    'C': (
        dict(life='wounded'),
        (),
        ()
    ),
    'D': (
        dict(life='exhausted'),
        (),
        (),
        ()
    )
}, 31: {
    'header': dict(name='werewolf', type='monster'),
    'A': (
        dict(life='healthy'),
        (),
        ()
    ),
    'B': (
        dict(life='healthy'),
        (),
        (),
        ()
    ),
    'C': (
        dict(life='wounded'),
        (),
        ()
    ),
    'D': (
        dict(life='exhausted'),
        (),
        (),
        ()
    )
}, 32: {
    'header': dict(name='werewolf', type='monster'),
    'A': (
        dict(life='healthy'),
        (),
        ()
    ),
    'B': (
        dict(life='healthy'),
        (),
        (),
        ()
    ),
    'C': (
        dict(life='wounded'),
        (),
        ()
    ),
    'D': (
        dict(life='exhausted'),
        (),
        (),
        ()
    )
}, 33: {
    'header': dict(name='demon', type='monster'),
    'A': (
        dict(life='healthy'),
        (),
        ()
    ),
    'B': (
        dict(life='healthy'),
        (),
        (),
        ()
    ),
    'C': (
        dict(life='wounded'),
        (),
        ()
    ),
    'D': (
        dict(life='exhausted'),
        (),
        (),
        ()
    )
}, 34: {
    'header': dict(name='demon', type='monster'),
    'A': (
        dict(life='healthy'),
        (),
        ()
    ),
    'B': (
        dict(life='healthy'),
        (),
        (),
        ()
    ),
    'C': (
        dict(life='wounded'),
        (),
        ()
    ),
    'D': (
        dict(life='exhausted'),
        (),
        (),
        ()
    )
}, 35: {
    'header': dict(name='demon', type='monster'),
    'A': (
        dict(life='healthy'),
        (),
        ()
    ),
    'B': (
        dict(life='healthy'),
        (),
        (),
        ()
    ),
    'C': (
        dict(life='wounded'),
        (),
        ()
    ),
    'D': (
        dict(life='exhausted'),
        (),
        (),
        ()
    )
}, 36: {
    'header': dict(name='demon', type='monster'),
    'A': (
        dict(life='healthy'),
        (),
        ()
    ),
    'B': (
        dict(life='healthy'),
        (),
        (),
        ()
    ),
    'C': (
        dict(life='wounded'),
        (),
        ()
    ),
    'D': (
        dict(life='exhausted'),
        (),
        (),
        ()
    )
}}

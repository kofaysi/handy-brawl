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
    - void
    - death
    - condition, this is a special action
        for which the second item in the tuple is a list of actions:
        example (condition, (('fire', 2, 'ally'), ('ablaze', None, 'enemy'), ('hit', 2, 'enemy'),))

    The second item is the range of the action
    - integer
    - 0 (zero) denotes the card with the action listed
    - 'inf'
    - None, if multiple or other, see action definition

    The following targets are recognised
    - 'enemy'
    - 'ally'
    - 'any'
    - 'both' (for 'teleport')
    - 'all' (for 'ablaze')
"""

cards = {1: {  # card 1
    'header': dict(name='warrior', type='hero'),
    'A': (
        dict(life='healthy'),
        (('hit', 2, 'enemy'),),
        (('delay', 2, 'any'), ('rotate', 0, 'self'))
    ),
    'B': (
        dict(life='healthy', shield=(('rotate', None, 'self'),)),
        (('delay', 1, 'any'), ('hit', 2, 'enemy')),
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
        (('hit', 2, 'enemy'), ('rotate', 0, 'self')),
        (('delay', 2, 'any'),)
    ),
    'B': (
        dict(life='healthy', shield=(('rotate', None, 'self'),)),
        (('heal', 'any', 'ally'), ('rotate', 0, 'self')),
        (('quicken', 2, 'any'),)
    ),
    'C': (
        dict(life='exhausted'),
        (('quicken', 2, 'any'),),
        (('delay', 2, 'any'),)
    ),
    'D': (
        dict(life='wounded'),
        (('heal', 'any', 'ally'), ('rotate', 0, 'self')),
        (('delay', 3, 'any'),)
    )
}, 3: {
    'header': dict(name='warrior', type='hero'),
    'A': (
        dict(life='healthy'),
        (('delay', 2, 'any'), ('rotate', 0, 'self')),
        (('quicken', 2, 'any'), ('rotate', 0, 'self'))
    ),
    'B': (
        dict(life='healthy'),
        (('hit', 4, 'enemy'), ('hit', 4, 'enemy'), ('rotate', 0, 'self'))
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
        dict(life='healthy', shield=(('rotate', None, 'self'),)),
        (('hit', 4, 'enemy'),),
        (('quicken', 2, 'any'),)
    ),
    'B': (
        dict(life='healthy'),
        (('hit', 2, 'enemy'),),
        (('delay', 1, 'any'), ('quicken', 1, 'any'), ('rotate', 0, 'self'))
    ),
    'C': (
        dict(life='wounded'),
        (('hit', 4, 'enemy'),),
        (('quicken', 1, 'any'),)
    ),
    'D': (
        dict(life='exhausted'),
        (('hit', 2, 'enemy'),),
        (('heal', 'any', 'ally'),)
    )
}, 5: {
    'header': dict(name='warrior', type='hero'),
    'A': (
        dict(life='healthy', shield=(('rotate', None, 'self'),)),
        (('quicken', 2, 'any'), ('hit', 2, 'enemy'))
    ),
    'B': (
        dict(life='healthy'),
        (('hit', 2, 'enemy'), ('rotate', 0, 'self')),
        (('quicken', 2, 'any'), ('rotate', 0, 'self'))
    ),
    'C': (
        dict(life='wounded'),
        (('delay', 3, 'any'), ('hit', 2, 'enemy'), ('hit', 2, 'enemy'), ('rotate', 0, 'self')),
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
        (('pull', 5, 'enemy'), ('hit', 1, 'enemy'), ('rotate', 0, 'self'))
    ),
    'B': (
        dict(life='healthy', shield=(('rotate', None, 'self'),)),
        (('hit', 4, 'enemy'), ('push', 3, 'enemy')),
    ),
    'C': (
        dict(life='exhausted'),
        (('hit', 5, 'enemy'),),
    ),
    'D': (
        dict(life='wounded', feature={'heavy'}, shield=()),
        (('hit', 'inf', 'enemy'), ('hit', 'inf', 'enemy'), ('rotate', 0, 'self')),
    )
}, 7: {
    'header': dict(name='ogre', type='monster'),
    'A': (
        dict(life='healthy', feature={'heavy'}),
        (('hit', 4, 'enemy'), ('rotate', 0, 'self')),
    ),
    'B': (
        dict(life='healthy', shield=(('rotate', None, 'self'),)),
        (('heal', 'any', 'ally'), ('rotate', 0, 'self')),
        (('hit', 7, 'enemy'), ('rotate', 0, 'self'))
    ),
    'C': (
        dict(life='exhausted'),
        (('hit', 5, 'enemy'), ('pull', 4, 'ally')),
    ),
    'D': (
        dict(life='wounded'),
        (('push', 3, 'enemy'), ('hit', 5, 'enemy'))
    )
}, 8: {
    'header': dict(name='ogre', type='monster'),
    'A': (
        dict(life='healthy'),
        (('hit', 4, 'enemy'), ('rotate', 0, 'self')),
    ),
    'B': (
        dict(life='healthy', feature={'heavy'}),
        (('heal', 'any', 'ally'), ('rotate', 0, 'self')),
        (('hit', 5, 'enemy'), ('rotate', 0, 'self'))
    ),
    'C': (
        dict(life='exhausted'),
        (('pull', 6, 'enemy'), ('hit', 1, 'enemy')),
    ),
    'D': (
        dict(life='wounded'),
        (('pull', 4, 'enemy'), ('hit', 1, 'enemy'))
    )
}, 9: {
    'header': dict(name='ogre', type='monster'),
    'A': (
        dict(life='healthy'),
        (('push', 3, 'enemy'), ('push', 3, 'enemy'), ('rotate', 0, 'self'))
    ),
    'B': (
        dict(life='healthy', reaction=('shield', 'rotate'),),
        (('hit', 5, 'enemy'), ('rotate', 0, 'self')),
    ),
    'C': (
        dict(life='exhausted', feature={'heavy'}),
        (('hit', 'inf', 'enemy'),),
    ),
    'D': (
        dict(life='wounded'),
        (('heal', 'any', 'ally'), ('heal', 'any', 'ally'), ('heal', 'any', 'ally'), ('rotate', 0, 'self')),
        (('pull', 5, 'ally'),)
    )
}, 10: {
    'header': dict(name='huntress', type='hero'),
    'A': (
        dict(life='healthy', feature={'trap'}),
        (('arrow', 1, 'enemy'), ('rotate', 0, 'self')),
        (('delay', 2, 'ally'), ('maneuver', 'any', 'ally'))
    ),
    'B': (
        dict(life='healthy', feature={'trap'}),
        (('quicken', 2, 'enemy'), ('maneuver', 'any', 'ally'), ('rotate', 0, 'self')),
        (('heal', 'any', 'ally'),)
    ),
    'C': (
        dict(life='exhausted', feature={'trap'}),
        (('maneuver', 'any', 'ally'),),
        (('hit', 1, 'enemy'),),
        (('delay', 1, 'any'),)
    ),
    'D': (
        dict(life='wounded', feature={'trap'}),
        (('arrow', 2, 'enemy'),),
        (('maneuver', 'any', 'ally'),),
        (('quicken', 1, 'any'),)
    )
}, 11: {
    'header': dict(name='huntress', type='hero'),
    'A': (
        dict(life='healthy', dodge=(('rotate', None, 'self'),)),
        (('arrow', 1, 'enemy'), ('rotate', 0, 'self')),
        (('quicken', 2, 'enemy'), ('maneuver', 'any', 'ally'), ('rotate', 0, 'self')),
        (('hit', 1, 'enemy'), ('rotate', 0, 'self'))
    ),
    'B': (
        dict(life='healthy'),
        (('delay', 2, 'hero'),),
        (('quicken', 2, 'enemy'),),
        (('maneuver', 'any', 'ally'), ('maneuver', 'any', 'ally'))
    ),
    'C': (
        dict(life='wounded'),
        (('hit', 1, 'enemy'), ('hit', 1, 'enemy'), ('rotate', 0, 'self')),
        (('quicken', 2, 'enemy'), ('maneuver', 'any', 'ally'))
    ),
    'D': (
        dict(life='exhausted'),
        (('hit', 1, 'enemy'), ('maneuver', 'any', 'ally'), ('delay', 2, 'hero'))
    )
}, 12: {
    'header': dict(name='huntress', type='hero'),
    'A': (
        dict(life='healthy', dodge=(('rotate', None, 'self'),)),
        (('maneuver', 'any', 'ally'), ('quicken', 2, 'enemy'), ('rotate', 0, 'self')),
        (('delay', 1, 'any'), ('rotate', 0, 'self'))
    ),
    'B': (
        dict(life='healthy', feature={'trap'}),
        (('arrow', 2, 'enemy'),),
        (('delay', 2, 'hero'), ('maneuver', 'any', 'ally'))
    ),
    'C': (
        dict(life='wounded', feature={'trap'}),
        (('delay', 2, 'hero'), ('arrow', 1, 'enemy')),
        (('maneuver', 'any', 'ally'),)
    ),
    'D': (
        dict(life='exhausted', feature={'trap'}),
        (('delay', 2, 'hero'), ('quicken', 2, 'enemy')),
        (('maneuver', 'any', 'ally'), ('hit', 1, 'enemy'))
    )
}, 13: {
    'header': dict(name='huntress', type='hero'),
    'A': (
        dict(life='healthy', feature={'trap'}),
        (('maneuver', 'any', 'ally'), ('rotate', 0, 'self')),
        (('hit', 1, 'enemy'),),
        (('delay', 1, 'any'),)
    ),
    'B': (
        dict(life='healthy'),
        (('arrow', 1, 'enemy'), ('rotate', 0, 'self')),
        (('maneuver', 'any', 'ally'), ('hit', 1, 'enemy'), ('rotate', 0, 'self')),
        (('quicken', 2, 'enemy'),)
    ),
    'C': (
        dict(life='exhausted', feature={'trap'}),
        (('arrow', 1, 'enemy'),),
        (('maneuver', 'any', 'ally'),),
        (('delay', 1, 'any'),)
    ),
    'D': (
        dict(life='wounded'),
        (('arrow', 1, 'enemy'),),
        (('quicken', 2, 'enemy'), ('maneuver', 'any', 'ally'))
    )
}, 14: {
    'header': dict(name='huntress', type='hero'),
    'A': (
        dict(life='healthy', dodge=(('rotate', None, 'self'),)),
        (('arrow', 1, 'enemy'), ('rotate', 0, 'self')),
        (('quicken', 2, 'enemy'), ('rotate', 0, 'self'))
    ),
    'B': (
        dict(life='healthy'),
        (('arrow', 2, 'enemy'),),
        (('delay', 2, 'hero'), ('maneuver', 'any', 'ally')),
        (('heal', 'any', 'ally'),)
    ),
    'C': (
        dict(life='wounded', feature={'trap'}),
        (('delay', 2, 'hero'), ('quicken', 2, 'enemy')),
        (('maneuver', 'any', 'ally'), ('hit', 1, 'enemy'))
    ),
    'D': (
        dict(life='exhausted'),
        (('arrow', 1, 'enemy'),),
        (('delay', 2, 'hero'),),
        (('heal', 'any', 'ally'),)
    )
}, 15: {
    'header': dict(name='vampire', type='monster'),
    'A': (
        dict(life='healthy'),
        (('hit', 1, 'enemy'), ('hit', 1, 'enemy'), ('flip', 0, 'self')),
        (('hit', 6, 'enemy'), ('rotate', 0, 'self'))
    ),
    'B': (
        dict(life='healthy'),
        (('pull', 3, 'ally'), ('pull', 3, 'ally')),
        (('hit', 3, 'enemy'), ('hit', 3, 'enemy'), ('hit', 3, 'enemy'), ('rotate', 0, 'self'))
    ),
    'C': (
        dict(life='wounded'),
        (('hit', 1, 'enemy'), ('hit', 1, 'enemy'), ('rotate', 0, 'self')),
        (('hit', 5, 'enemy'),)
    ),
    'D': (
        dict(life='exhausted'),
        (('push', 3, 'enemy'),),
        (('hit', 5, 'enemy'),)
    )
}, 16: {
    'header': dict(name='vampire', type='monster'),
    'A': (
        dict(life='healthy'),
        (('inspire', 'any', 'ally'), ('rotate', 0, 'self'))
    ),
    'B': (
        dict(life='healthy'),
        (('inspire', 'any', 'ally'), ('rotate', 0, 'self'))
    ),
    'C': (
        dict(life='wounded'),
        (('push', 2, 'enemy'),),
        (('hit', 5, 'enemy'),)
    ),
    'D': (
        dict(life='exhausted'),
        (('inspire', 'any', 'ally'),)
    )
}, 17: {
    'header': dict(name='vampire', type='monster'),
    'A': (
        dict(life='healthy'),
        (('pull', 3, 'enemy'), ('hit', 1, 'enemy'), ('push', 3, 'enemy'), ('rotate', 0, 'self')),
        (('hit', 5, 'enemy'), ('rotate', 0, 'self'))
    ),
    'B': (
        dict(life='healthy'),
        (('hit', 'inf', 'enemy'), ('hit', 'inf', 'enemy'), ('flip', 0, 'self'))
    ),
    'C': (
        dict(life='exhausted'),
        (('hit', 5, 'enemy'),),
        (('pull', 5, 'ally'),)
    ),
    'D': (
        dict(life='wounded'),
        (('pull', 5, 'ally'), ('flip', 0, 'self')),
        (('pull', 'inf', 'ally'),)
    )
}, 18: {
    'header': dict(name='vampire', type='monster'),
    'A': (
        dict(life='healthy', feature={'heavy'}, shield=()),
        (('wounded', '>2', (('resurrect', 'any', 'ally'), ('resurrect', 'any', 'ally'), ('resurrect', 'any', 'ally'),
                            ('rotate', 0, 'self'))),),
        (('hit', 'inf', 'enemy'), ('push', 5, 'enemy'))
    ),
    'B': (
        dict(life='healthy', feature={'heavy'}, shield=()),
        (('wounded', '>2', (('resurrect', 'any', 'ally'), ('resurrect', 'any', 'ally'), ('resurrect', 'any', 'ally'),
                            ('flip', 0, 'self'))),),
        (('push', 'inf', 'enemy'), ('push', 'inf', 'enemy'))
    ),
    'C': (
        dict(life='exhausted'),
        (('push', 'inf', 'enemy'), ('push', 'inf', 'enemy'))
    ),
    'D': (
        dict(life='wounded', feature={'heavy'}, shield=()),
        (('wounded', '>2', (('resurrect', 'any', 'ally'), ('resurrect', 'any', 'ally'), ('resurrect', 'any', 'ally'),
                            ('rotate', 0, 'self'))),),
        (('push', 'inf', 'enemy'),)
    )
}, 19: {
    'header': dict(name='pyromancer', type='hero'),
    'A': (
        dict(life='healthy', fire=(('rotate', 0, 'self'),)),
        (('pay fire', 2, (('heal', 'any', 'ally'), ('heal', 'any', 'ally'), ('rotate', 0, 'self'))),),
        (('pay fire', 1, (('maneuver', 'any', 'ally'), ('maneuver', 'any', 'ally'), ('delay', 2, 'any'),
                          ('rotate', 0, 'self'))),),
        (('delay', 1, 'any'), ('quicken', 1, 'any'))
    ),
    'B': (
        dict(life='wounded'),
        (('pay fire', 3, (('ablaze', None, 'all'), ('rotate', 0, 'self'))),),
        (('pay fire', 2, (('hit', 3, 'any'), ('hit', 3, 'any'))),),
        (('delay', 1, 'any'), ('quicken', 1, 'any'), ('rotate', 0, 'self'))
    ),
    'C': (
        dict(life='exhausted'),
        (('pay fire', 3, (('teleport', 'any', 'enemy'), ('hit', 2, 'any'))),),
        (('pay fire', 2, (('teleport', 'any', 'both'), ('rotate', 0, 'self'))),),
        (('teleport', 'any', 'ally'), ('rotate', 0, 'self'))
    ),
    'D': (
        dict(life='exhausted', fire=(('rotate', 0, 'self'),)),
        (('pay fire', 4, (('resurrect', 'any', 'ally'), ('rotate', 0, 'self'))),),
        (('maneuver', 'any', 'ally'), ('delay', 2, 'any'))
    )
}, 20: {
    'header': dict(name='pyromancer', type='hero'),
    'A': (
        dict(life='healthy'),
        (('pay fire', 2, (('ablaze', None, 'all'),)),),
        (('pay fire', 1, (('hit', 4, 'any'),)),),
        (('heal', 'any', 'ally'), ('maneuver', 'any', 'ally'), ('rotate', 0, 'self'))
    ),
    'B': (
        dict(life='wounded', fire=(('rotate', 0, 'self'),)),
        (('pay fire', 2, (('ablaze', None, 'all'), ('rotate', 0, 'self'))),),
        (('pay fire', 1, (('fireball', None, 'any'),)),),
        (('delay', 1, 'any'), ('quicken', 1, 'any'))
    ),
    'C': (
        dict(life='exhausted', fire=(('rotate', 0, 'self'),)),
        (('pay fire', 4, (('hit', 6, 'any'), ('hit', 6, 'any'), ('hit', 6, 'any'))),),
        (('pay fire', 2, (('resurrect', 'any', 'any'), ('heal', 'any', 'ally'), ('rotate', 0, 'self'))),),
        (('delay', 1, 'any'), ('quicken', 1, 'any'))
    ),
    'D': (
        dict(life='exhausted'),
        (('pay fire', 2, (('fireball', None, 'any'), ('rotate', 0, 'self'))),),
        (('pay fire', 1, (('hit', 3, 'any'),)),),
        (('heal', 'any', 'ally'), ('maneuver', 'any', 'ally'))
    )
}, 21: {
    'header': dict(name='pyromancer', type='hero'),
    'A': (
        dict(life='healthy'),
        (('pay fire', 2, (('fireball', None, 'any'), ('rotate', 0, 'self'))),),
        (('pay fire', 1, (('heal', 'any', 'ally'), ('heal', 'any', 'ally'), ('rotate', 0, 'self'))),),
        (('heal', 'any', 'ally'), ('maneuver', 'any', 'ally'), ('rotate', 0, 'self'))
    ),
    'B': (
        dict(life='wounded', fire=(('rotate', 0, 'self'),)),
        (('pay fire', 2, (('resurrect', 'any', 'any'), ('rotate', 0, 'self'))),),
        (('pay fire', 1, (('delay', 1, 'any'), ('quicken', 1, 'any'))),),
        (('heal', 'any', 'ally'), ('maneuver', 'any', 'ally'))
    ),
    'C': (
        dict(life='exhausted'),
        (('pay fire', 3, (('flip', 0, 'self'),)),),
        (('pay fire', 2, (('teleport', 'any', 'both'),)),),
        (('delay', 2, 'any'), ('maneuver', 'any', 'ally'), ('rotate', 0, 'self'))
    ),
    'D': (
        dict(life='exhausted', fire=(('rotate', 0, 'self'),)),
        (('pay fire', 3, (('resurrect', 'any', 'ally'),)),),
        (('pay fire', 2, (('ablaze', None, 'all'),)),),
        (('heal', 'any', 'ally'), ('rotate', 0, 'self'))
    )
}, 22: {
    'header': dict(name='pyromancer', type='hero'),
    'A': (
        dict(life='healthy', fire=(('rotate', 0, 'self'),)),
        (('pay fire', 2, (('teleport', 'any', 'both'),)),),
        (('pay fire', 2, (('teleport', 'any', 'ally'),)),),
        (('delay', 1, 'any'), ('quicken', 1, 'any'))
    ),
    'B': (
        dict(life='wounded'),
        (('pay fire', 2, (('hit', 5, 'any'), ('heal', 'any', 'ally'))),),
        (('pay fire', 1, (('teleport', 'any', 'enemy'), ('rotate', 0, 'self'))),),
        (('maneuver', 'any', 'ally'), ('heal', 'any', 'ally'))
    ),
    'C': (
        dict(life='exhausted', fire=(('rotate', 0, 'self'),)),
        (('pay fire', 2, (('fireball', None, 'any'), ('maneuver', 'any', 'ally'), ('rotate', 0, 'self'))),),
        (('pay fire', 1, (('hit', 1, 'any'), ('rotate', 0, 'self'))),),
        (('maneuver', 'any', 'ally'), ('maneuver', 'any', 'ally'))
    ),
    'D': (
        dict(life='exhausted'),
        (('pay fire', 2, (('ablaze', None, 'all'),)),),
        (('pay fire', 1, (('delay', 2, 'any'), ('quicken', 2, 'any'))),),
        (('delay', 1, 'any'), ('quicken', 1, 'any'), ('rotate', 0, 'self'))
    )
}, 23: {
    'header': dict(name='pyromancer', type='hero'),
    'A': (
        dict(life='healthy', fire=(('rotate', 0, 'self'),)),
        (('pay fire', 3, (('fireball', None, 'any'), ('fireball', None, 'any'))),),
        (('pay fire', 2, (('ablaze', None, 'all'), ('heal', 'any', 'ally'), ('flip', 0, 'self'))),),
        (('delay', 1, 'any'), ('maneuver', 'any', 'ally'))
    ),
    'B': (
        dict(life='wounded'),
        (('pay fire', 2, (('resurrect', 'any', 'ally'), ('rotate', 0, 'self'))),),
        (('pay fire', 2, (('hit', 5, 'any'), ('rotate', 0, 'self'))),),
        (('teleport', 'any', 'ally'),)
    ),
    'C': (
        dict(life='exhausted', fire=(('rotate', 0, 'self'),)),
        (('pay fire', 2, (('ablaze', None, 'all'),)),),
        (('pay fire', 1, (('heal', 'any', 'ally'), ('delay', 1, 'any'), ('rotate', 0, 'self'))),),
        (('quicken', 1, 'any'), ('maneuver', 'any', 'ally'))
    ),
    'D': (
        dict(life='exhausted'),
        (('pay fire', 2, (('hit', 3, 'any'), ('flip', 0, 'self'))),),
        (('teleport', 'any', 'ally'), ('rotate', 0, 'self'))
    )
}, 24: {
    'header': dict(name='spider', type='monster'),
    'A': (
        dict(life='healthy', feature={'venom'}),
        (('swarm', None, (('hit', 3, 'enemy'), ('pull', 3, 'ally'))),),
        (('hit', 5, 'enemy'), ('rotate', 0, 'self'))
    ),
    'B': (
        dict(life='healthy', feature={'venom'}),
        (('swarm', None, (('hit', 2, 'enemy'), ('push', 2, 'enemy'))),),
        (('push', 3, 'enemy'), ('hit', 2, 'enemy'))
    ),
    'C': (
        dict(life='exhausted', feature={'webs'}),
        (('swarm', None, (('heal', 'any', 'ally'),)),),
        (('hit', 'inf', 'enemy'),)
    ),
    'D': (
        dict(life='wounded', feature={'venom'}),
        (('swarm', None, (('pull', 4, 'ally'), ('push', 3, 'enemy'))),),
        (('hit', 3, 'enemy'),),
        (('resurrect', 'any', 'ally'),)
    )
}, 25: {
    'header': dict(name='spider', type='monster'),
    'A': (
        dict(life='healthy', feature={'venom'}),
        (('swarm', None, (('heal', 'any', 'ally'), ('rotate', 0, 'self'))),),
        (('push', 3, 'enemy'), ('hit', 3, 'enemy'))
    ),
    'B': (
        dict(life='healthy', feature={'venom'}),
        (('swarm', None, (('hit', 3, 'enemy'), ('push', 2, 'enemy'))),),
        (('hit', 5, 'enemy'), ('rotate', 0, 'self'))
    ),
    'C': (
        dict(life='exhausted', feature={'venom'}),
        (('swarm', None, (('push', 3, 'enemy'), ('pull', 5, 'ally'))),),
        (('push', 5, 'enemy'), ('hit', 2, 'enemy'))
    ),
    'D': (
        dict(life='wounded', feature={'webs'}),
        (('swarm', None, (('hit', 5, 'enemy'),)),),
        (('hit', 5, 'enemy'),)
    )
}, 26: {
    'header': dict(name='spider', type='monster'),
    'A': (
        dict(life='healthy', feature={'venom'}),
        (('swarm', None, (('hit', 'inf', 'enemy'),)),),
        (('pull', 4, 'enemy'), ('hit', 2, 'enemy'), ('rotate', 0, 'self')),
        (('hit', 5, 'enemy'),)
    ),
    'B': (
        dict(life='healthy', feature={'webs'}),
        (('swarm', None, (('hit', 4, 'enemy'),)),),
        (('push', 'inf', 'enemy'), ('push', 'inf', 'enemy'), ('push', 'inf', 'ally'), ('rotate', 0, 'self'))
    ),
    'C': (
        dict(life='exhausted', feature={'webs'}),
        (('swarm', None, (('resurrect', 'any', 'ally'),)),),
        (('heal', 'any', 'self'), ('push', 2, 'enemy')),
        (('hit', 4, 'enemy'), ('push', 4, 'enemy')),
    ),
    'D': (
        dict(life='wounded', feature={'venom'}),
        (('swarm', None, (('hit', 3, 'enemy'),)),),
        (('pull', 6, 'enemy'), ('pull', 6, 'enemy'))
    )
}, 27: {
    'header': dict(name='spider', type='monster'),
    'A': (
        dict(life='healthy', feature={'webs'}),
        (('swarm', None, (('hit', 5, 'enemy'),)),),
        (('hit', 3, 'enemy'), ('rotate', 0, 'self')),
        (('push', 3, 'enemy'), ('push', 3, 'enemy'))
    ),
    'B': (
        dict(life='healthy', feature={'venom'}, shield=(('rotate', None, 'self'),)),
        (('swarm', None, (('hit', 5, 'enemy'), ('hit', 5, 'enemy'))),)
    ),
    'C': (
        dict(life='exhausted', feature={'venom'}),
        (('swarm', None, (('hit', 'inf', 'enemy'),)),),
        (('hit', 5, 'enemy'), ('pull', 5, 'ally'))
    ),
    'D': (
        dict(life='wounded', feature={'webs'}),
        (('swarm', None, (('hit', 'inf', 'enemy'),)),),
        (('hit', 5, 'enemy'), ('pull', 5, 'ally'))
    )
}, 28: {
    'header': dict(name='cursed', type='hero'),
    'A': (
        dict(life='healthy'),
        (('delay', 1, 'ally'), ('heal', 'any', 'self')),
        (('maneuver', 'any', 'ally'), ('inspire', 'any', 'enemy'), ('maneuver', 'any', 'ally')),
        (('hit', 'inf', 'ally'), ('quicken', 1, 'enemy'))
    ),
    'B': (
        dict(life='exhausted'),
        (('inspire', 'any', 'enemy'), ('heal', 'any', 'self')),
        (('teleport', 'any', 'enemy'),)
    ),
    'C': (
        dict(life='wounded', shield=(('rotate', None, 'self'),), type={'werewolf'}),
        (('claws', 3, 'enemy'), ('rotate', 0, 'self'))
    ),
    'D': (
        dict(life='wounded'),
        (('delay', 2, 'ally'), ('rotate', 0, 'self')),
        (('quicken', 2, 'enemy'),),
        (('maneuver', 'any', 'ally'),)
    )
}, 29: {
    'header': dict(name='cursed', type='hero'),
    'A': (
        dict(life='healthy'),
        (('hit', 'inf', 'ally'), ('quicken', 1, 'enemy')),
        (('delay', 1, 'any'), ('quicken', 1, 'any'), ('maneuver', 'any', 'ally')),
        (('inspire', 'any', 'enemy'), ('quicken', 2, 'any'))
    ),
    'B': (
        dict(life='exhausted'),
        (('maneuver', 'any', 'ally'), ('quicken', 2, 'enemy'), ('inspire', 'any', 'enemy')),
        (('heal', 'any', 'self'),)
    ),
    'C': (
        dict(life='wounded', shield=(('rotate', None, 'self'),), type={'werewolf'}),
        (('claws', 3, 'enemy'), ('rotate', 0, 'self')),
        (('pull', 'inf', 'enemy'), ('hit', 1, 'enemy'), ('hit', 1, 'enemy'), ('hit', 1, 'enemy'))
    ),
    'D': (
        dict(life='wounded'),
        (('inspire', 'any', 'enemy'), ('maneuver', 'any', 'ally'), ('rotate', 0, 'self')),
        (('delay', 2, 'ally'), ('quicken', 2, 'enemy'))
    )
}, 30: {
    'header': dict(name='cursed', type='hero'),
    'A': (
        dict(life='healthy'),
        (('quicken', 2, 'any'), ('quicken', 2, 'any'), ('inspire', 'any', 'enemy')),
        (('delay', 1, 'ally'), ('hit', 'inf', 'ally'))
    ),
    'B': (
        dict(life='exhausted'),
        (('maneuver', 'any', 'ally'), ('quicken', 2, 'enemy'), ('inspire', 'any', 'enemy')),
        (('heal', 'any', 'eny'), ('inspire', 'any', 'enemy'))
    ),
    'C': (
        dict(life='wounded', shield=(('rotate', None, 'self'),), type={'werewolf'}),
        (('hit', 2, 'enemy'), ('hit', 2, 'enemy'), ('rotate', 0, 'self')),
        (('claws', 4, 'enemy'), )
    ),
    'D': (
        dict(life='wounded'),
        (('maneuver', 'any', 'ally'), ('heal', 'any', 'any'), ('rotate', 0, 'self')),
        (('delay', 1, 'ally'), ('quicken', 1, 'enemy')),
        (('teleport', 'any', 'both'),)
    )
}, 31: {
    'header': dict(name='cursed', type='hero'),
    'A': (
        dict(life='healthy'),
        (('heal', 'any', 'enemy'), ('maneuver', 'any', 'ally')),
        (('quicken', 2, 'enemy'), ('delay', 2, 'ally'), ('inspire', 'any', 'enemy')),
        (('hit', 'inf', 'enemy'), ('quicken', 1, 'enemy'))
    ),
    'B': (
        dict(life='healthy'),
        (('teleport', 'any', 'enemy'), ('inspire', 'any', 'enemy')),
        (('teleport', 'any', 'both'), ('maneuver', 'any', 'ally'))
    ),
    'C': (
        dict(life='wounded', shield=(('rotate', None, 'self'),), type={'werewolf'}),
        (('hit', 2, 'enemy'), ('hit', 2, 'enemy'), ('push', 2, 'enemy'), ('rotate', 0, 'self')),
        (('hit', 'inf', 'enemy'), ('hit', 'inf', 'enemy'))
    ),
    'D': (
        dict(life='wounded'),
        (('heal', 'any', 'enemy'), ('rotate', 0, 'self')),
        (('teleport', 'any', 'both'), ('maneuver', 'any', 'ally')),
        (('hit', 'inf', 'enemy'), ('delay', 1, 'enemy'))
    )
}, 32: {
    'header': dict(name='werewolf', type='monster'),
    'A': (
        dict(life='healthy'),
        (('teleport', 'any', 'enemy'), ('inspire', 'any', 'enemy')),
        (('maneuver', 'any', 'ally'), ('heal', 'any', 'enemy'), ('rotate', 0, 'self')),
        (('hit', 'inf', 'ally'), ('delay', 1, 'enemy'))
    ),
    'B': (
        dict(life='exhausted'),
        (('hit', 'inf', 'ally'), ('inspire', 'any', 'enemy'), ('maneuver', 'any', 'ally')),
        (('quicken', 1, 'any'), ('delay', 1, 'any'))
    ),
    'C': (
        dict(life='wounded', shield=(('rotate', None, 'self'),), type={'werewolf'}),
        (('pull', 6, 'enemy'), ('hit', 3, 'enemy'), ('hit', 3, 'enemy'), ('hit', 3, 'enemy'), ('rotate', 0, 'self')),
        (('hit', 'inf', 'enemy'),)
    ),
    'D': (
        dict(life='wounded'),
        (('inspire', 'any', 'enemy'), ('inspire', 'any', 'enemy'), ('delay', 1, 'any')),
        (('teleport', 'any', 'enemy'), ('maneuver', 'any', 'ally')),
        (('heal', 'any', 'enemy'), ('rotate', 0, 'self'))
    )
}, 33: {
    'header': dict(name='demon', type='monster'),
    'A': (
        dict(life='healthy'),
        (('count rage', '>3', (('pull', 'inf', 'enemy'), ('hit', 1, 'enemy'), ('hit', 1, 'enemy'))),),
        (('count rage', '>2', (('pull', 'inf', 'enemy'), ('hit', 1, 'enemy'))),),
        (('push', 3, 'enemy'), ('push', 3, 'enemy'))
    ),
    'B': (
        dict(life='healthy', rage=2),
        (('count rage', '>3', (('pull', 5, 'ally'), ('rotate', 0, 'self'))),),
        (('count rage', '>2', (('pull', 5, 'ally'), ('push', 5, 'enemy'))),),
        (('hit', 3, 'enemy'), ('push', 3, 'enemy'))
    ),
    'C': (
        dict(life='exhausted', rage=2, shield=(('rotate', None, 'self'),)),
        (('count rage', '>4', (('void', 'any', 'enemy'),)),),
        (('count rage', '>2', (('hit', 1, 'enemy'), ('hit', 2, 'enemy'), ('hit', 3, 'enemy'))),),
        (('hit', 2, 'enemy'), ('hit', 2, 'enemy'), ('rotate', 0, 'self'))
    ),
    'D': (
        dict(life='exhausted', rage=1, shield=(('rotate', None, 'self'),)),
        (('count rage', '>4', (('death', 'all', 'enemy'),)),),
        (('count rage', '>3', (('claws', 4, 'enemy'), ('rotate', 0, 'self'))),),
        (('quicken', 5, 'ally'), ('rotate', 0, 'self'))
    )
}, 34: {
    'header': dict(name='demon', type='monster'),
    'A': (
        dict(life='healthy'),
        (('count rage', '>5', (('death', 'all', 'enemy'),)),),
        (('count rage', '>3', (('void', 'any', 'enemy'),)),),
        (('hit', 'inf', 'enemy'),)
    ),
    'B': (
        dict(life='healthy', rage=1),
        (('count rage', '>4', (('void', 'any', 'enemy'), ('rotate', 0, 'self'))),),
        (('count rage', '>4', (('hit', 'inf', 'enemy'),)),),
        (('claws', 3, 'enemy'),)
    ),
    'C': (
        dict(life='wounded', rage=2, shield=(('rotate', None, 'self'),)),
        (('count rage', '>4', (('death', 'all', 'enemy'),)),),
        (('count rage', '>3', (('pull', 5, 'enemy'), ('hit', 1, 'enemy'), ('hit', 1, 'enemy'), ('push', 1, 'enemy'))),),
        (('pull', 5, 'enemy'), ('hit', 1, 'enemy'), ('hit', 1, 'enemy'))
    ),
    'D': (
        dict(life='exhausted', rage=1, shield=(('rotate', None, 'self'),)),
        (('count rage', '>4', (('death', 'all', 'enemy'),)),),
        (('count rage', '>2', (('hit', 'inf', 'enemy'), ('push', 'inf', 'enemy'), ('rotate', 0, 'self'))),),
        (('hit', 'inf', 'enemy'), ('rotate', 0, 'self'))
    )
}, 35: {
    'header': dict(name='demon', type='monster'),
    'A': (
        dict(life='healthy'),
        (('count rage', '>5', (('claws', 'inf', 'enemy'),)),),
        (('count rage', '>2', (('claws', 'inf', 'enemy'),)),),
        (('claws', 2, 'enemy'),),
    ),
    'B': (
        dict(life='healthy'),
        (('count rage', '>4', (('claws', 6, 'enemy'), ('rotate', 0, 'self'))),),
        (('count rage', '>3', (('claws', 4, 'enemy'), ('rotate', 0, 'self'))),),
        (('hit', 'inf', 'enemy'),)
    ),
    'C': (
        dict(life='exhausted', rage=1, shield=(('rotate', None, 'self'),)),
        (('count rage', '>4', (('death', 'all', 'enemy'),)),),
        (('claws', 4, 'enemy'), ('rotate', 0, 'self'))
    ),
    'D': (
        dict(life='exhausted', rage=1, shield=(('rotate', None, 'self'),)),
        (('count rage', '>5', (('death', 'all', 'enemy'),)),),
        (('count rage', '>3', (('hit', 'inf', 'enemy'), ('hit', 'inf', 'enemy'), ('rotate', 0, 'self'))),),
        (('hit', 'inf', 'enemy'), ('rotate', 0, 'self'))
    )
}, 36: {
    'header': dict(name='demon', type='monster'),
    'A': (
        dict(life='healthy', rage=0),
        (('count rage', '>3', (('void', 'any', 'enemy'),)),),
        (('count rage', '>2', (('hit', 4, 'enemy'), ('hit', 4, 'enemy'))),),
        (('hit', 'inf', 'enemy'),)
    ),
    'B': (
        dict(life='exhausted', rage=1),
        (('count rage', '>4', (('hit', 'inf', 'enemy'), ('hit', 'inf', 'enemy'), ('rotate', 0, 'self'))),),
        (('count rage', '>3', (('hit', 'inf', 'enemy'), ('rotate', 0, 'self'))),),
        (('hit', 4, 'enemy'),)
    ),
    'C': (
        dict(life='healthy', rage=3, shield=(('rotate', None, 'self'),)),
        (('count rage', '>5', (('death', 'all', 'enemy'),)),),
        (('count rage', '>3', (('void', 'any', 'enemy'),)),),
        (('pull', 5, 'ally'), ('rotate', 0, 'self'))
    ),
    'D': (
        dict(life='exhausted', rage=1, shield=(('rotate', None, 'self'),)),
        (('count rage', '>4', (('void', 'any', 'enemy'),)),),
        (('count rage', '>3', (('pull', 5, 'enemy'), ('hit', 1, 'enemy'), ('pull', 5, 'enemy'), ('hit', 1, 'enemy'),
                               ('rotate', 0, 'self'))),),
        (('pull', 5, 'enemy'), ('hit', 1, 'enemy'), ('rotate', 0, 'self'))
    )}}

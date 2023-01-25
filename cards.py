"""
content of the file
    A tuple of all cards ordered by the number of the cards


deck : tuple
    A deck consists of a tuple of cards.
    The deck is represented as a tuple of tuples (cards) from top (start=0) to bottom (end=len(deck)-1).

card : tuple
    A card consists of a tuple of one header (dict) and four faces.

header (to the card) : dict
    The card header (dict) identifies and specifies the card and contains the following keys:
    - name : str ("warrior", "ogre", "huntress", "vampire", "pyromancer", "spider")
    - type : str ("hero", "monster")
    - number : int, the card number

face : tuple
    A face consists of a list of one header and one or more rows (of actions).

header (to the face) : dict
    The face header (dict) identifies and specifies the face and contains the following keys:

    - face : str ("A", "B", "C", "D")
    - life : str ("healthy", "wounded", "exhausted")
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
        example (condition, (("fire", 2, "ally"), ("ablaze", None, "enemy"), ("hit", 2, "enemy"),))

    The following targets are recognised
    - "enemy"
    - "ally"
    - "any"
"""

cards = ((  # card 1
    dict(name="warrior", type="hero", number=1),
    (
        dict(face="A", life="healthy"),
        (("hit", 2, "enemy"),),
        (("delay", 2, "any"), ("rotate", None, "self"),)
    ),
    (
        dict(face="B", life="healthy", reaction="shield", shield="rotate"),
        (("delay", 1, "any"), ("hit", 2, "enemy"),),
        (("delay", 2, "any"),)
    ),
    (
        dict(face="C", life="exhausted"),
        (("hit", 2, "enemy"), ),
        (("delay", 2, "any"), )
    ),
    (
        dict(face="D", life="wounded"),
        (("hit", 4, "enemy"),),
        (("quicken", 2, "any"),)
    )
), (
    dict(name="warrior", type="hero", number=2),
    (
        dict(face="A", life="healthy"),
        (("hit", 2, "enemy"), ("rotate", None, "self"),),
        (("delay", 2, "any"),)
    ),
    (
        dict(face="B", life="healthy", reaction="shield", shield="rotate"),
        (("heal", None, "ally"), ("rotate", None, "self"),),
        (("quicken", 2, "any"),)
    ),
    (
        dict(face="C", life="exhausted"),
        (("quicken", 2, "any"),),
        (("delay", 2, "any"),)
    ),
    (
        dict(face="D", life="wounded"),
        (("heal", None, "ally"), ("rotate", None, "self"),),
        (("delay", 3, "any"),)
    )
), (
    dict(name="warrior", type="hero", number=3),
    (
        dict(face="A", life="healthy"),
        (("delay", 2, "any"), ("rotate", None, "self"),),
        (("quicken", 2, "any"), ("rotate", None, ),)
    ),
    (
        dict(face="B", life="healthy"),
        (("hit", 4, "enemy"), ("hit", 4, "enemy"), ("rotate", None, "self"),)
    ),
    (
        dict(face="C", life="exhausted"),
        (("quicken", 2, "any"),),
        (("delay", 2, "any"),)
    ),
    (
        dict(face="D", life="wounded"),
        (("hit", 4, "enemy"),),
        (("delay", 1, "any"),)
    )
), (
    dict(name="warrior", type="hero", number=4),
    (
        dict(face="A", life="healthy", reaction="shield", shield="rotate"),
        (("hit", 4, "enemy"),),
        (("quicken", 2, "any"),)
    ),
    (
        dict(face="B", life="healthy"),
        (("hit", 2, "enemy"),),
        (("delay", 1, "any"), ("quicken", 1, "any"), ("rotate", None, "self"),)
    ),
    (
        dict(face="C", life="wounded"),
        (("hit", 4, "enemy"),),
        (("quicken", 1, "any"),)
    ),
    (
        dict(face="D", life="exhausted"),
        (("hit", 2, "enemy"),),
        (("heal", None, "ally"),)
    )
), (
    dict(name="warrior", type="hero", number=5),
    (
        dict(face="A", life="healthy", reaction="shield", shield="rotate"),
        (("quicken", 2, "any"), ("hit", 2, "enemy"),)
    ),
    (
        dict(face="B", life="healthy"),
        (("hit", 2, "enemy"), ("rotate", None, "self"),),
        (("quicken", 2, "any"), ("rotate", None, "self"),)
    ),
    (
        dict(face="C", life="wounded"),
        (("delay", 3, "any"), ("hit", 2, "enemy"), ("hit", 2, "enemy"), ("rotate", None, "self"),),
        (("quicken", 2, "any"),)
    ),
    (
        dict(face="D", life="exhausted"),
        (("hit", 4, "enemy"),),
        (("quicken", 1, "any"),)
    )
), (  # card 6
    dict(name="ogre", type="monster", number=6),
    (
        dict(face="A", life="healthy"),
        (("pull", 5, "enemy"), ("hit", 1, "enemy"), ("rotate", None, "self"),)
    ),
    (
        dict(face="B", life="healthy", reaction="shield", shield="rotate"),
        (("hit", 4, "enemy"), ("push", 3, "enemy"),),
    ),
    (
        dict(face="C", life="exhausted"),
        (("hit", 5, "enemy"),),
    ),
    (
        dict(face="D", life="wounded", feature={"heavy"}, reaction="shield"),
        (("hit", 0, "enemy"), ("hit", 0, "enemy"), ("rotate", None, "self"),),
    )
), (
    dict(name="ogre", type="monster", number=7),
    (
        dict(face="A", life="healthy", feature={"heavy"}),
        (("hit", 4, "enemy"), ("rotate", None, "self"),),
    ),
    (
        dict(face="B", life="healthy", reaction="shield", shield="rotate"),
        (("heal", None, "ally"), ("rotate", None, "self"),),
        (("hit", 7, "enemy"), ("rotate", None, "self"),)
    ),
    (
        dict(face="C", life="exhausted"),
        (("hit", 5, "enemy"), ("pull", 4, "ally"),),
    ),
    (
        dict(face="D", life="wounded"),
        (("push", 3, "enemy"), ("hit", 5, "enemy"),)
    )
), (
    dict(name="ogre", type="monster", number=8),
    (
        dict(face="A", life="healthy"),
        (("hit", 4, "enemy"), ("rotate", None, "self"),),
    ),
    (
        dict(face="B", life="healthy", feature={"heavy"}),
        (("heal", None, "ally"), ("rotate", None, "self"),),
        (("hit", 5, "enemy"), ("rotate", None, "self"),)
    ),
    (
        dict(face="C", life="exhausted"),
        (("pull", 6, "enemy"), ("hit", 1, "enemy"),),
    ),
    (
        dict(face="D", life="wounded"),
        (("pull", 4, "enemy"), ("hit", 1, "enemy"),)
    )
), (
    dict(name="ogre", type="monster", number=9),
    (
        dict(face="A", life="healthy"),
        (("push", 3, "enemy"), ("push", 3, "enemy"), ("rotate", None, "self"),)
    ),
    (
        dict(face="B", life="healthy", reaction=("shield", "rotate"),),
        (("hit", 5, "enemy"), ("rotate", None, "self"),),
    ),
    (
        dict(face="C", life="exhausted", feature={"heavy"}),
        (("hit", 0, "enemy"),),
    ),
    (
        dict(face="D", life="wounded"),
        (("heal", None, "ally"), ("heal", None, "ally"), ("heal", None, "ally"), ("rotate", None, "self"),),
        (("pull", 5, "ally"),)
    )
), (
    dict(name="huntress", type="hero", number=10),
    (
        dict(face="A", life="healthy", feature={"trap"}),
        (("arrow", 1, "enemy"), ("rotate", None, "self"),),
        (("delay", 2, "ally"), ("maneuver", None, "ally"),)
    ),
    (
        dict(face="B", life="healthy", feature={"trap"}),
        (("quicken", 2, "enemy"), ("maneuver", None, "ally"), ("rotate", None, "self"),),
        (("heal", None, "ally"),)
    ),
    (
        dict(face="C", life="exhausted", feature={"trap"}),
        (("maneuver", None, "ally"),),
        (("hit", 1, "enemy"),),
        (("delay", 1, "any"),)
    ),
    (
        dict(face="D", life="wounded", feature={"trap"}),
        (("arrow", 2, "enemy"),),
        (("maneuver", None, "ally"),),
        (("quicken", 1, "any"),)
    )
), (
    dict(name="huntress", type="hero", number=11),
    (
        dict(face="A", life="healthy", reaction="dodge", dodge="rotate"),
        (("arrow", 1, "enemy"), ("rotate", None, "self"),),
        (("quicken", 2, "enemy"), ("maneuver", None, "ally"), ("rotate", None, "self"),),
        (("hit", 1, "enemy"), ("rotate", None, "self"),)
    ),
    (
        dict(face="B", life="healthy"),
        (("delay", 2, "hero"),),
        (("quicken", 2, "enemy"),),
        (("maneuver", None, "ally"), ("maneuver", None, "ally"),)
    ),
    (
        dict(face="C", life="wounded"),
        (("hit", 1, "enemy"), ("hit", 1, "enemy"), ("rotate", None, "self"),),
        (("quicken", 2, "enemy"), ("maneuver", None, "ally"),)
    ),
    (
        dict(face="D", life="exhausted"),
        (("hit", 1, "enemy"), ("maneuver", None, "ally"), ("delay", 2, "hero"),)
    )
), (
    dict(name="huntress", type="hero", number=12),
    (
        dict(face="A", life="healthy", reaction="dodge", dodge="rotate"),
        (("maneuver", None, "ally"), ("quicken", 2, "enemy"), ("rotate", None, "self"),),
        (("delay", 1, "any"), ("rotate", None, "self"),)
    ),
    (
        dict(face="B", life="healthy", feature={"trap"}),
        (("arrow", 2, "enemy"),),
        (("delay", 2, "hero"), ("maneuver", None, "ally"),)
    ),
    (
        dict(face="C", life="wounded", feature={"trap"}),
        (("delay", 2, "hero"), ("arrow", 1, "enemy"),),
        (("maneuver", None, "ally"),)
    ),
    (
        dict(face="D", life="exhausted", feature={"trap"}),
        (("delay", 2, "hero"), ("quicken", 2, "enemy"),),
        (("maneuver", None, "ally"), ("hit", 1, "enemy"),)
    )
), (
    dict(name="huntress", type="hero", number=13),
    (
        dict(face="A", life="healthy", feature={"trap"}),
        (("maneuver", None, "ally"), ("rotate", None, "self"),),
        (("hit", 1, "enemy"),),
        (("delay", 1, "any"),)
    ),
    (
        dict(face="B", life="healthy"),
        (("arrow", 1, "enemy"), ("rotate", None, "self"),),
        (("maneuver", None, "ally"), ("hit", 1, "enemy"), ("rotate", None, "self"),),
        (("quicken", 2, "enemy"),)
    ),
    (
        dict(face="C", life="exhausted", feature={"trap"}),
        (("arrow", 1, "enemy"),),
        (("maneuver", None, "ally"),),
        (("delay", 1, "any"),)
    ),
    (
        dict(face="D", life="wounded"),
        (("arrow", 1, "enemy"),),
        (("quicken", 2, "enemy"), ("maneuver", None, "ally"),)
    )
), (
    dict(name="huntress", type="hero", number=14),
    (
        dict(face="A", life="healthy", reaction="dodge", dodge="rotate"),
        (("arrow", 1, "enemy"), ("rotate", None, "self"),),
        (("quicken", 2, "enemy"), ("rotate", None, "self"),)
    ),
    (
        dict(face="B", life="healthy"),
        (("arrow", 2, "enemy"),),
        (("delay", 2, "hero"), ("maneuver", None, "ally"),),
        (("heal", None, "ally"),)
    ),
    (
        dict(face="C", life="wounded", feature={"trap"}),
        (("delay", 2, "hero"), ("quicken", 2, "enemy"),),
        (("maneuver", None, "ally"), ("hit", 1, "enemy"),)
    ),
    (
        dict(face="D", life="exhausted"),
        (("arrow", 1, "enemy"),),
        (("delay", 2, "hero"),),
        (("heal", None, "ally"),)
    )
), (
    dict(name="vampire", type="monster", number=15),
    (
        dict(face="A", life="healthy"),
        (),
        ()
    ),
    (
        dict(face="B", life="healthy"),
        (),
        (),
        ()
    ),
    (
        dict(face="C", life="wounded"),
        (),
        ()
    ),
    (
        dict(face="D", life="exhausted"),
        (),
        (),
        ()
    )
), (
    dict(name="vampire", type="monster", number=16),
    (
        dict(face="A", life="healthy"),
        (),
        ()
    ),
    (
        dict(face="B", life="healthy"),
        (),
        (),
        ()
    ),
    (
        dict(face="C", life="wounded"),
        (),
        ()
    ),
    (
        dict(face="D", life="exhausted"),
        (),
        (),
        ()
    )
), (
    dict(name="vampire", type="monster", number=17),
    (
        dict(face="A", life="healthy"),
        (),
        ()
    ),
    (
        dict(face="B", life="healthy"),
        (),
        (),
        ()
    ),
    (
        dict(face="C", life="wounded"),
        (),
        ()
    ),
    (
        dict(face="D", life="exhausted"),
        (),
        (),
        ()
    )
), (
    dict(name="vampire", type="monster", number=18),
    (
        dict(face="A", life="healthy"),
        (),
        ()
    ),
    (
        dict(face="B", life="healthy"),
        (),
        (),
        ()
    ),
    (
        dict(face="C", life="wounded"),
        (),
        ()
    ),
    (
        dict(face="D", life="exhausted"),
        (),
        (),
        ()
    )
), (
    dict(name="pyromancer", type="hero", number=19),
    (
        dict(face="A", life="healthy"),
        (),
        ()
    ),
    (
        dict(face="B", life="healthy"),
        (),
        (),
        ()
    ),
    (
        dict(face="C", life="wounded"),
        (),
        ()
    ),
    (
        dict(face="D", life="exhausted"),
        (),
        (),
        ()
    )
), (
    dict(name="pyromancer", type="hero", number=20),
    (
        dict(face="A", life="healthy"),
        (),
        ()
    ),
    (
        dict(face="B", life="healthy"),
        (),
        (),
        ()
    ),
    (
        dict(face="C", life="wounded"),
        (),
        ()
    ),
    (
        dict(face="D", life="exhausted"),
        (),
        (),
        ()
    )
), (
    dict(name="pyromancer", type="hero", number=21),
    (
        dict(face="A", life="healthy"),
        (),
        ()
    ),
    (
        dict(face="B", life="healthy"),
        (),
        (),
        ()
    ),
    (
        dict(face="C", life="wounded"),
        (),
        ()
    ),
    (
        dict(face="D", life="exhausted"),
        (),
        (),
        ()
    )
), (
    dict(name="pyromancer", type="hero", number=22),
    (
        dict(face="A", life="healthy"),
        (),
        ()
    ),
    (
        dict(face="B", life="healthy"),
        (),
        (),
        ()
    ),
    (
        dict(face="C", life="wounded"),
        (),
        ()
    ),
    (
        dict(face="D", life="exhausted"),
        (),
        (),
        ()
    )
), (
    dict(name="pyromancer", type="hero", number=23),
    (
        dict(face="A", life="healthy"),
        (),
        ()
    ),
    (
        dict(face="B", life="healthy"),
        (),
        (),
        ()
    ),
    (
        dict(face="C", life="wounded"),
        (),
        ()
    ),
    (
        dict(face="D", life="exhausted"),
        (),
        (),
        ()
    )
), (
    dict(name="spider", type="monster", number=24),
    (
        dict(face="A", life="healthy"),
        (),
        ()
    ),
    (
        dict(face="B", life="healthy"),
        (),
        (),
        ()
    ),
    (
        dict(face="C", life="wounded"),
        (),
        ()
    ),
    (
        dict(face="D", life="exhausted"),
        (),
        (),
        ()
    )
), (
    dict(name="spider", type="monster", number=25),
    (
        dict(face="A", life="healthy"),
        (),
        ()
    ),
    (
        dict(face="B", life="healthy"),
        (),
        (),
        ()
    ),
    (
        dict(face="C", life="wounded"),
        (),
        ()
    ),
    (
        dict(face="D", life="exhausted"),
        (),
        (),
        ()
    )
), (
    dict(name="spider", type="monster", number=26),
    (
        dict(face="A", life="healthy"),
        (),
        ()
    ),
    (
        dict(face="B", life="healthy"),
        (),
        (),
        ()
    ),
    (
        dict(face="C", life="wounded"),
        (),
        ()
    ),
    (
        dict(face="D", life="exhausted"),
        (),
        (),
        ()
    )
), (
    dict(name="spider", type="monster", number=27),
    (
        dict(face="A", life="healthy"),
        (),
        ()
    ),
    (
        dict(face="B", life="healthy"),
        (),
        (),
        ()
    ),
    (
        dict(face="C", life="wounded"),
        (),
        ()
    ),
    (
        dict(face="D", life="exhausted"),
        (),
        (),
        ()
    )
), (
    dict(name="werewolf", type="monster", number=28),
    (
        dict(face="A", life="healthy"),
        (),
        ()
    ),
    (
        dict(face="B", life="healthy"),
        (),
        (),
        ()
    ),
    (
        dict(face="C", life="wounded"),
        (),
        ()
    ),
    (
        dict(face="D", life="exhausted"),
        (),
        (),
        ()
    )
), (
    dict(name="werewolf", type="monster", number=29),
    (
        dict(face="A", life="healthy"),
        (),
        ()
    ),
    (
        dict(face="B", life="healthy"),
        (),
        (),
        ()
    ),
    (
        dict(face="C", life="wounded"),
        (),
        ()
    ),
    (
        dict(face="D", life="exhausted"),
        (),
        (),
        ()
    )
), (
    dict(name="werewolf", type="monster", number=30),
    (
        dict(face="A", life="healthy"),
        (),
        ()
    ),
    (
        dict(face="B", life="healthy"),
        (),
        (),
        ()
    ),
    (
        dict(face="C", life="wounded"),
        (),
        ()
    ),
    (
        dict(face="D", life="exhausted"),
        (),
        (),
        ()
    )
), (
    dict(name="werewolf", type="monster", number=31),
    (
        dict(face="A", life="healthy"),
        (),
        ()
    ),
    (
        dict(face="B", life="healthy"),
        (),
        (),
        ()
    ),
    (
        dict(face="C", life="wounded"),
        (),
        ()
    ),
    (
        dict(face="D", life="exhausted"),
        (),
        (),
        ()
    )
), (
    dict(name="werewolf", type="monster", number=32),
    (
        dict(face="A", life="healthy"),
        (),
        ()
    ),
    (
        dict(face="B", life="healthy"),
        (),
        (),
        ()
    ),
    (
        dict(face="C", life="wounded"),
        (),
        ()
    ),
    (
        dict(face="D", life="exhausted"),
        (),
        (),
        ()
    )
), (
    dict(name="demon", type="monster", number=33),
    (
        dict(face="A", life="healthy"),
        (),
        ()
    ),
    (
        dict(face="B", life="healthy"),
        (),
        (),
        ()
    ),
    (
        dict(face="C", life="wounded"),
        (),
        ()
    ),
    (
        dict(face="D", life="exhausted"),
        (),
        (),
        ()
    )
), (
    dict(name="demon", type="monster", number=34),
    (
        dict(face="A", life="healthy"),
        (),
        ()
    ),
    (
        dict(face="B", life="healthy"),
        (),
        (),
        ()
    ),
    (
        dict(face="C", life="wounded"),
        (),
        ()
    ),
    (
        dict(face="D", life="exhausted"),
        (),
        (),
        ()
    )
), (
    dict(name="demon", type="monster", number=35),
    (
        dict(face="A", life="healthy"),
        (),
        ()
    ),
    (
        dict(face="B", life="healthy"),
        (),
        (),
        ()
    ),
    (
        dict(face="C", life="wounded"),
        (),
        ()
    ),
    (
        dict(face="D", life="exhausted"),
        (),
        (),
        ()
    )
), (
    dict(name="demon", type="monster", number=36),
    (
        dict(face="A", life="healthy"),
        (),
        ()
    ),
    (
        dict(face="B", life="healthy"),
        (),
        (),
        ()
    ),
    (
        dict(face="C", life="wounded"),
        (),
        ()
    ),
    (
        dict(face="D", life="exhausted"),
        (),
        (),
        ()
    )
),)

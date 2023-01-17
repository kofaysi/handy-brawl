"""
List of all cards ordered by the number of the cards
A card consists of a header (dict) and four faces (lists).
The card header contains the following keys:
    name : str ["warrior", "ogre", "ranger", "vampire", "pyromancer", "venomous"]
    type : str ["hero", "monster"]
    number : int, the card number
A face consists of a header (dict) identifying and specifying the face and lists of actions (row-by-row).
A face header contains the following keys
    face : str ["A", "B", "C", "D"]
    life : str ["healthy", "wounded", "exhausted"]
    feature : set of str (mandatory, at least empty set {})
    reaction : str (optional)
    shield : str (optional)
An action (str) consist of the action name (str) and specifier (int or str)
The following action names are recognised (as expected at the end of the development)
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
"""

cards = [[  # card 1
    dict(name="warrior", type="hero", number=1),
    [
        dict(face="A", life="healthy", feature={"light"}),
        [("hit", 2)],
        [("delay", 2), ("rotate", None)]
    ],
    [
        dict(face="B", life="healthy", feature={}, reaction="shield", shield="rotate"),
        [("delay", 1), ("hit", 2)],
        [("delay", 2)]
    ],
    [
        dict(face="C", life="exhausted", feature={}),
        [("hit", 2)],
        [("delay", 2)]
    ],
    [
        dict(face="D", life="wounded", feature={}),
        [("hit", 4)],
        [("quicken", 2)]
    ]
], [
    dict(name="warrior", type="hero", number=2),
    [
        dict(face="A", life="healthy", feature={}),
        [("hit", 2), ("rotate", None)],
        [("delay", 2)]
    ],
    [
        dict(face="B", life="healthy", feature={}, reaction="shield", shield="rotate"),
        [("heal", None), ("rotate", None)],
        [("quicken", 2)]
    ],
    [
        dict(face="C", life="exhausted", feature={}),
        [("quicken", 2)],
        [("delay", 2)]
    ],
    [
        dict(face="D", life="wounded", feature={}),
        [("heal", None), ("rotate", None)],
        [("delay", 3)]
    ]
], [
    dict(name="warrior", type="hero", number=3),
    [
        dict(face="A", life="healthy", feature={}),
        [("delay", 2), ("rotate", None)],
        [("quicken", 2), ("rotate", None)]
    ],
    [
        dict(face="B", life="healthy", feature={}),
        [("hit", 4), ("hit", 4), ("rotate", None)]
    ],
    [
        dict(face="C", life="exhausted", feature={}),
        [("quicken", 2)],
        [("delay", 2)]
    ],
    [
        dict(face="D", life="wounded", feature={}),
        [("hit", 4)],
        [("delay", 1)]
    ]
], [
    dict(name="warrior", type="hero", number=4),
    [
        dict(face="A", life="healthy", feature={}, reaction="shield", shield="rotate"),
        [("hit", 4)],
        [("quicken", 2)]
    ],
    [
        dict(face="B", life="healthy", feature={}),
        [("hit", 2)],
        [("delay", 1), ("quicken", 1), ("rotate", None)]
    ],
    [
        dict(face="C", life="wounded", feature={}),
        [("hit", 4)],
        [("quicken", 1)]
    ],
    [
        dict(face="D", life="exhausted", feature={}),
        [("hit", 2)],
        [("heal", None)]
    ]
], [
    dict(name="warrior", type="hero", number=5),
    [
        dict(face="A", life="healthy", feature={}, reaction="shield", shield="rotate"),
        [("quicken", 2), ("hit", 2)]
    ],
    [
        dict(face="B", life="healthy", feature={}),
        [("hit", 2), ("rotate", None)],
        [("quicken", 2), ("rotate", None)]
    ],
    [
        dict(face="C", life="wounded", feature={}),
        [("delay", 3), ("hit", 2), ("hit", 2), ("rotate", None)],
        [("quicken", 2)]
    ],
    [
        dict(face="D", life="exhausted", feature={}),
        [("hit", 4)],
        [("quicken", 1)]
    ]
], [  # card 6
    dict(name="ogre", type="monster", number=6),
    [
        dict(face="A", life="healthy", feature={}),
        [("pull enemy", 5), ("hit", 1), ("rotate", None)]
    ],
    [
        dict(face="B", life="healthy", feature={}, reaction="shield", shield="rotate"),
        [("hit", 4), ("push enemy", 3)],
    ],
    [
        dict(face="C", life="exhausted", feature={}),
        [("hit", 5)],
    ],
    [
        dict(face="D", life="wounded", feature={"heavy"}, reaction="shield"),
        [("hit", 0), ("hit", 0), ("rotate", None)],
    ]
], [
    dict(name="ogre", type="monster", number=7),
    [
        dict(face="A", life="healthy", feature={"heavy"}),
        [("hit", 4), ("rotate", None)],
    ],
    [
        dict(face="B", life="healthy", feature={}, reaction="shield", shield="rotate"),
        [("heal", None), ("rotate", None)],
        [("hit", 7), ("rotate", None)]
    ],
    [
        dict(face="C", life="exhausted", feature={}),
        [("hit", 5), ("pull ally", 3)],
    ],
    [
        dict(face="D", life="wounded", feature={}),
        [("push enemy", 3), ("hit", 5)]
    ]
], [
    dict(name="ogre", type="monster", number=8),
    [
        dict(face="A", life="healthy", feature={"heavy"}),
        [("hit", 4), ("rotate", None)],
    ],
    [
        dict(face="B", life="healthy", feature={}, reaction="shield", shield="rotate"),
        [("heal", None), ("rotate", None)],
        [("hit", 5), ("rotate", None)]
    ],
    [
        dict(face="C", life="exhausted", feature={}),
        [("pull enemy", 6), ("hit", 1)],
    ],
    [
        dict(face="D", life="wounded", feature={}),
        [("pull enemy", 4), ("hit", 1)]
    ]
], [
    dict(name="ogre", type="monster", number=9),
    [
        dict(face="A", life="healthy", feature={}),
        [("push enemy", 3), ("push enemy", 3), ("rotate", None)]
    ],
    [
        dict(face="B", life="healthy", feature={}, reaction="shield", shield="rotate"),
        [("hit", 5), ("rotate", None)],
    ],
    [
        dict(face="C", life="exhausted", feature={"heavy"}),
        [("hit", 0)],
    ],
    [
        dict(face="D", life="wounded", feature={}),
        [("heal", None), ("heal", None), ("heal", None), ("rotate", None)],
        [("pull ally", 5)]
    ]
], [
    dict(name="ranger", type="hero", number=10),
    [
        dict(face="A", life="healthy", feature={"trap"}),
        [("arrow", 1), ("rotate", None)],
        [("delay ally", 2), ("maneuver", None)]
    ],
    [
        dict(face="B", life="healthy", feature={"trap"}),
        [("quicken enemy", 2), ("maneuver", None), ("rotate", None)],
        [("heal", None)]
    ],
    [
        dict(face="C", life="exhausted", feature={"trap"}),
        [("maneuver", None)],
        [("hit", 1)],
        [("delay", 1)]
    ],
    [
        dict(face="D", life="wounded", feature={"trap"}),
        [("arrow", 2)],
        [("maneuver", None)],
        [("quicken", 1)]
    ]
], [
    dict(name="ranger", type="hero", number=11),
    [
        dict(face="A", life="healthy", reaction="dodge", dodge="rotate"),
        [("arrow", 1), ("rotate", None)],
        [("quicken enemy", 2), ("maneuver", None), ("rotate", None)],
        [("hit", 1), ("rotate", None)]
    ],
    [
        dict(face="B", life="healthy", feature={}),
        [("delay hero", 2)],
        [("quicken enemy", 2)],
        [("maneuver", None), ("maneuver", None)]
    ],
    [
        dict(face="C", life="wounded", feature={}),
        [("hit", 1), ("hit", 1), ("rotate", None)],
        [("quicken enemy", 2), ("maneuver", None)]
    ],
    [
        dict(face="D", life="exhausted", feature={}),
        [("hit", 1), ("maneuver", None), ("delay hero", 2)]
    ]
], [
    dict(name="ranger", type="hero", number=12),
    [
        dict(face="A", life="healthy", feature={}, reaction="dodge", dodge="rotate"),
        [("maneuver", None), ("quicken enemy", 2), ("rotate", None)],
        [("delay", 1), ("rotate", None)]
    ],
    [
        dict(face="B", life="healthy", feature={"trap"}),
        [("arrow", 2)],
        [("delay hero", 2), ("maneuver", None)]
    ],
    [
        dict(face="C", life="wounded", feature={"trap"}),
        [("delay hero", 2), ("arrow", 1)],
        [("maneuver", None)]
    ],
    [
        dict(face="D", life="exhausted", feature={"trap"}),
        [("delay hero", 2), ("quicken enemy", 2)],
        [("maneuver", None), ("hit", 1)]
    ]
], [
    dict(name="ranger", type="hero", number=13),
    [
        dict(face="A", life="healthy", feature={"trap"}),
        [("maneuver", None), ("rotate", None)],
        [("hit", 1)],
        [("delay", 1)]
    ],
    [
        dict(face="B", life="healthy", feature={}),
        [("arrow", 1), ("rotate", None)],
        [("maneuver", None), ("hit", 1), ("rotate", None)],
        [("quicken enemy", 2)]
    ],
    [
        dict(face="C", life="exhausted", feature={"trap"}),
        [("arrow", 1)],
        [("maneuver", None)],
        [("delay", 1)]
    ],
    [
        dict(face="D", life="wounded", feature={}),
        [("arrow", 1)],
        [("quicken enemy", 2), ("maneuver", None)]
    ]
], [
    dict(name="ranger", type="hero", number=14),
    [
        dict(face="A", life="healthy", feature={}, reaction="dodge", dodge="rotate"),
        [("arrow", 1), ("rotate", None)],
        [("quicken enemy", 2), ("rotate", None)]
    ],
    [
        dict(face="B", life="healthy", feature={}),
        [("arrow", 2)],
        [("delay hero", 2), ("maneuver", None)],
        [("heal", None)]
    ],
    [
        dict(face="C", life="wounded", feature={"trap"}),
        [("delay hero", 2), ("quicken enemy", 2)],
        [("maneuver", None), ("hit", 1)]
    ],
    [
        dict(face="D", life="exhausted", feature={}),
        [("arrow", 1)],
        [("delay hero", 2)],
        [("heal", None)]
    ]
], [
    dict(name="vampire", type="monster", number=15),
    [
        dict(face="A", life="healthy", feature={}),
        [],
        []
    ],
    [
        dict(face="B", life="healthy", feature={}),
        [],
        [],
        []
    ],
    [
        dict(face="C", life="wounded", feature={}),
        [],
        []
    ],
    [
        dict(face="D", life="exhausted", feature={}),
        [],
        [],
        []
    ]
], [
    dict(name="vampire", type="monster", number=16),
    [
        dict(face="A", life="healthy", feature={}),
        [],
        []
    ],
    [
        dict(face="B", life="healthy", feature={}),
        [],
        [],
        []
    ],
    [
        dict(face="C", life="wounded", feature={}),
        [],
        []
    ],
    [
        dict(face="D", life="exhausted", feature={}),
        [],
        [],
        []
    ]
], [
    dict(name="vampire", type="monster", number=17),
    [
        dict(face="A", life="healthy", feature={}),
        [],
        []
    ],
    [
        dict(face="B", life="healthy", feature={}),
        [],
        [],
        []
    ],
    [
        dict(face="C", life="wounded", feature={}),
        [],
        []
    ],
    [
        dict(face="D", life="exhausted", feature={}),
        [],
        [],
        []
    ]
], [
    dict(name="vampire", type="monster", number=18),
    [
        dict(face="A", life="healthy", feature={}),
        [],
        []
    ],
    [
        dict(face="B", life="healthy", feature={}),
        [],
        [],
        []
    ],
    [
        dict(face="C", life="wounded", feature={}),
        [],
        []
    ],
    [
        dict(face="D", life="exhausted", feature={}),
        [],
        [],
        []
    ]
], [
    dict(name="pyromancer", type="hero", number=19),
    [
        dict(face="A", life="healthy", feature={}),
        [],
        []
    ],
    [
        dict(face="B", life="healthy", feature={}),
        [],
        [],
        []
    ],
    [
        dict(face="C", life="wounded", feature={}),
        [],
        []
    ],
    [
        dict(face="D", life="exhausted", feature={}),
        [],
        [],
        []
    ]
], [
    dict(name="pyromancer", type="hero", number=20),
    [
        dict(face="A", life="healthy", feature={}),
        [],
        []
    ],
    [
        dict(face="B", life="healthy", feature={}),
        [],
        [],
        []
    ],
    [
        dict(face="C", life="wounded", feature={}),
        [],
        []
    ],
    [
        dict(face="D", life="exhausted", feature={}),
        [],
        [],
        []
    ]
], [
    dict(name="pyromancer", type="hero", number=21),
    [
        dict(face="A", life="healthy", feature={}),
        [],
        []
    ],
    [
        dict(face="B", life="healthy", feature={}),
        [],
        [],
        []
    ],
    [
        dict(face="C", life="wounded", feature={}),
        [],
        []
    ],
    [
        dict(face="D", life="exhausted", feature={}),
        [],
        [],
        []
    ]
], [
    dict(name="pyromancer", type="hero", number=22),
    [
        dict(face="A", life="healthy", feature={}),
        [],
        []
    ],
    [
        dict(face="B", life="healthy", feature={}),
        [],
        [],
        []
    ],
    [
        dict(face="C", life="wounded", feature={}),
        [],
        []
    ],
    [
        dict(face="D", life="exhausted", feature={}),
        [],
        [],
        []
    ]
], [
    dict(name="pyromancer", type="hero", number=23),
    [
        dict(face="A", life="healthy", feature={}),
        [],
        []
    ],
    [
        dict(face="B", life="healthy", feature={}),
        [],
        [],
        []
    ],
    [
        dict(face="C", life="wounded", feature={}),
        [],
        []
    ],
    [
        dict(face="D", life="exhausted", feature={}),
        [],
        [],
        []
    ]
], [
    dict(name="venomous", type="monster", number=24),
    [
        dict(face="A", life="healthy", feature={}),
        [],
        []
    ],
    [
        dict(face="B", life="healthy", feature={}),
        [],
        [],
        []
    ],
    [
        dict(face="C", life="wounded", feature={}),
        [],
        []
    ],
    [
        dict(face="D", life="exhausted", feature={}),
        [],
        [],
        []
    ]
], [
    dict(name="venomous", type="monster", number=25),
    [
        dict(face="A", life="healthy", feature={}),
        [],
        []
    ],
    [
        dict(face="B", life="healthy", feature={}),
        [],
        [],
        []
    ],
    [
        dict(face="C", life="wounded", feature={}),
        [],
        []
    ],
    [
        dict(face="D", life="exhausted", feature={}),
        [],
        [],
        []
    ]
], [
    dict(name="venomous", type="monster", number=26),
    [
        dict(face="A", life="healthy", feature={}),
        [],
        []
    ],
    [
        dict(face="B", life="healthy", feature={}),
        [],
        [],
        []
    ],
    [
        dict(face="C", life="wounded", feature={}),
        [],
        []
    ],
    [
        dict(face="D", life="exhausted", feature={}),
        [],
        [],
        []
    ]
], [
    dict(name="venomous", type="monster", number=27),
    [
        dict(face="A", life="healthy", feature={}),
        [],
        []
    ],
    [
        dict(face="B", life="healthy", feature={}),
        [],
        [],
        []
    ],
    [
        dict(face="C", life="wounded", feature={}),
        [],
        []
    ],
    [
        dict(face="D", life="exhausted", feature={}),
        [],
        [],
        []
    ]
]]

# pyromancer, vampire, venomous

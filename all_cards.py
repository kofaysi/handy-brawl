"""
List of all cards ordered by the number of the cards
"""
cards = [[  # card 1
    dict(name="warrior", type="hero", number=1),
    [
        dict(face="A", life="healthy", feature="light"),  # first one is always passive
        [("hit", 2)],
        [("delay", 2), ("rotate", None)]
    ],
    [
        dict(face="B", life="healthy", reaction="shield", shield="rotate"),
        [("delay", 1), ("hit", 2)],
        [("delay", 2)]
    ],
    [
        dict(face="C", life="exhausted"),
        [("hit", 2)],
        [("delay", 1)]
    ],
    [
        dict(face="D", life="wounded"),
        [("hit", 4)],
        [("quicken", 2)]
    ]
], [
    dict(name="warrior", type="hero", number=2),
    [
        dict(face="A", life="healthy"),
        [("hit", 2), ("rotate", None)],
        [("delay", 2)]
    ],
    [
        dict(face="B", life="healthy", reaction="shield", shield="rotate"),
        [("heal", None), ("rotate", None)],
        [("quicken", 2)]
    ],
    [
        dict(face="C", life="exhausted"),
        [("quicken", 2)],
        [("delay", 2)]

    ],
    [
        dict(face="D", life="wounded"),
        [("heal", None), ("rotate", None)],
        [("delay", 3)]
    ]
], [
    dict(name="warrior", type="hero", number=3),
    [
        dict(face="A", life="healthy"),
        [("delay", 2), ("rotate", None)],
        [("quicken", 2), ("rotate", None)]
    ],
    [
        dict(face="B", life="healthy"),
        [("hit", 4), ("hit", 4), ("rotate", None)]
    ],
    [
        dict(face="C", life="exhausted"),
        [("quicken", 2)],
        [("delay", 2)]
    ],
    [
        dict(face="D", life="wounded"),
        [("hit", 4)],
        [("delay", 1)]
    ]
], [
    dict(name="warrior", type="hero", number=4),
    [
        dict(face="A", life="healthy", reaction="shield", shield="rotate"),
        [("hit", 4)],
        [("quicken", 2)]
    ],
    [
        dict(face="B", life="healthy"),
        [("hit", 2)],
        [("delay", 1), ("quicken", 1), ("rotate", None)]
    ],
    [
        dict(face="C", life="wounded"),
        [("hit", 4)],
        [("quicken", 1)]
    ],
    [
        dict(face="D", life="exhausted"),
        [("hit", 2)],
        [("heal", None)]
    ]
], [
    dict(name="warrior", type="hero", number=5),
    [
        dict(face="A", life="healthy", reaction="shield", shield="rotate"),
        [("quicken", 2), ("hit", 2)]
    ],
    [
        dict(face="B", life="healthy"),
        [("hit", 2), ("rotate", None)],
        [("quicken", 2), ("rotate", None)]
    ],
    [
        dict(face="C", life="wounded"),
        [("delay", 3), ("hit", 2), ("hit", 2), ("rotate", None)],
        [("quicken", 2)]
    ],
    [
        dict(face="D", life="exhausted"),
        [("hit", 4)],
        [("quicken", 1)]
    ]
], [  # card 6
    dict(name="ogre", type="monster", number=6),
    [
        dict(face="A", life="healthy"),  # first one is always passive
        [("pull enemy", 5), ("hit", 1), ("rotate", None)]
    ],
    [
        dict(face="B", life="healthy", reaction="shield", shield="rotate"),
        [("hit", 4), ("push enemy", 3)],
    ],
    [
        dict(face="C", life="exhausted"),
        [("hit", 5)],
    ],
    [
        dict(face="D", life="wounded", feature="heavy", reaction="shield"),
        [("hit", 0), ("hit", 0), ("rotate", None)],
    ]
], [
    dict(name="ogre", type="monster", number=7),
    [
        dict(face="A", life="healthy", feature="heavy"),
        [("hit", 4), ("rotate", None)],
    ],
    [
        dict(face="B", life="healthy", reaction="shield", shield="rotate"),
        [("heal", None), ("rotate", None)],
        [("hit", 7), ("rotate", None)]
    ],
    [
        dict(face="C", life="exhausted"),
        [("hit", 5), ("pull self", 3)],
    ],
    [
        dict(face="D", life="wounded"),
        [("push enemy", 3), ("hit", 5)]
    ]
], [
    dict(name="ogre", type="monster", number=8),
    [
        dict(face="A", life="healthy", feature="heavy"),
        [("hit", 4), ("rotate", None)],
    ],
    [
        dict(face="B", life="healthy", reaction="shield", shield="rotate"),
        [("heal", None), ("rotate", None)],
        [("hit", 5), ("rotate", None)]
    ],
    [
        dict(face="C", life="exhausted"),
        [("pull enemy", 6), ("hit", 1)],
    ],
    [
        dict(face="D", life="wounded"),
        [("pull enemy", 4), ("hit", 1)]
    ]
], [
    dict(name="ogre", type="monster", number=9),
    [
        dict(face="A", life="healthy"),  # first one is always passive
        [("push enemy", 3), ("push enemy", 3), ("rotate", None)]
    ],
    [
        dict(face="B", life="healthy", reaction="shield", shield="rotate"),
        [("hit", 5), ("rotate", None)],
    ],
    [
        dict(face="C", life="exhausted", feature="heavy"),
        [("hit", 0)],
    ],
    [
        dict(face="D", life="wounded"),
        [("heal", None), ("heal", None), ("heal", None), ("rotate", None)],
        [("pull", 5)]
    ]
], [
    dict(name="ranger", type="hero", number=10),
    [
        dict(face="A", life="healthy", trap=True),  # first one is always passive
        [("arrow", None), ("rotate", None)],
        [("delay self", 2), ("maneuver", None)]
    ],
    [
        dict(face="B", life="healthy", trap=True),
        [("quicken enemy", 2), ("maneuver", None), ("rotate", None)],
        [("heal", None)]
    ],
    [
        dict(face="C", life="exhausted", trap=True),
        [("maneuver", None)],
        [("hit", 1)],
        [("delay", 1)]
    ],
    [
        dict(face="D", life="wounded", trap=True),
        [("arrow", "double")],
        [("maneuver", None)],
        [("quicken", 1)]
    ]
], [
    dict(name="ranger", type="hero", number=11),
    [
        dict(face="A", life="healthy", dodge="rotate"),  # first one is always passive
        [("arrow", None), ("rotate", None)],
        [("quicken enemy", 2), ("maneuver", None), ("rotate", None)],
        [("hit", 1), ("rotate", None)]
    ],
    [
        dict(face="B", life="healthy"),
        [("delay hero", 2)],
        [("quicken enemy", 2)],
        [("maneuver", None), ("maneuver", None)]
    ],
    [
        dict(face="C", life="wounded"),
        [("hit", 1), ("hit", 1), ("rotate", None)],
        [("quicken enemy", 2), ("maneuver", None)]
    ],
    [
        dict(face="D", life="exhausted"),
        [("hit", 1), ("maneuver", None), ("delay hero", 2)]
    ]
], [
    dict(name="ranger", type="hero", number=12),
    [
        dict(face="A", life="healthy", dodge="rotate"),  # first one is always passive
        [("maneuver", None), ("quicken enemy", 2), ("rotate", None)],
        [("delay", 1), ("rotate", None)]
    ],
    [
        dict(face="B", life="healthy", trap=True),
        [("arrow", "double")],
        [("delay hero", 2), ("maneuver", None)]
    ],
    [
        dict(face="C", life="wounded", trap=True),
        [("delay hero", 2), ("arrow", None)],
        [("maneuver", None)]
    ],
    [
        dict(face="D", life="exhausted", trap=True),
        [("delay hero", 2), ("quicken enemy", 2)],
        [("maneuver", None), ("hit", 1)]
    ]
], [
    dict(name="ranger", type="hero", number=13),
    [
        dict(face="A", life="healthy", trap=True),  # first one is always passive
        [("maneuver", None), ("rotate", None)],
        [("hit", 1)],
        [("delay", 1)]
    ],
    [
        dict(face="B", life="healthy"),
        [("arrow", None), ("rotate", None)],
        [("maneuver", None), ("hit", 1), ("rotate", None)],
        [("quicken enemy", 2)]
    ],
    [
        dict(face="C", life="exhausted", trap=True),
        [("arrow", None)],
        [("maneuver", None)],
        [("delay", 1)]
    ],
    [
        dict(face="D", life="wounded"),
        [("arrow", None)],
        [("quicken enemy", 2), ("maneuver", None)]
    ]
], [
    dict(name="ranger", type="hero", number=14),
    [
        dict(face="A", life="healthy", dodge="rotate"),  # first one is always passive
        [("arrow", None), ("rotate", None)],
        [("quicken enemy", 2), ("rotate", None)]
    ],
    [
        dict(face="B", life="healthy"),
        [("arrow", "double")],
        [("delay hero", 2), ("maneuver", None)],
        [("heal", None)]
    ],
    [
        dict(face="C", life="wounded", trap=True),
        [("delay hero", 2), ("quicken enemy", 2)],
        [("maneuver", None), ("hit", 1)]
    ],
    [
        dict(face="D", life="exhausted"),
        [("arrow", None)],
        [("delay hero", 2)],
        [("heal", None)]
    ]
]]

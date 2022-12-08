paladin = [[  # card 1
    dict(name="paladin", type="hero", number=1),
    [
        dict(face="A", health=1, weight="light"),  # first one is always passive
        [("attack", 2)],
        [("push", 2), ("rotate_vertical", 0)]
    ],
    [
        dict(face="B", health=1, shield="rotate_vertical"),
        [("push", 1), ("attack", 2)],
        [("push", 2)]
    ],
    [
        dict(face="C", health=0.5),
        [("attack", 5)],
        [("push", 1)]
    ],
    [
        dict(face="D", health=0),
        [("attack", 2)],
        [("push", 2)]
    ]
], [
    [
        ["paladin", 2]
    ],
    [
        {"face": "A", "health": 1},
        [("attack", 2), ("rotate", 0)],
        [("push", 2)]
    ],
    [
        {"face": "B", "health": 1, "shield": "rotate"},
        [("heal", 0), ("rotate", 0)],
        [("push", 2)]
    ],
    [
        {"face": "C", "health": 0.5},
        [("heal", 0), ("rotate", 0)],
        [("push", 2)]
    ],
    [
        {"face": "D", "health": 0},
        [("pull", 2)],
        [("push", 2)]
    ]
], [
    [
        ["paladin", 3]
    ],
    [
        {"face": "A", "health": 1},
        [("push", 2), ("rotate", 0)],
        [("pull", 2), ("rotate", 0)]
    ],
    [
        {"face": "B", "health": 1},
        [("attack", 4), ("attack", 4), ("rotate", 0)]
    ],
    [
        {"face": "C", "health": 0.5},
        [("attack", 5)],
        [("push", 1)]
    ],
    [
        {"face": "D", "health": 0},
        [("pull", 2)],
        [("push", 2)]
    ]
], [
    [
        ["paladin", 4]
    ],
    [
        {"face": "A", "health": 1, "shield": "rotate"},
        [("attack", 4)],
        [("push", 2)]
    ],
    [
        {"face": "B", "health": 1},
        [("attack", 2)],
        [("push", 2), ("pull", 2), ("rotate", 0)]
    ],
    [
        {"face": "C", "health": 0.5},
        [("attack", 5)],
        [("pull", 2)]
    ],
    [
        {"face": "D", "health": 0},
        [("attack", 4)],
        [("heal", 0)]
    ]
], [
    [
        ["paladin", 5]
    ],
    [
        {"face": "A", "health": 1, "shield": "rotate"},
        [("pull", 2), ("attack", 2)]
    ],
    [
        {"face": "B", "health": 1},
        [("attack", 2), ("rotate", 0)],
        [("pull", 2), ("rotate", 0)]
    ],
    [
        {"face": "C", "health": 0.5},
        [("push", 3), ("attack", 2), ("attack", 2), ("rotate", 0)],
        [("pull", 2)]
    ],
    [
        {"face": "D", "health": 0},
        [("attack", 3)],
        [("pull", 2)]
    ]
]]

archer = [[
    [
        ["archer", 10]
    ],
    [
        {"face": "A", "health": 1, "trap": True},  # first one is always passive
        [("arch", 0), ("rotate", 0)],
        [("push-hero", 2), ("rotate-other", 0)]
    ],
    [
        {"face": "B", "health": 1, "trap": True},
        [("pull-enemy", 2), ("rotate-other", 0), ("rotate", 0)],
        [("heal", 0)]
    ],
    [
        {"face": "C", "health": 0.5, "trap": True},
        [("arch-2-different", 0)],
        [("rotate-other", 0)],
        [("pull", 1)]
    ],
    [
        {"face": "D", "health": 0, "trap": True},
        [("rotate-other", 0)],
        [("attack", 1)],
        [("push", 1)]
    ]
], [
    [
        ["archer", 11]
    ],
    [
        {"face": "A", "health": 1, "run": "rotate"},  # first one is always passive
        [("arch", 0), ("rotate", 0)],
        [("pull-enemy", 2), ("rotate-other", 0), ("rotate", 0)],
        [("attack", 1), ("rotate", 0)]
    ],
    [
        {"face": "B", "health": 1},
        [("push-hero", 2)],
        [("pull-enemy", 2)],
        [("rotate-other", 0), ("rotate-other", 0)]
    ],
    [
        {"face": "C", "health": 0.5},
        [("attack", 1), ("attack", 1), ("rotate", 0)],
        [("pull-enemy", 1), ("rotate-other", 0)]
    ],
    [
        {"face": "D", "health": 0},
        [("attack", 1), ("rotate-other", 0), ("push-hero", 2)]
    ]
], [
    [
        ["archer", 12]
    ],
    [
        {"face": "A", "health": 1, "run": "rotate"},  # first one is always passive
        [("rotate-other", 0), ("pull-enemy", 2), ("rotate", 0)],
        [("push", 1), ("rotate", 0)]
    ],
    [
        {"face": "B", "health": 1, "trap": True},
        [("arch-2-different", 0)],
        [("push-hero", 2), ("rotate-other", 0)]
    ],
    [
        {"face": "C", "health": 0.5, "trap": True},
        [("push-hero", 2), ("arch", 0)],
        [("rotate-other", 0)]
    ],
    [
        {"face": "D", "health": 0},
        [("push-hero", 2), ("pull-enemy", 2)],
        [("rotate-other", 0), ("attack", 1)]
    ]
], [
    [
        ["archer", 13]
    ],
    [
        {"face": "A", "health": 1, "trap": True},  # first one is always passive
        [("rotate-other", 0), ("rotate", 0)],
        [("attack", 1)],
        [("push", 1)]
    ],
    [
        {"face": "B", "health": 1},
        [("arch", 0), ("rotate", 0)],
        [("rotate-other", 0), ("attack", 1), ("rotate", 0)],
        [("pull-enemy", 2)]
    ],
    [
        {"face": "C", "health": 0.5},
        [("arch", 0)],
        [("pull-enemy", 2), ("rotate-other", 0)]
    ],
    [
        {"face": "D", "health": 0, "trap": True},
        [("arch", 0)],
        [("rotate-other", 0)],
        [("push", 1)]
    ]
], [
    [
        ["archer", 14]
    ],
    [
        {"face": "A", "health": 1, "run": "rotate"},  # first one is always passive
        [("arch", 0), ("rotate", 0)],
        [("pull-enemy", 1), ("rotate", 0)]
    ],
    [
        {"face": "B", "health": 1},
        [("arch-2-different", 0)],
        [("push-hero", 2), ("rotate-other", 0)],
        [("heal", 0)]
    ],
    [
        {"face": "C", "health": 0.5, "trap": True},
        [("push-hero", 2), ("pull-enemy", 2)],
        [("rotate-other", 0), ("attack", 1)]
    ],
    [
        {"face": "D", "health": 0},
        [("arch", 0)],
        [("push-hero", 2)],
        [("heal", 0)]
    ]
]]

paladin = [[  # card 1
    [
        ["paladin", 1]
    ],
    [
        [("health", 1)],  # first one is always passive
        [("attack", 2)],
        [("push", 2), ("rotate_vertical", 0)]
    ],
    [
        [("health", 1), ("shield", 2), ("rotate_vertical", 0)],
        [("push", 1), ("attack", 2)],
        [("push", 2)]
    ],
    [
        [("health", 0.5)],
        [("attack", 5)],
        [("push", 1)]
    ],
    [
        [("health", 0)],
        [("attack", 2)],
        [("push", 2)]
    ]
], [
    [
        ["paladin", 2]
    ],
    [
        [("health", 1)],
        [("attack", 2), ("rotate", 0)],
        [("push", 2)]
    ],
    [
        [("health", 1), ("shield", 0), ("rotate", 0)],
        [("heal", 0), ("rotate", 0)],
        [("push", 2)]
    ],
    [
        [("health", 0.5)],
        [("heal", 0), ("rotate", 0)],
        [("push", 2)]
    ],
    [
        [("health", 0)],
        [("pull", 2)],
        [("push", 2)]
    ]
], [
    [
        ["paladin", 3]
    ],
    [
        [("health", 1)],
        [("push", 2), ("rotate", 0)],
        [("pull", 2), ("rotate", 0)]
    ],
    [
        [("health", 1)],
        [("attack", 4), ("attack", 4), ("rotate", 0)]
    ],
    [
        [("health", 0.5)],
        [("attack", 5)],
        [("push", 1)]
    ],
    [
        [("health", 0)],
        [("pull", 2)],
        [("push", 2)]
    ]
], [
    [
        ["paladin", 4]
    ],
    [
        [("health", 1), ("shield", 0), ("rotate", 0)],
        [("attack", 4)],
        [("push", 2)]
    ],
    [
        [("health", 1)],
        [("attack", 2)],
        [("push", 2), ("pull", 2), ("rotate", 0)]
    ],
    [
        [("health", 0.5)],
        [("attack", 5)],
        [("pull", 2)]
    ],
    [
        [("health", 0)],
        [("attack", 4)],
        [("heal", 0)]
    ]
], [
    [
        ["paladin", 5]
    ],
    [
        [("health", 1), ("shield", 0), ("rotate", 0)],
        [("pull", 2), ("attack", 2)]
    ],
    [
        [("health", 1)],
        [("attack", 2), ("rotate", 0)],
        [("pull", 2), ("rotate", 0)]
    ],
    [
        [("health", 0.5)],
        [("push", 3), ("attack", 2), ("attack", 2), ("rotate", 0)],
        [("pull", 2)]
    ],
    [
        [("health", 0)],
        [("attack", 3)],
        [("pull", 2)]
    ]
]]

archer = [[
    [
        ["archer", 10]
    ],
    [
        [("health", 1), ("trap", 0)],  # first one is always passive
        [("arch", 0), ("rotate", 0)],
        [("push-hero", 2), ("rotate-other", 0)]
    ],
    [
        [("health", 1), ("trap", 0)],
        [("pull-enemy", 2), ("rotate-other", 0), ("rotate", 0)],
        [("heal", 0)]
    ],
    [
        [("health", 0.5), ("trap", 0)],
        [("arch-2-different", 0)],
        [("rotate-other", 0)],
        [("pull", 1)]
    ],
    [
        [("health", 0), ("trap", 0)],
        [("rotate-other", 0)],
        [("attack", 1)],
        [("push", 1)]
    ]
], [
    [
        ["archer", 11]
    ],
    [
        [("health", 1), ("run", 0), ("rotate", 0)],  # first one is always passive
        [("arch", 0), ("rotate", 0)],
        [("pull-enemy", 2), ("rotate-other", 0), ("rotate", 0)],
        [("attack", 1), ("rotate", 0)]
    ],
    [
        [("health", 1)],
        [("push-hero", 2)],
        [("pull-enemy", 2)],
        [("rotate-other", 0), ("rotate-other", 0)]
    ],
    [
        [("health", 0.5)],
        [("attack", 1), ("attack", 1), ("rotate", 0)],
        [("pull-enemy", 1), ("rotate-other", 0)]
    ],
    [
        [("health", 0)],
        [("attack", 1), ("rotate-other", 0), ("push-hero", 2)]
    ]
], [
    [
        ["archer", 12]
    ],
    [
        [("health", 1), ("run", 0), ("rotate", 0)],  # first one is always passive
        [("rotate-other", 0), ("pull-enemy", 2), ("rotate", 0)],
        [("push", 1), ("rotate", 0)]
    ],
    [
        [("health", 1), ("trap", 0)],
        [("arch-2-different", 0)],
        [("push-hero", 2), ("rotate-other", 0)]
    ],
    [
        [("health", 0.5), ("trap", 0)],
        [("push-hero", 2), ("arch", 0)],
        [("rotate-other", 0)]
    ],
    [
        [("health", 0)],
        [("push-hero", 2), ("pull-enemy", 2)],
        [("rotate-other", 0), ("attack", 1)]
    ]
], [
    [
        ["archer", 13]
    ],
    [
        [("health", 1), ("trap", 0)],  # first one is always passive
        [("rotate-other", 0), ("rotate", 0)],
        [("attack", 1)],
        [("push", 1)]
    ],
    [
        [("health", 1)],
        [("arch", 0), ("rotate", 0)],
        [("rotate-other", 0), ("attack", 1), ("rotate", 0)],
        [("pull-enemy", 2)]
    ],
    [
        [("health", 0.5)],
        [("arch", 0)],
        [("pull-enemy", 2), ("rotate-other", 0)]
    ],
    [
        [("health", 0), ("trap", 0)],
        [("arch", 0)],
        [("rotate-other", 0)],
        [("push", 1)]
    ]
], [
    [
        ["archer", 14]
    ],
    [
        [("health", 1), ("run", 0), ("rotate", 0)],  # first one is always passive
        [("arch", 0), ("rotate", 0)],
        [("pull-enemy", 1), ("rotate", 0)]
    ],
    [
        [("health", 1)],
        [("arch-2-different", 0)],
        [("push-hero", 2), ("rotate-other", 0)],
        [("heal", 0)]
    ],
    [
        [("health", 0.5), ("trap", 0)],
        [("push-hero", 2), ("pull-enemy", 2)],
        [("rotate-other", 0), ("attack", 1)]
    ],
    [
        [("health", 0)],
        [("arch", 0)],
        [("push-hero", 2)],
        [("heal", 0)]
    ]
]]

# gt_st_booster/questions.py
# Practice question bank for all ASVAB subtests that contribute to GT and ST composites.
# Each question is a dict: { "q": str, "choices": [A,B,C,D], "answer": "A"|"B"|"C"|"D", "explanation": str }

# ---------------------------------------------------------------------------
# AR – Arithmetic Reasoning  (feeds GT)
# ---------------------------------------------------------------------------
AR_QUESTIONS = [
    {
        "q": "A soldier runs 3 miles in 24 minutes. How many minutes does it take to run 1 mile?",
        "choices": ["A) 6", "B) 7", "C) 8", "D) 9"],
        "answer": "C",
        "explanation": "24 ÷ 3 = 8 minutes per mile."
    },
    {
        "q": "A convoy travels 280 miles on 14 gallons of fuel. How many miles per gallon does the vehicle get?",
        "choices": ["A) 18", "B) 20", "C) 22", "D) 25"],
        "answer": "B",
        "explanation": "280 ÷ 14 = 20 mpg."
    },
    {
        "q": "A supply room has 5 boxes, each containing 24 MREs. How many MREs are there in total?",
        "choices": ["A) 100", "B) 110", "C) 120", "D) 130"],
        "answer": "C",
        "explanation": "5 × 24 = 120 MREs."
    },
    {
        "q": "If a soldier earns $2,400 per month and spends 35% on rent, how much does he spend on rent?",
        "choices": ["A) $720", "B) $800", "C) $840", "D) $900"],
        "answer": "C",
        "explanation": "2400 × 0.35 = $840."
    },
    {
        "q": "A tank holds 50 gallons and is currently 40% full. How many gallons does it need to be filled completely?",
        "choices": ["A) 20", "B) 25", "C) 30", "D) 35"],
        "answer": "C",
        "explanation": "50 × 0.40 = 20 gallons already in. 50 − 20 = 30 gallons needed."
    },
    {
        "q": "A unit has 120 soldiers. If 15% are on leave, how many are present for duty?",
        "choices": ["A) 96", "B) 100", "C) 102", "D) 108"],
        "answer": "C",
        "explanation": "120 × 0.15 = 18 on leave. 120 − 18 = 102 present."
    },
    {
        "q": "A soldier drives at 60 mph for 2.5 hours. How many miles did he travel?",
        "choices": ["A) 120", "B) 140", "C) 150", "D) 160"],
        "answer": "C",
        "explanation": "60 × 2.5 = 150 miles."
    },
    {
        "q": "If a rifle weighs 8.5 lbs and a soldier carries 4 of them, what is the total weight?",
        "choices": ["A) 32 lbs", "B) 34 lbs", "C) 36 lbs", "D) 38 lbs"],
        "answer": "B",
        "explanation": "8.5 × 4 = 34 lbs."
    },
    {
        "q": "A squad of 9 soldiers shares 63 pounds of equipment equally. How many pounds does each carry?",
        "choices": ["A) 6", "B) 7", "C) 8", "D) 9"],
        "answer": "B",
        "explanation": "63 ÷ 9 = 7 pounds each."
    },
    {
        "q": "A soldier saves $150 per month. How many months will it take to save $1,800?",
        "choices": ["A) 10", "B) 11", "C) 12", "D) 13"],
        "answer": "C",
        "explanation": "1800 ÷ 150 = 12 months."
    },
]

# ---------------------------------------------------------------------------
# VE – Verbal Expression: Word Knowledge (WK)  (feeds GT)
# ---------------------------------------------------------------------------
WK_QUESTIONS = [
    {
        "q": "AUDACIOUS most nearly means:",
        "choices": ["A) Timid", "B) Bold", "C) Graceful", "D) Quiet"],
        "answer": "B",
        "explanation": "Audacious means showing a willingness to take bold risks."
    },
    {
        "q": "DILIGENT most nearly means:",
        "choices": ["A) Lazy", "B) Careless", "C) Hardworking", "D) Reckless"],
        "answer": "C",
        "explanation": "Diligent means having or showing care and conscientiousness in one's work."
    },
    {
        "q": "MUNDANE most nearly means:",
        "choices": ["A) Extraordinary", "B) Ordinary", "C) Dangerous", "D) Spiritual"],
        "answer": "B",
        "explanation": "Mundane means lacking interest or excitement; dull / ordinary."
    },
    {
        "q": "TACITURN most nearly means:",
        "choices": ["A) Talkative", "B) Reserved", "C) Angry", "D) Joyful"],
        "answer": "B",
        "explanation": "Taciturn means reserved or uncommunicative in speech."
    },
    {
        "q": "BENEVOLENT most nearly means:",
        "choices": ["A) Hostile", "B) Kind", "C) Greedy", "D) Fearful"],
        "answer": "B",
        "explanation": "Benevolent means well-meaning and kindly."
    },
    {
        "q": "OBSOLETE most nearly means:",
        "choices": ["A) Current", "B) Outdated", "C) Efficient", "D) Modern"],
        "answer": "B",
        "explanation": "Obsolete means no longer in use or no longer useful."
    },
    {
        "q": "TENACIOUS most nearly means:",
        "choices": ["A) Weak", "B) Persistent", "C) Generous", "D) Confused"],
        "answer": "B",
        "explanation": "Tenacious means tending to keep a firm hold; not giving up easily."
    },
    {
        "q": "OMINOUS most nearly means:",
        "choices": ["A) Cheerful", "B) Threatening", "C) Peaceful", "D) Trivial"],
        "answer": "B",
        "explanation": "Ominous means giving the impression that something bad is about to happen."
    },
    {
        "q": "LUCID most nearly means:",
        "choices": ["A) Confusing", "B) Dark", "C) Clear", "D) Hidden"],
        "answer": "C",
        "explanation": "Lucid means expressed clearly and easy to understand."
    },
    {
        "q": "FRUGAL most nearly means:",
        "choices": ["A) Wasteful", "B) Thrifty", "C) Generous", "D) Careless"],
        "answer": "B",
        "explanation": "Frugal means sparing or economical with money or food."
    },
]

# ---------------------------------------------------------------------------
# VE – Verbal Expression: Paragraph Comprehension (PC)  (feeds GT)
# ---------------------------------------------------------------------------
PC_QUESTIONS = [
    {
        "q": (
            "Passage: 'The Army values are Loyalty, Duty, Respect, Selfless Service, Honor, "
            "Integrity, and Personal Courage. Soldiers are expected to live and uphold these "
            "values at all times, both on and off duty.'\n"
            "According to the passage, when are soldiers expected to uphold Army values?"
        ),
        "choices": ["A) Only while in uniform", "B) Only on duty", "C) At all times", "D) Only during training"],
        "answer": "C",
        "explanation": "The passage states 'both on and off duty,' meaning at all times."
    },
    {
        "q": (
            "Passage: 'Dehydration reduces a soldier's physical and cognitive performance. "
            "Even a 2% loss in body weight due to fluid loss can impair strength, endurance, "
            "and decision-making ability.'\n"
            "What is the main point of this passage?"
        ),
        "choices": [
            "A) Soldiers should drink water only during exercise.",
            "B) Losing 2% body weight has no effect.",
            "C) Dehydration negatively impacts soldier performance.",
            "D) Strength is the most important military skill."
        ],
        "answer": "C",
        "explanation": "The passage focuses on how dehydration reduces both physical and cognitive performance."
    },
    {
        "q": (
            "Passage: 'Land navigation is a critical survival skill. Soldiers must be able to "
            "read a map, use a compass, and determine grid coordinates to move efficiently "
            "in unfamiliar terrain.'\n"
            "Which of the following is NOT mentioned as a land navigation skill?"
        ),
        "choices": ["A) Reading a map", "B) Using a compass", "C) Swimming across rivers", "D) Determining grid coordinates"],
        "answer": "C",
        "explanation": "Swimming is not mentioned; map reading, compass use, and grid coordinates are."
    },
    {
        "q": (
            "Passage: 'Maintenance of equipment is a commander's responsibility. Leaders must "
            "ensure vehicles, weapons, and communication devices are fully operational before "
            "any mission.'\n"
            "Who is responsible for equipment maintenance according to the passage?"
        ),
        "choices": ["A) The supply sergeant", "B) The commander", "C) The mechanic", "D) The soldier"],
        "answer": "B",
        "explanation": "The passage explicitly states 'maintenance of equipment is a commander's responsibility.'"
    },
    {
        "q": (
            "Passage: 'Sleep deprivation has been shown to impair judgment, slow reaction times, "
            "and increase the likelihood of accidents. Studies suggest that 7-9 hours of sleep "
            "per night is optimal for peak performance.'\n"
            "According to the passage, how many hours of sleep are optimal?"
        ),
        "choices": ["A) 5-6 hours", "B) 6-7 hours", "C) 7-9 hours", "D) 9-11 hours"],
        "answer": "C",
        "explanation": "The passage states '7-9 hours of sleep per night is optimal for peak performance.'"
    },
]

# ---------------------------------------------------------------------------
# MC – Mechanical Comprehension  (feeds ST)
# ---------------------------------------------------------------------------
MC_QUESTIONS = [
    {
        "q": "If gear A has 10 teeth and gear B has 20 teeth, and gear A turns at 100 RPM, how fast does gear B turn?",
        "choices": ["A) 25 RPM", "B) 50 RPM", "C) 100 RPM", "D) 200 RPM"],
        "answer": "B",
        "explanation": "Gear ratio: A/B = 10/20 = 1/2. Gear B turns at 100 × (10/20) = 50 RPM."
    },
    {
        "q": "A lever has its fulcrum 2 feet from a 100-lb load and 8 feet from the effort side. What effort is needed to lift the load?",
        "choices": ["A) 10 lbs", "B) 25 lbs", "C) 50 lbs", "D) 100 lbs"],
        "answer": "B",
        "explanation": "Load × load arm = Effort × effort arm. 100×2 = E×8. E = 200/8 = 25 lbs."
    },
    {
        "q": "A pulley system with 4 supporting ropes supports a 200-lb load. What is the effort required (ignoring friction)?",
        "choices": ["A) 25 lbs", "B) 40 lbs", "C) 50 lbs", "D) 100 lbs"],
        "answer": "C",
        "explanation": "With 4 rope segments, effort = 200 ÷ 4 = 50 lbs."
    },
    {
        "q": "Water flows through a pipe that narrows from a 4-inch diameter to a 2-inch diameter. What happens to the water speed?",
        "choices": ["A) It stays the same", "B) It slows down", "C) It speeds up", "D) It stops"],
        "answer": "C",
        "explanation": "By continuity, when the pipe narrows the fluid must speed up to maintain flow rate."
    },
    {
        "q": "A screw has 10 threads per inch. How many full rotations are needed to advance the screw 1 inch?",
        "choices": ["A) 1", "B) 5", "C) 10", "D) 20"],
        "answer": "C",
        "explanation": "10 threads per inch means 10 rotations move it 1 inch."
    },
    {
        "q": "Which simple machine is a ramp?",
        "choices": ["A) Lever", "B) Pulley", "C) Inclined plane", "D) Wheel and axle"],
        "answer": "C",
        "explanation": "A ramp is an inclined plane — it reduces the force needed to raise an object by increasing distance."
    },
    {
        "q": "If a wedge is driven 4 inches to split a log that moves apart 1 inch, what is the mechanical advantage?",
        "choices": ["A) 1", "B) 2", "C) 4", "D) 8"],
        "answer": "C",
        "explanation": "MA = distance driven ÷ distance load moved = 4 ÷ 1 = 4."
    },
    {
        "q": "A vehicle's engine produces 300 lb-ft of torque. If the drive wheel radius is 1.5 ft, what force does it apply to the ground?",
        "choices": ["A) 100 lbs", "B) 150 lbs", "C) 200 lbs", "D) 300 lbs"],
        "answer": "C",
        "explanation": "Force = Torque ÷ radius = 300 ÷ 1.5 = 200 lbs."
    },
    {
        "q": "Two objects are at rest on a slope. Object A weighs twice as much as Object B. Which slides down first (same friction coefficient)?",
        "choices": [
            "A) Object A slides first because it is heavier.",
            "B) Object B slides first because it is lighter.",
            "C) They slide at the same time.",
            "D) Neither will slide."
        ],
        "answer": "C",
        "explanation": "With the same friction coefficient, gravitational and friction forces scale equally with mass, so both slide at the same time."
    },
    {
        "q": "A hydraulic jack has an input piston area of 2 sq in and an output piston area of 20 sq in. If you apply 50 lbs of force, what force lifts the car?",
        "choices": ["A) 50 lbs", "B) 100 lbs", "C) 500 lbs", "D) 1000 lbs"],
        "answer": "C",
        "explanation": "Pascal's principle: F_out = F_in × (A_out/A_in) = 50 × (20/2) = 500 lbs."
    },
]

# ---------------------------------------------------------------------------
# GS – General Science  (feeds ST)
# ---------------------------------------------------------------------------
GS_QUESTIONS = [
    {
        "q": "What is the chemical formula for water?",
        "choices": ["A) CO2", "B) NaCl", "C) H2O", "D) O2"],
        "answer": "C",
        "explanation": "Water is composed of 2 hydrogen atoms and 1 oxygen atom: H2O."
    },
    {
        "q": "Which planet is closest to the Sun?",
        "choices": ["A) Venus", "B) Earth", "C) Mars", "D) Mercury"],
        "answer": "D",
        "explanation": "Mercury is the closest planet to the Sun."
    },
    {
        "q": "What is the unit of electrical resistance?",
        "choices": ["A) Volt", "B) Ampere", "C) Ohm", "D) Watt"],
        "answer": "C",
        "explanation": "Resistance is measured in Ohms (Ω)."
    },
    {
        "q": "Which gas makes up most of Earth's atmosphere?",
        "choices": ["A) Oxygen", "B) Carbon dioxide", "C) Hydrogen", "D) Nitrogen"],
        "answer": "D",
        "explanation": "Nitrogen makes up about 78% of Earth's atmosphere."
    },
    {
        "q": "The process by which plants make food using sunlight is called:",
        "choices": ["A) Respiration", "B) Photosynthesis", "C) Fermentation", "D) Digestion"],
        "answer": "B",
        "explanation": "Photosynthesis converts sunlight, CO2, and water into glucose and oxygen."
    },
    {
        "q": "What is Newton's Second Law of Motion?",
        "choices": [
            "A) Objects in motion stay in motion.",
            "B) Every action has an equal and opposite reaction.",
            "C) Force equals mass times acceleration (F = ma).",
            "D) Energy cannot be created or destroyed."
        ],
        "answer": "C",
        "explanation": "Newton's Second Law: F = ma (Force = mass × acceleration)."
    },
    {
        "q": "Which of the following is NOT a state of matter?",
        "choices": ["A) Solid", "B) Liquid", "C) Gas", "D) Energy"],
        "answer": "D",
        "explanation": "The three classic states of matter are solid, liquid, and gas. Energy is not a state of matter."
    },
    {
        "q": "The human body has how many bones?",
        "choices": ["A) 186", "B) 196", "C) 206", "D) 216"],
        "answer": "C",
        "explanation": "The adult human body has 206 bones."
    },
    {
        "q": "What is the speed of light (approximate)?",
        "choices": ["A) 300,000 km/s", "B) 30,000 km/s", "C) 3,000 km/s", "D) 300 km/s"],
        "answer": "A",
        "explanation": "The speed of light in a vacuum is approximately 300,000 km/s (3 × 10^8 m/s)."
    },
    {
        "q": "Which organ produces insulin?",
        "choices": ["A) Liver", "B) Kidney", "C) Pancreas", "D) Stomach"],
        "answer": "C",
        "explanation": "The pancreas produces insulin, which regulates blood glucose levels."
    },
]

# ---------------------------------------------------------------------------
# AS – Assembling Objects  (feeds ST)
# ---------------------------------------------------------------------------
AS_QUESTIONS = [
    {
        "q": "Which of the following best describes the purpose of an Assembling Objects question?",
        "choices": [
            "A) To test your ability to solve math equations.",
            "B) To evaluate spatial reasoning and how parts fit together.",
            "C) To measure reading comprehension.",
            "D) To test knowledge of electronics circuits."
        ],
        "answer": "B",
        "explanation": "AS tests spatial reasoning — how shapes, connectors, and parts combine into a whole object."
    },
    {
        "q": "A diagram shows a line connecting point A on one shape to point B on another. Which answer shows those two shapes connected at those exact points?",
        "choices": [
            "A) Both shapes are separate with no connection.",
            "B) The shapes are connected at random points.",
            "C) The shapes are connected at the labeled points A and B.",
            "D) The shapes overlap completely."
        ],
        "answer": "C",
        "explanation": "In connector-type AS problems, the line always shows exactly where the two shapes must join."
    },
    {
        "q": "You see four shapes: a circle, a square, a triangle, and a pentagon. Which combined silhouette could they form if arranged without overlap?",
        "choices": [
            "A) A shape smaller than any individual piece.",
            "B) Any shape formed by placing all four adjacent to each other.",
            "C) Only a rectangle.",
            "D) Only a circle."
        ],
        "answer": "B",
        "explanation": "Combined without overlap, the pieces can form various shapes depending on arrangement."
    },
    {
        "q": "In an AS puzzle, a triangle is reflected horizontally. What does the resulting shape look like?",
        "choices": [
            "A) The triangle is upside down.",
            "B) The triangle is a mirror image left-to-right.",
            "C) The triangle is rotated 90 degrees.",
            "D) The triangle is enlarged."
        ],
        "answer": "B",
        "explanation": "A horizontal reflection creates a left-to-right mirror image of the original shape."
    },
    {
        "q": "When solving spatial rotation problems, the best strategy is to:",
        "choices": [
            "A) Guess quickly without analyzing.",
            "B) Focus only on the largest shape.",
            "C) Track a unique feature of the shape as it rotates.",
            "D) Assume all shapes stay in the same orientation."
        ],
        "answer": "C",
        "explanation": "Tracking a unique feature (e.g., a notch, dot, or corner) helps you follow the shape through rotation accurately."
    },
    {
        "q": "Two identical right triangles are placed with their hypotenuses touching. What shape do they form?",
        "choices": ["A) A circle", "B) A rectangle", "C) A pentagon", "D) A hexagon"],
        "answer": "B",
        "explanation": "Two right triangles placed hypotenuse-to-hypotenuse form a rectangle."
    },
    {
        "q": "A shape is rotated 180 degrees. What is true about its appearance?",
        "choices": [
            "A) It looks exactly the same as the original.",
            "B) It is flipped both vertically and horizontally.",
            "C) It is only flipped vertically.",
            "D) It disappears."
        ],
        "answer": "B",
        "explanation": "A 180-degree rotation is equivalent to flipping the shape both up-down and left-right."
    },
    {
        "q": "In a connector problem, point A is at the top of a circle and point B is at the left corner of a triangle. The connected figure shows them joined at:",
        "choices": [
            "A) The bottom of the circle and right corner of the triangle.",
            "B) The center of both shapes.",
            "C) The top of the circle and the left corner of the triangle.",
            "D) Random points."
        ],
        "answer": "C",
        "explanation": "Connector problems always join the shapes at the exact labeled points shown in the diagram."
    },
    {
        "q": "Which strategy best improves AS scores?",
        "choices": [
            "A) Memorizing math formulas.",
            "B) Practicing mental rotation of 2D and 3D shapes daily.",
            "C) Studying vocabulary words.",
            "D) Reviewing grammar rules."
        ],
        "answer": "B",
        "explanation": "AS is purely a spatial reasoning test; regular practice with mental rotation of shapes directly improves performance."
    },
    {
        "q": "A flat cross-shaped net is folded. Which 3D shape does it form?",
        "choices": ["A) A pyramid", "B) A sphere", "C) A cube", "D) A cylinder"],
        "answer": "C",
        "explanation": "A cross-shaped net with 6 squares folds into a cube."
    },
]

# ---------------------------------------------------------------------------
# EI – Electronics Information  (feeds ST)
# ---------------------------------------------------------------------------
EI_QUESTIONS = [
    {
        "q": "Ohm's Law states that voltage equals:",
        "choices": ["A) Current ÷ Resistance", "B) Current × Resistance", "C) Resistance ÷ Current", "D) Power × Time"],
        "answer": "B",
        "explanation": "Ohm's Law: V = I × R (Voltage = Current × Resistance)."
    },
    {
        "q": "In a series circuit, what happens to total resistance when more resistors are added?",
        "choices": ["A) It decreases", "B) It stays the same", "C) It increases", "D) It becomes zero"],
        "answer": "C",
        "explanation": "In a series circuit, resistances add up: R_total = R1 + R2 + R3…"
    },
    {
        "q": "In a parallel circuit, what happens to total resistance when more resistors are added?",
        "choices": ["A) It increases", "B) It stays the same", "C) It decreases", "D) It doubles"],
        "answer": "C",
        "explanation": "In parallel, adding more paths lowers total resistance: 1/R_total = 1/R1 + 1/R2…"
    },
    {
        "q": "A circuit has a 12V battery and a 4-ohm resistor. What is the current?",
        "choices": ["A) 1 A", "B) 2 A", "C) 3 A", "D) 4 A"],
        "answer": "C",
        "explanation": "I = V ÷ R = 12 ÷ 4 = 3 Amperes."
    },
    {
        "q": "What is the function of a diode?",
        "choices": [
            "A) Stores electrical charge.",
            "B) Amplifies signals.",
            "C) Allows current to flow in only one direction.",
            "D) Converts AC to DC mechanically."
        ],
        "answer": "C",
        "explanation": "A diode allows current to flow in only one direction, acting as a one-way valve."
    },
    {
        "q": "What does AC stand for in electrical terms?",
        "choices": ["A) Actual Current", "B) Alternating Current", "C) Amplified Circuit", "D) Adjusted Charge"],
        "answer": "B",
        "explanation": "AC stands for Alternating Current — current that periodically reverses direction."
    },
    {
        "q": "A transformer steps voltage UP. What happens to current?",
        "choices": ["A) Current also increases.", "B) Current stays the same.", "C) Current decreases.", "D) Current becomes zero."],
        "answer": "C",
        "explanation": "In a transformer, power is conserved (P = IV). If voltage increases, current must decrease proportionally."
    },
    {
        "q": "What component stores electrical energy in an electric field?",
        "choices": ["A) Resistor", "B) Inductor", "C) Capacitor", "D) Transistor"],
        "answer": "C",
        "explanation": "A capacitor stores energy in an electric field between two conductive plates."
    },
    {
        "q": "What is the standard household voltage in the United States?",
        "choices": ["A) 12V", "B) 60V", "C) 110–120V", "D) 220–240V"],
        "answer": "C",
        "explanation": "Standard US household voltage is 110–120V AC at 60 Hz."
    },
    {
        "q": "Electrical power (P) is calculated as:",
        "choices": ["A) P = V + I", "B) P = V × I", "C) P = V ÷ I", "D) P = I ÷ V"],
        "answer": "B",
        "explanation": "Power (Watts) = Voltage (Volts) × Current (Amps): P = V × I."
    },
]

# Master dictionary mapping subtest code to its question list
ALL_SUBTESTS = {
    "AR": AR_QUESTIONS,
    "WK": WK_QUESTIONS,
    "PC": PC_QUESTIONS,
    "MC": MC_QUESTIONS,
    "GS": GS_QUESTIONS,
    "AS": AS_QUESTIONS,
    "EI": EI_QUESTIONS,
}

SUBTEST_NAMES = {
    "AR": "Arithmetic Reasoning",
    "WK": "Word Knowledge (VE)",
    "PC": "Paragraph Comprehension (VE)",
    "MC": "Mechanical Comprehension",
    "GS": "General Science",
    "AS": "Assembling Objects",
    "EI": "Electronics Information",
}

# GT composite uses AR + VE (WK + PC combined)
GT_SUBTESTS = ["AR", "WK", "PC"]
# ST composite uses MC + AS + EI + GS
ST_SUBTESTS = ["MC", "GS", "AS", "EI"]

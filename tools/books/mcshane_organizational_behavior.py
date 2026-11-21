# McShane & Von Glinow - Organizational Behavior: Emerging Knowledge, Global Reality.
# Chapter list: 2026 release, from McGraw Hill's product page table of contents (mheducation.com).
# Summaries cover each chapter's standard topics; they are written for this site, not copied from the book.

def ch(n, title, text, keys):
    return (n, title, [text], keys)

C = [
    ch(1, "Introduction to the Field of Organizational Behavior", "Organizational behavior (OB) studies what people think, feel, and do in and around organizations. Organizations are groups of people who work interdependently toward a purpose. Perspectives of organizational effectiveness include the open systems view, organizational learning, high-performance work practices, and the stakeholder perspective. OB relies on evidence-based management rather than fads or intuition.", ["OB = people in organizations", "Open systems perspective", "Stakeholder perspective", "Evidence-based management"]),
    ch(2, "Individual Differences: Personality and Values", "The MARS model explains individual behavior through Motivation, Ability, Role perceptions, and Situational factors. Personality traits are described by the Big Five (conscientiousness, agreeableness, neuroticism, openness, extraversion) and by the MBTI. Values are stable beliefs about what is important; Schwartz's model groups values, and cultural values differ across countries (individualism vs. collectivism, power distance).", ["MARS: motivation, ability, role perceptions, situation", "Big Five personality traits", "Values guide decisions", "Individualism vs. collectivism"]),
    ch(3, "Perceiving Ourselves and Others in Organizations", "Self-concept includes self-enhancement, self-verification, and self-evaluation (self-esteem, self-efficacy, locus of control). Perception is selecting, organizing, and interpreting information. Errors include stereotyping, attribution errors (the fundamental attribution error and self-serving bias), the halo effect, and the self-fulfilling prophecy. Awareness and empathy improve perceptions.", ["Self-efficacy = belief in your ability", "Fundamental attribution error", "Halo effect and stereotyping", "Self-fulfilling prophecy"]),
    ch(4, "Workplace Emotions, Attitudes, and Stress", "Emotions shape attitudes and behavior at work. Emotional labor is managing emotions to meet job expectations, and emotional intelligence is the ability to recognize and manage emotions in oneself and others. Job satisfaction and organizational commitment affect performance and turnover. Stress results from stressors such as role overload and conflict; managing stress includes removing stressors, withdrawing, changing perceptions, and social support.", ["Emotional intelligence", "Emotional labor", "Job satisfaction and commitment", "Stressors and stress management"]),
    ch(5, "Foundations of Employee Motivation", "Motivation is the forces that affect the direction, intensity, and persistence of effort. Theories include Maslow's needs hierarchy, four-drive theory, expectancy theory (effort → performance → outcomes), goal setting (SMART goals with feedback), and equity/organizational justice. Feedback and fairness strongly influence motivation.", ["Direction, intensity, persistence", "Expectancy theory", "SMART goals with feedback", "Equity and fairness"]),
    ch(6, "Applied Performance Practices", "Organizations use rewards (membership, seniority, job status, competency, and performance-based pay), job design (job rotation, enlargement, enrichment), and empowerment to improve performance. The job characteristics model identifies skill variety, task identity, task significance, autonomy, and feedback as motivating features. Self-leadership helps people motivate themselves.", ["Job enrichment and rotation", "Job characteristics model", "Empowerment", "Self-leadership"]),
    ch(7, "Decision Making and Creativity", "The rational decision-making model identifies the problem, chooses a decision style, develops alternatives, chooses, implements, and evaluates. Real decisions are limited by bounded rationality, satisficing, and biases such as anchoring, confirmation bias, and escalation of commitment. Creativity follows stages (preparation, incubation, illumination, verification) and is supported by creative people and work environments; design thinking and employee involvement improve decisions.", ["Bounded rationality and satisficing", "Escalation of commitment", "Creative process: preparation, incubation, illumination, verification", "Design thinking"]),
    ch(8, "Team Dynamics", "Teams are groups whose members interact and share accountability. Team effectiveness depends on design (task, size, composition), processes such as development stages (forming, storming, norming, performing, adjourning), norms, cohesion, and trust. Problems include social loafing and process losses; self-directed and virtual teams have special considerations. Decision tools include brainstorming, nominal group technique, and electronic brainstorming.", ["Forming, storming, norming, performing, adjourning", "Social loafing", "Cohesion and trust", "Nominal group technique"]),
    ch(9, "Communicating in Teams and Organizations", "Communication involves encoding, transmitting through channels, decoding, and feedback. Channels vary in media richness, from face-to-face (richest) to written messages. Barriers include perception differences, filtering, language, and information overload. Organizations use direct communication from leaders, grapevines, and digital tools.", ["Encode, transmit, decode, feedback", "Media richness", "Information overload", "Grapevine communication"]),
    ch(10, "Power and Influence in the Workplace", "Power is the capacity to influence others. Sources are legitimate, reward, coercive, expert, and referent power; contingencies such as substitutability, centrality, visibility, and discretion amplify power. Influence tactics include persuasion, ingratiation, impression management, coalition formation, upward appeal, and pressure. Organizational politics occur when influence serves self-interest.", ["Legitimate, reward, coercive, expert, referent power", "Persuasion is effective influence", "Organizational politics", "Contingencies of power"]),
    ch(11, "Conflict and Negotiation in the Workplace", "Conflict can be task-related (constructive) or relationship-related (harmful). Causes include incompatible goals, differentiation, interdependence, scarce resources, ambiguous rules, and communication problems. Conflict styles are problem solving (win-win), forcing, avoiding, yielding, and compromising. Negotiation strategies, BATNA, and third-party resolution (mediation, arbitration) help resolve disputes.", ["Task vs. relationship conflict", "Problem solving = win-win", "BATNA", "Mediation vs. arbitration"]),
    ch(12, "Leadership in Organizational Settings", "Leadership is influencing and enabling others to contribute to organizational success. Perspectives include transformational leadership (vision, modeling, encouraging experimentation, building commitment), managerial leadership, path-goal theory, situational leadership, servant leadership, authentic leadership, and implicit leadership theories. Competencies such as emotional intelligence and integrity matter.", ["Transformational leadership", "Path-goal and situational leadership", "Servant and authentic leadership", "Leadership competencies"]),
    ch(13, "Designing Organizational Structures", "Organizational structure divides labor and coordinates work through informal communication, formal hierarchy, and standardization. Elements include span of control, centralization, and formalization; structures are mechanistic or organic. Forms include functional, divisional, team-based, matrix, and network structures, chosen based on environment, size, technology, and strategy.", ["Span of control, centralization, formalization", "Mechanistic vs. organic", "Functional, divisional, matrix, team-based", "Fit with environment and strategy"]),
    ch(14, "Organizational Culture", "Organizational culture is shared values and assumptions. It is seen through artifacts: stories, rituals, language, and physical structures. Strong, adaptive cultures support performance. Culture is changed and strengthened through leadership actions, aligning artifacts, selection, and socialization of new employees. Mergers often fail due to culture clashes.", ["Shared values and assumptions", "Artifacts reveal culture", "Socialization of newcomers", "Culture clashes in mergers"]),
    ch(15, "Organizational Change", "Lewin's force field model says change requires unfreezing, moving, and refreezing, increasing driving forces and reducing restraining forces. Resistance to change comes from direct costs, saving face, fear of the unknown, and habits. Strategies include communication, learning, involvement, stress management, negotiation, and coercion as a last resort. Approaches include action research, appreciative inquiry, and large group interventions.", ["Unfreeze, move, refreeze", "Driving vs. restraining forces", "Reasons for resistance", "Appreciative inquiry"]),
]

Q = [
    ((1, 2, 3), [
        (1, "Organizational behavior studies:", "What people think, feel, and do in organizations", ["Only company finances", "Only machines", "Only marketing"], "It applies to everyone in organizations."),
        (1, "Making decisions based on the best available evidence is:", "Evidence-based management", ["Intuition-only management", "Fad management", "Random choice"], "It avoids following trends blindly."),
        (1, "The perspective that organizations must satisfy people who affect or are affected by them is the:", "Stakeholder perspective", ["Open systems perspective", "Learning perspective", "Mechanistic perspective"], "Stakeholders include employees, customers, and communities."),
        (2, "The MARS model explains behavior through motivation, ability, role perceptions, and:", "Situational factors", ["Salary", "Skills only", "Supervision"], "All four affect performance."),
        (2, "Which is one of the Big Five personality traits?", "Conscientiousness", ["Intelligence", "Creativity", "Loyalty"], "Others: agreeableness, neuroticism, openness, extraversion."),
        (2, "A culture that values group goals over individual goals is:", "Collectivist", ["Individualist", "Low power distance", "Masculine"], "Individualist cultures value personal goals."),
        (3, "Belief in your ability to perform a task is:", "Self-efficacy", ["Self-esteem", "Locus of control", "Self-enhancement"], "It affects motivation."),
        (3, "Blaming others' behavior on their personality rather than the situation is the:", "Fundamental attribution error", ["Self-serving bias", "Halo effect", "Recency effect"], "We overlook situational causes."),
        (3, "When one positive trait shapes our overall view of someone, it's the:", "Halo effect", ["Stereotype", "Primacy effect", "False consensus"], "It distorts performance appraisals."),
        (3, "When expectations about someone cause them to act that way, it's a:", "Self-fulfilling prophecy", ["Stereotype threat", "Halo effect", "Attribution"], "Expectations shape behavior."),
    ]),
    ((4, 5, 6), [
        (4, "The ability to recognize and manage emotions in yourself and others is:", "Emotional intelligence", ["Emotional labor", "Cognitive dissonance", "Stress"], "It's important for leaders and teams."),
        (4, "Managing emotions to meet job expectations, like smiling at customers, is:", "Emotional labor", ["Emotional intelligence", "Job satisfaction", "Burnout"], "It can be stressful."),
        (4, "Having too much work to do is a stressor called:", "Role overload", ["Role ambiguity", "Low interdependence", "Job enrichment"], "It's a major source of work stress."),
        (5, "Motivation affects the direction, intensity, and:", "Persistence of effort", ["Price of effort", "Location of work", "Salary level"], "These are the three elements of motivation."),
        (5, "Effective goals are:", "Specific, challenging, and accompanied by feedback", ["Vague and easy", "Set without feedback", "Impossible"], "SMART goals work best."),
        (5, "Expectancy theory says people are motivated when they believe:", "Effort leads to performance and valued outcomes", ["All rewards are equal", "Needs follow a fixed order", "Punishment works best"], "E → P → O."),
        (6, "Adding more responsibility and control to a job is:", "Job enrichment", ["Job rotation", "Job enlargement", "Job sharing"], "Enlargement adds more tasks of similar difficulty."),
        (6, "Which is a core job characteristic?", "Autonomy", ["Salary", "Office size", "Commute"], "Others: skill variety, task identity, task significance, feedback."),
        (6, "Moving employees between different jobs is:", "Job rotation", ["Job enrichment", "Empowerment", "Demotion"], "It builds skills and reduces boredom."),
        (4, "Social support helps employees:", "Cope with stress", ["Increase stress", "Avoid work", "Lose motivation"], "Coworkers and family can help."),
    ]),
    ((7, 8, 9), [
        (7, "Choosing an option that is good enough rather than the best is:", "Satisficing", ["Maximizing", "Anchoring", "Brainstorming"], "It reflects bounded rationality."),
        (7, "Continuing a failing course of action because of past investment is:", "Escalation of commitment", ["Satisficing", "Groupthink", "Incubation"], "It's related to the sunk cost fallacy."),
        (7, "In the creative process, stepping away from a problem so ideas can form is:", "Incubation", ["Preparation", "Illumination", "Verification"], "Illumination is the 'aha' moment."),
        (8, "The team stage where conflict over roles and goals arises is:", "Storming", ["Forming", "Norming", "Performing"], "Teams then develop norms."),
        (8, "When team members put in less effort than they would alone, it's:", "Social loafing", ["Synergy", "Cohesion", "Groupthink"], "Clear accountability reduces it."),
        (8, "A technique where members write ideas alone before discussing and voting is:", "Nominal group technique", ["Brainstorming", "Delphi only", "Devil's advocacy"], "It reduces dominance by a few members."),
        (9, "The richest communication channel is:", "Face-to-face conversation", ["Email", "Memo", "Text message"], "It allows immediate feedback and nonverbal cues."),
        (9, "Receiving more information than you can process is:", "Information overload", ["Filtering", "Media richness", "Grapevine"], "It's a common communication barrier."),
        (9, "Informal communication networks in organizations are called the:", "Grapevine", ["Hierarchy", "Matrix", "Channel"], "They spread information quickly."),
        (8, "Team cohesion refers to:", "How attracted members are to the team and motivated to stay", ["The team's size", "The team's budget", "The team's deadline"], "High cohesion can improve performance."),
    ]),
    ((10, 11, 12), [
        (10, "Power based on a person's knowledge or skills is:", "Expert power", ["Legitimate power", "Coercive power", "Reward power"], "Referent power comes from admiration."),
        (10, "Power that comes from being admired or liked is:", "Referent power", ["Expert power", "Legitimate power", "Coercive power"], "Charismatic leaders often have it."),
        (10, "Using logical arguments and evidence to influence others is:", "Persuasion", ["Coercion", "Ingratiation", "Upward appeal"], "It's often the most effective tactic."),
        (11, "Conflict focused on the issue rather than the people is:", "Task (constructive) conflict", ["Relationship conflict", "Personal conflict", "Avoidance"], "It can improve decisions."),
        (11, "The conflict style that seeks a win-win solution is:", "Problem solving", ["Forcing", "Avoiding", "Yielding"], "It integrates both sides' interests."),
        (11, "Your best alternative if a negotiation fails is your:", "BATNA", ["Bottom line only", "Opening offer", "Agenda"], "Best Alternative To a Negotiated Agreement."),
        (11, "A third party who makes a binding decision is an:", "Arbitrator", ["Mediator", "Negotiator", "Facilitator"], "Mediators help parties reach their own agreement."),
        (12, "Leaders who create a vision and inspire change are:", "Transformational leaders", ["Transactional leaders", "Laissez-faire leaders", "Micromanagers"], "They build commitment."),
        (12, "Leaders who focus on serving followers' needs are:", "Servant leaders", ["Autocratic leaders", "Coercive leaders", "Transactional leaders"], "They put others first."),
        (12, "Path-goal theory says leaders should:", "Choose behaviors that help followers reach goals", ["Always use the same style", "Avoid giving direction", "Focus only on punishment"], "Style depends on the situation."),
    ]),
    ((13, 14, 15), [
        (13, "The number of people reporting directly to a manager is the:", "Span of control", ["Chain of command", "Centralization", "Formalization"], "Wide spans create flatter organizations."),
        (13, "An organization with many rules and centralized decisions is:", "Mechanistic", ["Organic", "Flat", "Virtual"], "Organic structures are flexible."),
        (13, "A structure where employees report to both a functional and a project manager is:", "Matrix", ["Functional", "Divisional", "Simple"], "It combines two structures."),
        (14, "Organizational culture is:", "Shared values and assumptions", ["The building layout", "The organization chart", "The budget"], "It guides behavior."),
        (14, "Stories, rituals, and language that reveal culture are:", "Artifacts", ["Values only", "Strategies", "Policies"], "They're visible signs of culture."),
        (14, "Helping new employees learn the culture is called:", "Socialization", ["Recruitment", "Termination", "Promotion"], "It shapes newcomers' behavior."),
        (15, "Lewin's model of change is:", "Unfreeze, move, refreeze", ["Plan, do, check, act", "Forming, storming, norming", "Alarm, resistance, exhaustion"], "Change must be stabilized."),
        (15, "A common reason employees resist change is:", "Fear of the unknown", ["Too much information", "Higher pay", "More autonomy"], "Communication reduces resistance."),
        (15, "An approach to change that focuses on what works well is:", "Appreciative inquiry", ["Coercion", "Downsizing", "Force field analysis only"], "It builds on strengths."),
        (13, "A structure organized around products, clients, or regions is:", "Divisional", ["Functional", "Matrix", "Simple"], "Functional structures group by specialty."),
    ]),
]

BOOK = {
    "titles": ["Organizational Behavior"],
    "edition": "2026 release",
    "source": "McGraw Hill product page table of contents",
    "chapters": C,
    "quizzes": Q,
}

# Pass & Freestyle Trainer - CarbonX Plugin

A comprehensive training plugin for Rocket League that helps players improve their passing plays and freestyle dribbling skills through intelligent tracking, real-time feedback, and progressive difficulty levels.

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.7+-green.svg)
![Platform](https://img.shields.io/badge/platform-CarbonX-orange.svg)

## 🎯 Features Overview

### Passing Play Training
- **Pass Trainer Mode**: Tracks and evaluates passing accuracy and quality
- **Pass Quality Scoring**: Awards points based on pass speed and execution
- **Multiple Pass Types**: Ground, aerial, and wall passes
- **Pass Timing Analysis**: Feedback on when to pass vs. shoot
- **Accuracy Tracking**: Detailed statistics on successful vs. attempted passes

### Freestyle Dribbling Training
- **Aerial Control Trainer**: Tracks air time and awards points for sustained control
- **Flip Reset Detector**: Recognizes flip reset opportunities and tracks execution
- **Air Dribble Tracker**: Monitors air dribble consistency and technique
- **Ceiling Shot Practice**: Detects ceiling touches and ceiling shot attempts
- **Recovery Trainer**: Evaluates landing quality after aerial maneuvers

### Intelligent Feedback System
- **Real-Time Scoring**: Immediate point awards for successful maneuvers
- **Color-Coded Console Output**: Easy-to-read feedback with visual indicators
- **Progressive Difficulty**: 4 difficulty levels (Beginner → Pro) with scaled rewards
- **Session Statistics**: Comprehensive tracking of progress and performance

### Difficulty Levels
1. **Beginner** (1.0x multiplier): Perfect for learning basics
2. **Intermediate** (1.5x multiplier): Building consistency
3. **Advanced** (2.0x multiplier): Refining technique
4. **Pro** (2.5x multiplier): Mastery level challenges

## 📥 Installation

### Prerequisites
- Rocket League installed
- CarbonX bot system set up and running
- Python 3.7 or higher

### Installation Steps

1. **Locate Your Plugins Folder**
   - Navigate to your CarbonX installation directory
   - Find the `PLUGINS` folder

2. **Install the Plugin**
   - Copy `plugin_PassFreestyleTrainer.py` to the `PLUGINS` folder
   - Ensure the filename starts with `plugin_` prefix

3. **Load the Plugin**
   - Launch your CarbonX bot system
   - The plugin will auto-load and display initialization message
   - Look for the colorful startup message in console

4. **Verify Installation**
   - You should see: "Pass & Freestyle Trainer v1.0.0 loaded!"
   - Available commands will be listed in the console

## 🎮 Usage Guide

### Quick Start

1. **Enable the Plugin**
   ```
   pft enable
   ```

2. **Select Training Mode**
   ```
   pft mode pass_trainer
   ```
   Available modes:
   - `pass_trainer` - Practice passing accuracy
   - `aerial_control` - Master air control
   - `flip_reset` - Learn flip resets
   - `air_dribble` - Perfect air dribbles
   - `ceiling_shot` - Practice ceiling shots
   - `recovery` - Improve landing recovery

3. **Set Difficulty**
   ```
   pft difficulty beginner
   ```
   Levels: `beginner`, `intermediate`, `advanced`, `pro`

4. **Start Training**
   - Play normally in game
   - Plugin tracks your actions automatically
   - Points and feedback appear in console

5. **Check Progress**
   ```
   pft stats
   ```

### Console Commands

| Command | Description | Example |
|---------|-------------|---------|
| `pft enable` | Toggle plugin on/off | `pft enable` |
| `pft mode <mode>` | Set training mode | `pft mode aerial_control` |
| `pft difficulty <level>` | Set difficulty | `pft difficulty intermediate` |
| `pft spawn_pass` | Spawn pass scenario | `pft spawn_pass` |
| `pft spawn_freestyle` | Spawn freestyle scenario | `pft spawn_freestyle` |
| `pft stats` | Show statistics | `pft stats` |
| `pft reset` | Reset session stats | `pft reset` |

## 🏋️ Training Modes Explained

### 1. Pass Trainer Mode
**Objective**: Improve passing accuracy and decision-making

**How it Works**:
- Tracks when you hit the ball
- Measures ball speed after contact
- Awards points for passes over 500 speed
- Higher speed = more points

**Tips**:
- Focus on hitting the ball with good power
- Aim for 1000+ ball speed for best scores
- Practice different pass angles
- Start with ground passes, progress to aerials

**Scoring**:
- Base: 10 points per quality pass
- Multiplied by pass quality (0-1)
- Scaled by difficulty level

### 2. Aerial Control Trainer
**Objective**: Master car control while airborne

**How it Works**:
- Tracks total air time
- Awards points every update tick while airborne
- Rewards sustained aerial control (1+ seconds)
- Logs progress every 2 seconds

**Tips**:
- Practice air roll control
- Work on directional air roll
- Try maintaining altitude
- Combine with ball touches for maximum score

**Scoring**:
- 0.5 points per tick while airborne (after 1 second)
- Scales with difficulty

### 3. Flip Reset Trainer
**Objective**: Learn flip reset mechanics and timing

**How it Works**:
- Detects when car is close to ball (under 150 units)
- Both car and ball must be airborne
- Awards points for flip reset opportunities
- Tracks consecutive resets

**Tips**:
- Approach ball from below
- Match ball velocity
- Use air roll to align wheels
- Practice on wall-to-air setups

**Scoring**:
- 15 points per flip reset opportunity
- Cooldown prevents spam scoring
- Tracks total freestyle tricks

### 4. Air Dribble Trainer
**Objective**: Perfect air dribble technique and consistency

**How it Works**:
- Monitors car-ball distance in air
- Both must be airborne
- Awards points for close proximity (< 200 units)
- Continuous tracking for extended dribbles

**Tips**:
- Keep ball close to car
- Match ball velocity
- Use small adjustments
- Practice feathering boost

**Scoring**:
- 1 point per tick when active
- Periodic console feedback
- Best for building consistency

### 5. Ceiling Shot Trainer
**Objective**: Master ceiling shot mechanics

**How it Works**:
- Detects when car touches ceiling (Z > 1900)
- Car must be airborne (wheels off ceiling)
- Awards points for ceiling touches
- 2-second cooldown between detections

**Tips**:
- Jump off ceiling, don't fall
- Maintain car control after ceiling touch
- Practice ceiling-to-ball transitions
- Work on double touches

**Scoring**:
- 20 points per ceiling touch
- Tracks as freestyle tricks
- Higher points reflect difficulty

### 6. Recovery Trainer
**Objective**: Improve landing safety and consistency

**How it Works**:
- Monitors air time and landing speed
- Evaluates recovery quality on landing
- Better recovery (slower landing) = more points
- Helps reduce whiffs and maintain possession

**Tips**:
- Air roll to land on wheels
- Bleed speed before landing
- Practice wave dashes
- Anticipate landing location

**Scoring**:
- Up to 5 points per recovery
- Based on landing speed quality
- Only "good" recoveries are logged

## 📊 Statistics Tracking

### Session Stats Display

Access with `pft stats` command:

```
═══════════════════════════════════
   Pass & Freestyle Trainer Stats
═══════════════════════════════════
Session Time: 15m 32s
Total Score: 547.5 points
Passes: 12/18 (66.7%)
Freestyle Tricks: 8
Total Air Time: 45.3s
Current Mode: aerial_control
Difficulty: intermediate
═══════════════════════════════════
```

### Tracked Metrics

- **Session Time**: Total time training
- **Total Score**: Accumulated points
- **Pass Accuracy**: Success rate (successful/attempted)
- **Freestyle Tricks**: Count of flip resets, ceiling touches
- **Air Time**: Total seconds airborne
- **Current Settings**: Active mode and difficulty

## 🎯 Training Progression Guide

### Week 1: Foundations
**Goal**: Learn the basics

**Daily Plan** (30 min/day):
- Days 1-3: Pass Trainer (Beginner) - 15 min
- Days 1-3: Recovery Trainer (Beginner) - 15 min
- Days 4-7: Aerial Control (Beginner) - 20 min
- Days 4-7: Pass Trainer (Beginner) - 10 min

**Target**: 
- 50+ successful passes
- 10+ minutes total air time
- 80%+ pass accuracy

### Week 2: Building Skills
**Goal**: Increase difficulty and variety

**Daily Plan** (45 min/day):
- Pass Trainer (Intermediate) - 15 min
- Air Dribble Trainer (Beginner) - 15 min
- Aerial Control (Intermediate) - 15 min

**Target**:
- 100+ successful passes
- 20+ minutes total air time
- Maintain 70%+ pass accuracy

### Week 3: Advanced Techniques
**Goal**: Learn advanced mechanics

**Daily Plan** (60 min/day):
- Flip Reset Trainer (Beginner) - 20 min
- Ceiling Shot Trainer (Beginner) - 20 min
- Air Dribble (Intermediate) - 20 min

**Target**:
- 5+ flip reset attempts
- 10+ ceiling touches
- Consistent air dribbles (30+ seconds)

### Week 4: Mastery
**Goal**: Refine and combine skills

**Daily Plan** (60 min/day):
- All modes on Advanced difficulty
- Focus on lowest scoring areas
- Practice mode combinations

**Target**:
- 200+ passes at Advanced
- 10+ flip resets
- 20+ ceiling shots
- 90%+ pass accuracy

## 🔧 Customization & Configuration

### Adjusting Update Rate

In the plugin code, you can modify:
```python
self.update_interval = 1.0 / 30.0  # 30 Hz default
```

Lower values = more frequent updates (higher CPU usage)
Higher values = less frequent updates (better performance)

### Customizing Difficulty Multipliers

Modify the multipliers:
```python
self.difficulty_multipliers = {
    "beginner": 1.0,
    "intermediate": 1.5,
    "advanced": 2.0,
    "pro": 2.5
}
```

### Adjusting Detection Thresholds

**Pass Speed Threshold**:
```python
if ball_speed > 500:  # Minimum speed for valid pass
```

**Flip Reset Distance**:
```python
if distance < 150:  # Maximum distance for flip reset
```

**Air Dribble Distance**:
```python
if distance < 200:  # Maximum distance for air dribble
```

## 🐛 Troubleshooting

### Plugin Not Loading

**Symptom**: No startup message in console

**Solutions**:
1. Verify filename starts with `plugin_`
2. Check file is in correct PLUGINS folder
3. Ensure no syntax errors (check Python console)
4. Verify Python 3.7+ is installed

### Commands Not Working

**Symptom**: Commands have no effect

**Solutions**:
1. Check plugin is enabled (`pft enable`)
2. Verify exact command syntax
3. Look for error messages in console
4. Try restarting the bot system

### No Points Being Awarded

**Symptom**: Actions don't generate points

**Solutions**:
1. Ensure plugin is enabled
2. Verify correct training mode is set
3. Check you're meeting mode requirements
4. Confirm difficulty is set
5. Look for console error messages

### Stats Not Updating

**Symptom**: Statistics don't change

**Solutions**:
1. Plugin must be enabled
2. Game must be active (valid game_tick_packet)
3. Try resetting stats (`pft reset`)
4. Check update_interval isn't too high

## 💡 Pro Tips

### General Training Tips
1. **Start Small**: Begin with Beginner difficulty
2. **Focus**: Work on one mode at a time
3. **Consistency**: Train daily for best results
4. **Track Progress**: Check stats regularly
5. **Mix It Up**: Combine different modes

### Mode-Specific Tips

**Pass Trainer**:
- Practice against walls for rebounds
- Work on pass timing (when teammate would receive)
- Try different ball speeds

**Aerial Control**:
- Practice without ball first
- Focus on smooth movements
- Try aerial while boosting vs. not boosting

**Flip Reset**:
- Master slow approaches first
- Practice on custom training packs
- Watch replays to see wheel contact

**Air Dribble**:
- Start from ground → air transitions
- Master single touches before chains
- Practice feathering boost

**Ceiling Shot**:
- Practice driving on ceiling first
- Work on ceiling-to-ball reads
- Try different drop angles

**Recovery**:
- Always think about next move
- Practice power sliding
- Use air roll for clean landings

## 📝 Technical Details

### Plugin Architecture

The plugin follows CarbonX plugin standards:
- Class name: `plugin_PassFreestyleTrainer`
- Required methods: `Name()`, `Description()`, `Author()`, `Version()`
- Game data via: `game_tick_packet_set()`
- Main loop: `main()` runs continuously

### Performance Optimization

- **Update Rate Limiting**: 30 Hz default (configurable)
- **Minimal CPU Usage**: Sleep intervals prevent CPU spike
- **Efficient Calculations**: Optimized distance/speed formulas
- **Smart Cooldowns**: Prevent duplicate detections

### Dependencies

- `time`: For timing and intervals
- `math`: For calculations (distance, angles, speed)
- `random`: For future randomized scenarios
- `rlbot.agents.base_agent`: For SimpleControllerState

## 🤝 Contributing

Want to improve the plugin? Here's how:

1. **Report Bugs**: Describe issue, steps to reproduce
2. **Suggest Features**: Explain use case and benefit
3. **Submit Code**: Follow existing style, test thoroughly
4. **Improve Docs**: Fix typos, add examples, clarify

## 📜 License

MIT License - Free to use, modify, and distribute.

```
MIT License

Copyright (c) 2024 CarbonX Plugin Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software.
```

## 🙏 Credits

- **CarbonX Team**: For the amazing plugin system
- **RLBot Community**: For the framework and tools
- **Rocket League Players**: For feedback and testing

## 📞 Support

- **Issues**: Report on GitHub or Discord
- **Questions**: Ask in CarbonX Discord
- **Updates**: Check GitHub for new versions

## 🔄 Changelog

### Version 1.0.0 (Initial Release)
- ✨ Pass Trainer with quality scoring
- ✨ Aerial Control tracking
- ✨ Flip Reset detection
- ✨ Air Dribble monitoring
- ✨ Ceiling Shot tracking
- ✨ Recovery evaluation
- ✨ 4 difficulty levels
- ✨ Comprehensive statistics
- ✨ Color-coded console feedback
- ✨ Session tracking and reset

## 🎯 Future Plans

- [ ] Visual overlay support (if CarbonX adds rendering)
- [ ] Custom training pack integration
- [ ] Replay analysis and suggestions
- [ ] Multiplayer pass training scenarios
- [ ] AI-based technique recommendations
- [ ] Mobile app for progress tracking
- [ ] Advanced combo detection
- [ ] Leaderboards and challenges

---

**Made with ❤️ for the Rocket League community**

*Train hard, rank up! 🚗⚽*

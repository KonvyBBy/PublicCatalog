# Quick Start Guide - Pass & Freestyle Trainer

## Installation (2 minutes)

1. **Copy the plugin file**
   - Copy `plugin_PassFreestyleTrainer.py` 
   - Paste into your `PLUGINS` folder
   
2. **Start your CarbonX bot**
   - Launch Rocket League
   - Start CarbonX system
   - Look for green startup message

3. **You should see:**
   ```
   ● [PLUGIN] Pass & Freestyle Trainer v1.0.0 loaded!
   ```

## First Training Session (5 minutes)

### Basic Commands

```bash
# Enable the plugin
pft enable

# Choose a training mode
pft mode pass_trainer

# Set difficulty
pft difficulty beginner

# Check your stats anytime
pft stats

# Reset stats to start fresh
pft reset
```

### Try Pass Training

1. Enable plugin: `pft enable`
2. Set mode: `pft mode pass_trainer`
3. Play Rocket League normally
4. Hit the ball hard (500+ speed)
5. Watch console for feedback:
   ```
   ✓ Great Pass! +10.5 points
   ```

### Try Aerial Training

1. Set mode: `pft mode aerial_control`
2. Stay in the air for 1+ seconds
3. Get points for sustained control:
   ```
   ⚡ Aerial Control: 2.5s +0.5 pts
   ```

### Try Freestyle Training

1. Set mode: `pft mode flip_reset`
2. Get close to ball while airborne
3. Earn points for opportunities:
   ```
   🔄 Flip Reset Opportunity! +15.0 pts
   ```

## All Training Modes

| Mode | Focus | Best For |
|------|-------|----------|
| `pass_trainer` | Passing accuracy | Beginners |
| `aerial_control` | Air time & control | All levels |
| `flip_reset` | Flip reset setups | Advanced |
| `air_dribble` | Air dribble consistency | Intermediate |
| `ceiling_shot` | Ceiling touches | Advanced |
| `recovery` | Safe landings | Beginners |

## Difficulty Levels

| Level | Multiplier | When to Use |
|-------|------------|-------------|
| `beginner` | 1.0x | Learning basics |
| `intermediate` | 1.5x | Building consistency |
| `advanced` | 2.0x | Refining technique |
| `pro` | 2.5x | Mastery challenges |

## Training Schedule

### Day 1-3: Basics
```bash
pft enable
pft mode pass_trainer
pft difficulty beginner
# Play for 15 minutes
pft stats
```

### Day 4-7: Air Control
```bash
pft enable
pft mode aerial_control
pft difficulty beginner
# Play for 20 minutes
pft stats
```

### Week 2+: Advanced
```bash
pft enable
pft mode flip_reset
pft difficulty intermediate
# Play for 30 minutes
pft stats
```

## Tips for Success

✅ **DO**:
- Start with Beginner difficulty
- Focus on one mode per session
- Check stats regularly (`pft stats`)
- Reset stats between sessions (`pft reset`)
- Increase difficulty gradually

❌ **DON'T**:
- Jump straight to Pro difficulty
- Switch modes too frequently
- Ignore console feedback
- Forget to enable plugin
- Train when tired

## Understanding Feedback

### Color Codes

- 🟢 **Green**: Success (passes, recoveries)
- 🔵 **Cyan**: Info (aerial control)
- 🟣 **Purple**: Freestyle (flip resets)
- 🟠 **Orange**: Advanced (ceiling shots)
- 🔴 **Red**: Errors

### Point Values

| Action | Base Points | Notes |
|--------|-------------|-------|
| Quality Pass | 10 pts | Based on speed |
| Aerial Control | 0.5 pts/tick | Sustained air time |
| Flip Reset | 15 pts | Per opportunity |
| Ceiling Touch | 20 pts | High difficulty |
| Good Recovery | 5 pts | Based on landing |
| Air Dribble | 1 pt/tick | Continuous contact |

## Viewing Statistics

Type `pft stats` to see:

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

## Common Issues

### "Game not active" error
- Ensure you're in a match (not menu)
- CarbonX bot must be running

### No points awarded
- Check plugin is enabled (`pft enable`)
- Verify correct mode is set
- Check difficulty is set
- Read mode requirements above

### Commands not working
- Check exact spelling
- Plugin must be loaded first
- Look for error messages in console

## Next Steps

1. ✅ Complete 3 training sessions
2. 📈 Track your improvement with stats
3. 🎯 Increase difficulty when ready
4. 🏆 Try all training modes
5. 📖 Read full README for advanced tips

## Need Help?

- 📘 Read `README_PassFreestyleTrainer.md` for detailed docs
- 💬 Ask in CarbonX Discord
- 🐛 Report bugs on GitHub

---

**Ready to improve? Type `pft enable` and start training! 🚀**

# Pass & Freestyle Trainer - Console Output Examples

## Plugin Startup
```
● [PLUGIN] Pass & Freestyle Trainer v1.0.0 loaded!
Type commands in console to control the plugin:
  pft enable - Enable the plugin
  pft mode <mode> - Set training mode
  pft difficulty <level> - Set difficulty
  pft spawn_pass - Spawn pass training scenario
  pft spawn_freestyle - Spawn freestyle scenario
  pft stats - Show session statistics
  pft reset - Reset session stats
```

## Enable Plugin
```
> pft enable
✓ Pass & Freestyle Trainer enabled!
```

## Set Training Mode
```
> pft mode pass_trainer
✓ Training mode set to: pass_trainer
```

## Set Difficulty
```
> pft difficulty intermediate
✓ Difficulty set to: intermediate
```

## Training Feedback - Pass Trainer
```
✓ Great Pass! +12.5 points
✓ Great Pass! +15.8 points
✓ Great Pass! +10.2 points
```

## Training Feedback - Aerial Control
```
⚡ Aerial Control: 2.1s +0.5 pts
⚡ Aerial Control: 4.1s +0.5 pts
⚡ Aerial Control: 6.1s +0.5 pts
```

## Training Feedback - Flip Reset
```
🔄 Flip Reset Opportunity! +15.0 pts
🔄 Flip Reset Opportunity! +15.0 pts
```

## Training Feedback - Air Dribble
```
💨 Air Dribble Active +1.0 pts
💨 Air Dribble Active +1.0 pts
```

## Training Feedback - Ceiling Shot
```
🏠 Ceiling Touch! +20.0 pts
```

## Training Feedback - Recovery
```
✓ Good Recovery! +4.8 pts
✓ Good Recovery! +3.2 pts
```

## Session Statistics
```
> pft stats
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

## Reset Session
```
> pft reset
✓ Session statistics reset!
```

## Error Messages
```
> pft mode invalid_mode
Invalid mode. Valid modes: none, pass_trainer, aerial_control, flip_reset, air_dribble, ceiling_shot, recovery

> pft difficulty expert
Invalid difficulty. Valid: beginner, intermediate, advanced, pro

> pft spawn_pass
(when game not active)
Error: Game not active
```

## Complete Training Session Example
```
> pft enable
✓ Pass & Freestyle Trainer enabled!

> pft mode pass_trainer
✓ Training mode set to: pass_trainer

> pft difficulty beginner
✓ Difficulty set to: beginner

> pft reset
✓ Session statistics reset!

[Playing Rocket League - making passes]

✓ Great Pass! +10.0 points
✓ Great Pass! +8.5 points
✓ Great Pass! +12.3 points
✓ Great Pass! +11.7 points

> pft stats
═══════════════════════════════════
   Pass & Freestyle Trainer Stats
═══════════════════════════════════
Session Time: 5m 12s
Total Score: 42.5 points
Passes: 4/6 (66.7%)
Freestyle Tricks: 0
Total Air Time: 0.0s
Current Mode: pass_trainer
Difficulty: beginner
═══════════════════════════════════

> pft mode aerial_control
✓ Training mode set to: aerial_control

[Flying around in-game]

⚡ Aerial Control: 2.0s +0.5 pts
⚡ Aerial Control: 4.0s +0.5 pts
⚡ Aerial Control: 6.0s +0.5 pts
✓ Good Recovery! +3.5 pts

> pft stats
═══════════════════════════════════
   Pass & Freestyle Trainer Stats
═══════════════════════════════════
Session Time: 8m 45s
Total Score: 46.0 points
Passes: 4/6 (66.7%)
Freestyle Tricks: 0
Total Air Time: 6.5s
Current Mode: aerial_control
Difficulty: beginner
═══════════════════════════════════
```

## Advanced Session with Multiple Modes
```
> pft enable
✓ Pass & Freestyle Trainer enabled!

> pft difficulty advanced
✓ Difficulty set to: advanced

> pft mode flip_reset
✓ Training mode set to: flip_reset

[Attempting flip resets]

🔄 Flip Reset Opportunity! +30.0 pts
🔄 Flip Reset Opportunity! +30.0 pts
✓ Good Recovery! +8.5 pts

> pft mode ceiling_shot
✓ Training mode set to: ceiling_shot

[Practicing ceiling shots]

🏠 Ceiling Touch! +40.0 pts
🏠 Ceiling Touch! +40.0 pts
✓ Good Recovery! +6.8 pts

> pft mode air_dribble
✓ Training mode set to: air_dribble

[Air dribbling practice]

💨 Air Dribble Active +2.0 pts
💨 Air Dribble Active +2.0 pts
💨 Air Dribble Active +2.0 pts

> pft stats
═══════════════════════════════════
   Pass & Freestyle Trainer Stats
═══════════════════════════════════
Session Time: 25m 18s
Total Score: 161.3 points
Passes: 0/0 (0%)
Freestyle Tricks: 4
Total Air Time: 127.8s
Current Mode: air_dribble
Difficulty: advanced
═══════════════════════════════════
```

## Pro Level Training
```
> pft difficulty pro
✓ Difficulty set to: pro

> pft mode flip_reset
✓ Training mode set to: flip_reset

[Advanced freestyle practice]

🔄 Flip Reset Opportunity! +37.5 pts  (2.5x multiplier!)
🔄 Flip Reset Opportunity! +37.5 pts
🔄 Flip Reset Opportunity! +37.5 pts
🏠 Ceiling Touch! +50.0 pts
✓ Good Recovery! +10.5 pts

> pft stats
═══════════════════════════════════
   Pass & Freestyle Trainer Stats
═══════════════════════════════════
Session Time: 12m 05s
Total Score: 173.0 points
Passes: 0/0 (0%)
Freestyle Tricks: 4
Total Air Time: 45.2s
Current Mode: flip_reset
Difficulty: pro
═══════════════════════════════════
```

## Color Legend (as seen in console)
- 🟢 Green: Success messages, good passes, recoveries
- 🔵 Cyan: Info messages, aerial control, mode names
- 🟡 Yellow: Scores, difficulty levels, version info
- 🟣 Purple: Freestyle tricks, flip resets
- 🟠 Orange: Advanced tricks, ceiling shots
- 🔴 Red: Errors, problems, invalid input
- ⚪ White: General text, descriptions, stats

## Tips for Reading Console Output
1. **Point values change with difficulty** - Higher difficulty = more points
2. **Multiple actions tracked simultaneously** - Pass + aerial control both score
3. **Cooldowns prevent spam** - Some actions have delays between scoring
4. **Stats are cumulative** - All modes contribute to session total
5. **Color coding helps identify** - Quick visual scan of feedback type

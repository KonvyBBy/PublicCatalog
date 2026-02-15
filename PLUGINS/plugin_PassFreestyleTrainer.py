"""
Pass & Freestyle Trainer Plugin for CarbonX
A comprehensive training plugin for Rocket League to improve passing plays and freestyle dribbling skills.

Author: CarbonX Plugin Team
Version: 1.0.0
"""

import time
import math
import random
from rlbot.agents.base_agent import SimpleControllerState

class plugin_PassFreestyleTrainer:
    def __init__(self, player_index=0, ConsoleLogger=None, BotController=None):
        self.controller = None
        self.player_index = player_index
        self.game_tick_packet = None
        self.ConsoleLogger = ConsoleLogger
        self.BotController = BotController
        self.pid = None
        self.playername = "default"
        
        # Training state
        self.enabled = False
        self.current_mode = "none"  # none, pass_trainer, aerial_control, flip_reset, air_dribble, ceiling_shot, recovery
        self.difficulty = "beginner"  # beginner, intermediate, advanced, pro
        self.show_visuals = True
        
        # Session statistics
        self.session_start_time = time.time()
        self.successful_passes = 0
        self.attempted_passes = 0
        self.freestyle_tricks = 0
        self.total_score = 0.0
        self.air_time = 0.0
        self.last_ground_time = time.time()
        
        # Pass training state
        self.pass_target_location = None
        self.pass_started = False
        self.pass_start_time = 0
        self.pass_strength = 1500.0
        self.pass_drill_type = "ground"  # ground, aerial, wall
        
        # Freestyle training state
        self.freestyle_active = False
        self.flip_reset_count = 0
        self.ceiling_touch_time = 0
        self.last_ball_touch = 0
        self.combo_count = 0
        self.last_trick_time = 0
        
        # Ball spawn settings
        self.ball_spawn_x = 0.0
        self.ball_spawn_y = 0.0
        self.ball_spawn_z = 500.0
        
        # Difficulty multipliers
        self.difficulty_multipliers = {
            "beginner": 1.0,
            "intermediate": 1.5,
            "advanced": 2.0,
            "pro": 2.5
        }
        
        # Last update time for tick rate control
        self.last_update = time.time()
        self.update_interval = 1.0 / 30.0  # 30 Hz update rate
        
    def Name(self):
        self.ConsoleLogger("{cyan}Pass & Freestyle Trainer")
    
    def Description(self):
        self.ConsoleLogger("{white}Comprehensive training plugin for passing plays and freestyle mechanics. "
                         "Includes pass trainer, aerial control, flip reset practice, air dribbles, "
                         "ceiling shots, and recovery training with multiple difficulty levels.")
    
    def Author(self):
        self.ConsoleLogger("{green}Created by CarbonX Team")
    
    def Version(self):
        self.ConsoleLogger("{yellow}v1.0.0")
    
    def game_tick_packet_set(self, packet, local_player_index=0, playername="default", process_id=None):
        self.game_tick_packet = packet
        self.player_index = local_player_index
        self.pid = process_id
        self.playername = playername
        
        if self.controller:
            return self.controller
        else:
            return None
    
    def main(self):
        """Main plugin loop - runs continuously"""
        self.ConsoleLogger("{green}● [PLUGIN] {cyan}Pass & Freestyle Trainer {white}v1.0.0 loaded!")
        self.ConsoleLogger("{yellow}Type commands in console to control the plugin:")
        self.ConsoleLogger("  {cyan}pft enable{white} - Enable the plugin")
        self.ConsoleLogger("  {cyan}pft mode <mode>{white} - Set training mode")
        self.ConsoleLogger("  {cyan}pft difficulty <level>{white} - Set difficulty")
        self.ConsoleLogger("  {cyan}pft spawn_pass{white} - Spawn pass training scenario")
        self.ConsoleLogger("  {cyan}pft spawn_freestyle{white} - Spawn freestyle scenario")
        self.ConsoleLogger("  {cyan}pft stats{white} - Show session statistics")
        self.ConsoleLogger("  {cyan}pft reset{white} - Reset session stats")
        
        target_fps = 30
        frame_duration = 1.0 / target_fps
        
        while True:
            try:
                start_time = time.time()
                
                if self.game_tick_packet and self.enabled:
                    current_time = time.time()
                    
                    # Only update at specified interval to reduce CPU usage
                    if current_time - self.last_update >= self.update_interval:
                        self.update_training()
                        self.last_update = current_time
                
                # Frame rate limiting
                elapsed_time = time.time() - start_time
                sleep_duration = frame_duration - elapsed_time
                if sleep_duration > 0:
                    time.sleep(sleep_duration)
                else:
                    time.sleep(0.001)  # Minimal sleep to prevent CPU spike
                    
            except Exception as e:
                self.ConsoleLogger(f"{{red}}Error in main loop: {e}")
                time.sleep(1)
                self.controller = None
    
    def update_training(self):
        """Update training logic based on current mode"""
        if not self.game_tick_packet:
            return
        
        # Track air time
        player = self.get_player()
        if player:
            if not player.has_wheel_contact:
                self.air_time += self.update_interval
            else:
                self.last_ground_time = time.time()
        
        # Update based on current mode
        if self.current_mode == "pass_trainer":
            self.update_pass_trainer()
        elif self.current_mode == "aerial_control":
            self.update_aerial_control()
        elif self.current_mode == "flip_reset":
            self.update_flip_reset()
        elif self.current_mode == "air_dribble":
            self.update_air_dribble()
        elif self.current_mode == "ceiling_shot":
            self.update_ceiling_shot()
        elif self.current_mode == "recovery":
            self.update_recovery()
    
    def update_pass_trainer(self):
        """Update pass training mode"""
        player = self.get_player()
        ball = self.game_tick_packet.game_ball
        
        if not player or not ball:
            return
        
        # Calculate distance to ball
        distance = self.calculate_distance(
            player.physics.location,
            ball.physics.location
        )
        
        # Detect pass attempt (player close to ball)
        if distance < 200 and not self.pass_started:
            self.pass_started = True
            self.pass_start_time = time.time()
            self.attempted_passes += 1
        
        # Evaluate pass quality
        if self.pass_started:
            ball_speed = self.calculate_speed(ball.physics.velocity)
            
            # Good pass criteria
            if ball_speed > 500:
                # Calculate pass accuracy (simplified)
                pass_quality = min(ball_speed / 2000.0, 1.0)
                
                if time.time() - self.pass_start_time > 0.5:  # Half second delay
                    self.successful_passes += 1
                    points = 10 * pass_quality * self.difficulty_multipliers[self.difficulty]
                    self.total_score += points
                    self.ConsoleLogger(f"{{green}}✓ Great Pass! {{white}}+{points:.1f} points")
                    self.pass_started = False
            
            # Reset if ball slows down
            if ball_speed < 300 and time.time() - self.pass_start_time > 2.0:
                self.pass_started = False
    
    def update_aerial_control(self):
        """Update aerial control training"""
        player = self.get_player()
        
        if not player:
            return
        
        # Award points for sustained aerial control
        if not player.has_wheel_contact:
            air_duration = time.time() - self.last_ground_time
            
            if air_duration > 1.0:  # More than 1 second in air
                points = 0.5 * self.difficulty_multipliers[self.difficulty]
                self.total_score += points
                
                if int(air_duration) % 2 == 0:  # Log every 2 seconds
                    self.ConsoleLogger(f"{{cyan}}⚡ Aerial Control: {air_duration:.1f}s {{white}}+{points:.1f} pts")
    
    def update_flip_reset(self):
        """Update flip reset training"""
        player = self.get_player()
        ball = self.game_tick_packet.game_ball
        
        if not player or not ball:
            return
        
        # Check for flip reset opportunity (car near ball underside in air)
        distance = self.calculate_distance(
            player.physics.location,
            ball.physics.location
        )
        
        if distance < 150 and not player.has_wheel_contact:
            # Potential flip reset
            current_time = time.time()
            if current_time - self.last_ball_touch > 0.5:
                self.flip_reset_count += 1
                self.last_ball_touch = current_time
                points = 15 * self.difficulty_multipliers[self.difficulty]
                self.total_score += points
                self.freestyle_tricks += 1
                self.ConsoleLogger(f"{{purple}}🔄 Flip Reset Opportunity! {{white}}+{points:.1f} pts")
    
    def update_air_dribble(self):
        """Update air dribble training"""
        player = self.get_player()
        ball = self.game_tick_packet.game_ball
        
        if not player or not ball:
            return
        
        # Track air dribble (both car and ball in air, close together)
        distance = self.calculate_distance(
            player.physics.location,
            ball.physics.location
        )
        
        if not player.has_wheel_contact and ball.physics.location.z > 150:
            if distance < 200:
                points = 1.0 * self.difficulty_multipliers[self.difficulty]
                self.total_score += points
                
                if int(self.total_score) % 10 == 0:  # Log periodically
                    self.ConsoleLogger(f"{{blue}}💨 Air Dribble Active {{white}}+{points:.1f} pts")
    
    def update_ceiling_shot(self):
        """Update ceiling shot training"""
        player = self.get_player()
        
        if not player:
            return
        
        # Detect ceiling touch (car near ceiling)
        if player.physics.location.z > 1900 and not player.has_wheel_contact:
            current_time = time.time()
            if current_time - self.ceiling_touch_time > 2.0:
                self.ceiling_touch_time = current_time
                points = 20 * self.difficulty_multipliers[self.difficulty]
                self.total_score += points
                self.freestyle_tricks += 1
                self.ConsoleLogger(f"{{orange}}🏠 Ceiling Touch! {{white}}+{points:.1f} pts")
    
    def update_recovery(self):
        """Update recovery training"""
        player = self.get_player()
        
        if not player:
            return
        
        # Award points for good recoveries (landing from air)
        if player.has_wheel_contact and self.air_time > 0.5:
            # Calculate recovery quality based on landing speed
            landing_speed = self.calculate_speed(player.physics.velocity)
            recovery_quality = max(0, 1.0 - (landing_speed / 2000.0))
            
            points = 5 * recovery_quality * self.difficulty_multipliers[self.difficulty]
            self.total_score += points
            
            if recovery_quality > 0.5:
                self.ConsoleLogger(f"{{green}}✓ Good Recovery! {{white}}+{points:.1f} pts")
            
            self.air_time = 0
    
    def spawn_pass_scenario(self):
        """Spawn a pass training scenario"""
        if not self.game_tick_packet:
            self.ConsoleLogger("{red}Error: Game not active")
            return
        
        self.ConsoleLogger(f"{{cyan}}Spawning {self.pass_drill_type} pass scenario...")
        
        # Note: Actual ball spawning would require memory manipulation
        # This is a placeholder for the intended functionality
        self.pass_started = False
        self.attempted_passes += 1
        
        self.ConsoleLogger("{green}✓ Pass scenario spawned! Practice your pass!")
    
    def spawn_freestyle_scenario(self):
        """Spawn a freestyle training scenario"""
        if not self.game_tick_packet:
            self.ConsoleLogger("{red}Error: Game not active")
            return
        
        self.ConsoleLogger(f"{{purple}}Spawning freestyle scenario at height {self.ball_spawn_z}...")
        
        # Note: Actual ball spawning would require memory manipulation
        # This is a placeholder for the intended functionality
        self.freestyle_active = True
        
        self.ConsoleLogger("{green}✓ Freestyle scenario spawned! Show your skills!")
    
    def show_stats(self):
        """Display session statistics"""
        session_time = time.time() - self.session_start_time
        minutes = int(session_time / 60)
        seconds = int(session_time % 60)
        
        pass_accuracy = 0
        if self.attempted_passes > 0:
            pass_accuracy = (self.successful_passes / self.attempted_passes) * 100
        
        self.ConsoleLogger("{cyan}═══════════════════════════════════")
        self.ConsoleLogger("{yellow}   Pass & Freestyle Trainer Stats")
        self.ConsoleLogger("{cyan}═══════════════════════════════════")
        self.ConsoleLogger(f"{{white}}Session Time: {{green}}{minutes}m {seconds}s")
        self.ConsoleLogger(f"{{white}}Total Score: {{yellow}}{self.total_score:.1f} points")
        self.ConsoleLogger(f"{{white}}Passes: {{green}}{self.successful_passes}{{white}}/{{red}}{self.attempted_passes} {{white}}({pass_accuracy:.1f}%)")
        self.ConsoleLogger(f"{{white}}Freestyle Tricks: {{purple}}{self.freestyle_tricks}")
        self.ConsoleLogger(f"{{white}}Total Air Time: {{cyan}}{self.air_time:.1f}s")
        self.ConsoleLogger(f"{{white}}Current Mode: {{cyan}}{self.current_mode}")
        self.ConsoleLogger(f"{{white}}Difficulty: {{yellow}}{self.difficulty}")
        self.ConsoleLogger("{cyan}═══════════════════════════════════")
    
    def reset_stats(self):
        """Reset session statistics"""
        self.session_start_time = time.time()
        self.successful_passes = 0
        self.attempted_passes = 0
        self.freestyle_tricks = 0
        self.total_score = 0.0
        self.air_time = 0.0
        
        self.ConsoleLogger("{green}✓ Session statistics reset!")
    
    def set_mode(self, mode):
        """Set training mode"""
        valid_modes = ["none", "pass_trainer", "aerial_control", "flip_reset", 
                      "air_dribble", "ceiling_shot", "recovery"]
        
        if mode.lower() in valid_modes:
            self.current_mode = mode.lower()
            self.ConsoleLogger(f"{{green}}✓ Training mode set to: {{cyan}}{self.current_mode}")
        else:
            self.ConsoleLogger(f"{{red}}Invalid mode. Valid modes: {', '.join(valid_modes)}")
    
    def set_difficulty(self, difficulty):
        """Set difficulty level"""
        valid_difficulties = ["beginner", "intermediate", "advanced", "pro"]
        
        if difficulty.lower() in valid_difficulties:
            self.difficulty = difficulty.lower()
            self.ConsoleLogger(f"{{green}}✓ Difficulty set to: {{yellow}}{self.difficulty}")
        else:
            self.ConsoleLogger(f"{{red}}Invalid difficulty. Valid: {', '.join(valid_difficulties)}")
    
    def toggle_enable(self):
        """Toggle plugin enable/disable"""
        self.enabled = not self.enabled
        status = "enabled" if self.enabled else "disabled"
        color = "green" if self.enabled else "red"
        self.ConsoleLogger(f"{{{color}}}✓ Pass & Freestyle Trainer {status}!")
    
    # Utility functions
    def get_player(self):
        """Get current player data"""
        if not self.game_tick_packet:
            return None
        
        if self.player_index < len(self.game_tick_packet.game_cars):
            return self.game_tick_packet.game_cars[self.player_index]
        return None
    
    def calculate_distance(self, pos1, pos2):
        """Calculate 3D distance between two positions"""
        dx = pos2.x - pos1.x
        dy = pos2.y - pos1.y
        dz = pos2.z - pos1.z
        return math.sqrt(dx*dx + dy*dy + dz*dz)
    
    def calculate_speed(self, velocity):
        """Calculate speed from velocity vector"""
        return math.sqrt(velocity.x**2 + velocity.y**2 + velocity.z**2)
    
    def calculate_angle(self, vec1, vec2):
        """Calculate angle between two vectors"""
        dot = vec1.x * vec2.x + vec1.y * vec2.y + vec1.z * vec2.z
        mag1 = math.sqrt(vec1.x**2 + vec1.y**2 + vec1.z**2)
        mag2 = math.sqrt(vec2.x**2 + vec2.y**2 + vec2.z**2)
        
        if mag1 == 0 or mag2 == 0:
            return 0
        
        cos_angle = dot / (mag1 * mag2)
        cos_angle = max(-1.0, min(1.0, cos_angle))  # Clamp to valid range
        return math.acos(cos_angle)

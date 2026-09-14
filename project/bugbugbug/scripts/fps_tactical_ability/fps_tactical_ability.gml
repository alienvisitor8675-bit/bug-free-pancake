#macro FPS_DASH_ACTIVE_FRAMES 8
#macro FPS_DASH_COOLDOWN_FRAMES 90
#macro FPS_DASH_SPEED 18

/// Creates a fresh Phase Dash state for a new run or room.
function fps_dash_create_state() {
	return {
		cooldown_frames: 0,
		active_frames: 0,
		direction_x: 0,
		direction_y: 0,
	};
}

/// Ticks the dash timers without changing its direction contract.
function fps_dash_tick(_state) {
	_state.cooldown_frames = max(0, _state.cooldown_frames - 1);
	_state.active_frames = max(0, _state.active_frames - 1);
	if (_state.active_frames <= 0) {
		_state.direction_x = 0;
		_state.direction_y = 0;
	}

	return _state;
}

/// Starts one normalized dash when the ability is ready and input has direction.
function fps_dash_start(_state, _direction_x, _direction_y) {
	if (_state.cooldown_frames > 0 || _state.active_frames > 0) {
		return false;
	}

	var _direction_length = point_distance(0, 0, _direction_x, _direction_y);
	if (_direction_length <= 0) {
		return false;
	}

	_state.direction_x = _direction_x / _direction_length;
	_state.direction_y = _direction_y / _direction_length;
	_state.active_frames = FPS_DASH_ACTIVE_FRAMES;
	_state.cooldown_frames = FPS_DASH_COOLDOWN_FRAMES;
	return true;
}

/// Returns whether the player can activate the dash now.
function fps_dash_ready(_state) {
	return _state.cooldown_frames <= 0 && _state.active_frames <= 0;
}

/// Returns whether the player is inside the brief damage-proof phase window.
function fps_dash_is_active(_state) {
	return _state.active_frames > 0;
}

/// Returns the movement vector for the active dash, or no movement when idle.
function fps_dash_movement(_state) {
	if (!fps_dash_is_active(_state)) {
		return [0, 0];
	}

	return [
		_state.direction_x * FPS_DASH_SPEED,
		_state.direction_y * FPS_DASH_SPEED,
	];
}

/// Reports whether incoming damage must be ignored for the current frame.
function fps_dash_blocks_damage(_state) {
	return fps_dash_is_active(_state);
}

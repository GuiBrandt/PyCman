class InputManager:
    
    _state = {}

    def key_state(k):
        return InputManager._state[k] if k in InputManager._state else False

    def key_down(k):
        InputManager._state[k] = True

    def key_up(k):
        InputManager._state[k] = False
class Difficulty:
    """Oyun zorluk seviyelerini yönetir."""
    def __init__(self):
        self.difficulty_levels = {
            "easy": {"speed": 1000, "time_limit": 30},
            "medium": {"speed": 700, "time_limit": 20},
            "hard": {"speed": 500, "time_limit": 10},
        }
        self.current_level = "easy"  # Varsayılan zorluk seviyesi

    def set_difficulty(self, level):
        """Zorluk seviyesini ayarla."""
        if level in self.difficulty_levels:
            self.current_level = level
        else:
            raise ValueError(f"Geçersiz zorluk seviyesi: {level}")

    def get_settings(self):
        """Geçerli zorluk seviyesinin ayarlarını al."""
        return self.difficulty_levels[self.current_level]

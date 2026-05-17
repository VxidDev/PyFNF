from pathlib import Path
import json, pygame

class Mod:
    def __init__(self, mod_path: str) -> None:
        self.is_malformed: bool = False

        self.mod_path: Path = Path(mod_path)

        self.mod_name: Path | None = None
        self.mod_bg_path: Path | None = None
        self.mod_song_path: Path | None = None 

        if not self.parse_mod_data():
            self.is_malformed = True
            return

        self.mod_song: pygame.mixer.Sound | None = None 
        self.mod_bg: pygame.Surface | None = None

        if not self.init_mod():
            self.is_malformed = True
            return

    def parse_mod_data(self) -> bool:
        try:
            with open(f"{self.mod_path}/data.json", "r") as mod_data:
                mod_data_json: dict[str, str] = json.load(mod_data)

                self.mod_name = mod_data_json["name"]
                self.mod_bg_path = self.mod_path / Path(mod_data_json["bg"])
                self.mod_song_path = self.mod_path / Path(mod_data_json["song"])

                return True
        except (FileNotFoundError, json.JSONDecodeError, KeyError) as exc:
            print(f"Malformed Mod: {type(exc).__name__}: {str(exc)}")
            return False

    def init_mod(self) -> bool:
        if not self.mod_bg_path.exists():
            print("Mod Loader: Mod BG not found.")
            return False

        if not self.mod_song_path.exists():
            print("Mod Loader: Mod song not found.")
            return False 

        self.mod_song = pygame.mixer.Sound(self.mod_song_path)
        self.mod_bg = pygame.image.load(self.mod_bg_path)

        return True

    def __repr__(self) -> str:
        return f"Mod({self.mod_path.stem}, {self.mod_bg_path}, {self.mod_bg_path}, malformed={self.is_malformed})"

class ModLoader:
    def __init__(self, path: str) -> None:
        self.path: str = path 

        self.mod_entries: list[Mod] = self.load_mod_entries()

        if not self.mod_entries:
            print("No mods detected.")
            return  

        print("Loaded mods: ")

        for mod in self.mod_entries:
            print(mod)

    def load_mod_entries(self) -> list:
        path = Path(self.path) / "mods"
        mods = []

        if not path.exists() or not path.is_dir():
            return mods 

        for entry in path.iterdir():
            mods.append(Mod(entry))

        return mods
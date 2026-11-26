# Make the AI Judge Feel Nostalgic: A Childhood Memory — entry for make.fun.
# Writes the childhood memory sentence to entry.txt in the output directory.
import os

LINE = "On rainy afternoons my mother would fry pitha while the tin roof drummed overhead, and I would sit by the window counting the seconds between lightning and thunder, certain the storm was only for us."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()

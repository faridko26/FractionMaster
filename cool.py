import time
import math

def draw_sine_wave():
    """Draw an animated sine wave in the terminal."""
    width = 60
    height = 10

    for frame in range(50):
        lines = []
        for y in range(height):
            row = ""
            for x in range(width):
                # Calculate sine wave position
                wave_y = int((height / 2) + (height / 3) * math.sin((x + frame) * 0.2))
                if y == wave_y:
                    row += "*"
                elif y == height // 2:
                    row += "-"
                else:
                    row += " "
            lines.append(row)

        # Clear and print
        print("\033[H\033[J", end="")  # Clear screen
        print("=" * width)
        print("\n".join(lines))
        print("=" * width)
        print(f"  Frame: {frame + 1}/50")
        time.sleep(0.1)

    print("\nDone! Thanks for watching the wave!")

if __name__ == "__main__":
    draw_sine_wave()

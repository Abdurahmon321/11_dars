def colored_print(text, color="red"):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m"
    }
    end_color = "\033[0m"

    color_code = colors.get(color.lower())
    return color_code + text + end_color


def free_space():
    print(colored_print("-" * 50, color="red"))

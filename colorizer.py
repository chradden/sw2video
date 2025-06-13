import os
import sys
import os
sys.path.append(os.path.abspath("DeOldify"))

from deoldify.visualize import get_image_colorizer

# DeOldify erwartet, dass du im DeOldify-Verzeichnis arbeitest
# Deshalb ändern wir temporär das Verzeichnis
def colorize_image(input_path):
    cwd = os.getcwd()
    deoldify_path = os.path.join(cwd, "DeOldify")
    models_path = os.path.join(deoldify_path, "models")
    os.makedirs(models_path, exist_ok=True)

    # Wechsle in das DeOldify-Verzeichnis
    os.chdir(deoldify_path)

    # Lade den Colorizer
    colorizer = get_image_colorizer(artistic=True)

    # Führe Kolorierung durch
    output_path = input_path.replace(".jpg", "_color.jpg")
    colorizer.plot_transformed_image(
        path=input_path,
        results_dir=os.path.dirname(input_path),
        render_factor=35,
        display_render_factor=False
    )

    # Zurück ins ursprüngliche Verzeichnis
    os.chdir(cwd)

    return output_path
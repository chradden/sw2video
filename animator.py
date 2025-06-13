import os
import subprocess

def animate_image(image_path):
    cwd = os.getcwd()
    model_dir = os.path.join(cwd, "first-order-model")
    driving_video = os.path.join(model_dir, "demo", "motion.mp4")
    config_path = os.path.join(model_dir, "config", "vox-256.yaml")
    checkpoint_path = os.path.join(model_dir, "checkpoints", "vox-cpk.pth.tar")

    os.makedirs(os.path.join(model_dir, "result"), exist_ok=True)
    output_path = os.path.join(model_dir, "result", os.path.basename(image_path).replace(".jpg", "_animated.mp4"))

    # Führe das Model als externes Python-Skript aus
    subprocess.run([
        "python3", "demo.py",
        "--config", config_path,
        "--driving_video", driving_video,
        "--source_image", image_path,
        "--checkpoint", checkpoint_path,
        "--relative",
        "--adapt_scale",
        "--result_video", output_path
    ], cwd=model_dir)

    return output_path
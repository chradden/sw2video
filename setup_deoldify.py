import os
import subprocess

def setup_deoldify():
    if not os.path.exists("DeOldify"):
        subprocess.run(["git", "clone", "https://github.com/jantic/DeOldify.git"])
    os.chdir("DeOldify")

    subprocess.run(["pip", "install", "-r", "requirements-colab.txt"])

    os.makedirs("models", exist_ok=True)
    model_path = os.path.join("models", "ColorizeArtistic_gen.pth")

    if not os.path.exists(model_path):
        print("⬇️ Lade Modell (ColorizeArtistic_gen.pth) ...")
        subprocess.run([
            "wget",
            "-O", model_path,
            "https://data.deepai.org/deoldify/ColorizeArtistic_gen.pth"
        ])

    print("✅ DeOldify ist vollständig eingerichtet.")
    os.chdir("..")

if __name__ == "__main__":
    setup_deoldify()
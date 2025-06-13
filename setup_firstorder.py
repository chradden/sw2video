import os
import subprocess

def setup_first_order_model():
    if not os.path.exists("first-order-model"):
        subprocess.run(["git", "clone", "https://github.com/AliaksandrSiarohin/first-order-model.git"])
    os.chdir("first-order-model")

    subprocess.run(["pip", "install", "-r", "requirements.txt"])

    # Modell-Checkpoint
    os.makedirs("checkpoints", exist_ok=True)
    ckpt_path = os.path.join("checkpoints", "vox-cpk.pth.tar")
    if not os.path.exists(ckpt_path):
        print("⬇️ Lade Pretrained Checkpoint...")
        subprocess.run([
            "wget", "-O", ckpt_path,
            "https://www.dropbox.com/s/zg2n6n4ws9c6uyt/vox-cpk.pth.tar?dl=1"
        ])

    # Beispiel-Driving-Video
    os.makedirs("demo", exist_ok=True)
    demo_path = os.path.join("demo", "motion.mp4")
    if not os.path.exists(demo_path):
        print("⬇️ Lade Beispielvideo (motion.mp4)...")
        subprocess.run([
            "wget", "-O", demo_path,
            "https://raw.githubusercontent.com/AliaksandrSiarohin/first-order-model/master/demo/driver.mp4"
        ])

    print("✅ First-Order-Model vollständig eingerichtet.")
    os.chdir("..")

if __name__ == "__main__":
    setup_first_order_model()
import cv2
import torch
from torchvision import transforms
from PIL import Image

def predict_disease(img_path):
    model = torch.load("models/crop_disease_model.pt")
    model.eval()
    img = Image.open(img_path).convert('RGB')
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor()
    ])
    img_tensor = transform(img).unsqueeze(0)
    output = model(img_tensor)
    _, predicted = output.max(1)
    return predicted.item()

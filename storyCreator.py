from ultralytics import YOLO

model = YOLO("best.pt")

#results = model.predict("/Users/sdhillon/D/Projects/hackathon/FigmatoStory/valid/images/HeaderSFRA_png.rf.39dc48b7ee4e37fde572d8416f63567f.jpg")
#results = model.predict("/Users/sdhillon/D/Projects/hackathon/FigmatoStory/valid/images/Header_png.rf.9388bf1183bf5a99205b6889ad43b950.jpg")
#results = model.predict("/Users/sdhillon/D/Projects/hackathon/FigmatoStory/valid/images/FooterBannerSFRA_png.rf.657a31b9056034ba81c04019777afdc9.jpg")
#results = model.predict("/Users/sdhillon/D/Projects/hackathon/FigmatoStory/train/images/header-menu_png.rf.f73730b0bc7400402abe351835957995.jpg")
results = model.predict("/Users/sdhillon/D/Projects/hackathon/FigmatoStory/valid/images/HOMEPAGE.jpg")



result = results[0]
output = []
test = result.boxes
for box in result.boxes:
    x1, y1, x2, y2 = [
        round(x) for x in box.xyxy[0].tolist()
    ]
    class_id = box.cls[0].item()
    prob = round(box.conf[0].item(), 2)
    output.append([
        x1, y1, x2, y2, result.names[class_id], prob
    ])
print(output)


from os import listdir
from os.path import isfile, join
import torch
from torchvision import transforms
from PIL import Image

models = {'inception': torch.load('./simpsons_model.pkl'),
          'dense': torch.load('./dense.pt', map_location=torch.device('cpu'))}

data_transforms = transforms.Compose([
    transforms.Resize([224, 224]),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

simpsons_class_names = ['Abraham Grampa Simpson',
                        'Agnes Skinner',
                        'Apu Nahasapeemapetilon',
                        'Barney Gumble',
                        'Bart Simpson',
                        'Carl Carlson',
                        'Charles Montgomery Burns',
                        'Chief Wiggum',
                        'Cletus Spuckler',
                        'Comic Book Guy',
                        'Disco Stu',
                        'Edna Krabappel',
                        'Fat Tony',
                        'Gil',
                        'Groundskeeper Willie',
                        'Homer Simpson',
                        'Kent Brockman',
                        'Krusty The Clown',
                        'Lenny Leonard',
                        'Lionel Hutz',
                        'Lisa Simpson',
                        'Maggie Simpson',
                        'Marge Simpson',
                        'Martin Prince',
                        'Mayor Quimby',
                        'Milhouse Van Houten',
                        'Miss Hoover',
                        'Moe Szyslak',
                        'Ned Flanders',
                        'Nelson Muntz',
                        'Otto Mann',
                        'Patty Bouvier',
                        'Principal Skinner',
                        'Professor John Frink',
                        'Rainier Wolfcastle',
                        'Ralph Wiggum',
                        'Selma Bouvier',
                        'Sideshow Bob',
                        'Sideshow Mel',
                        'Snake Jailbird',
                        'Troy Mcclure',
                        'Waylon Smithers']


def classify(img_file, model):
    image = Image.open(img_file)
    image.load()
    inp_data = data_transforms(image).unsqueeze(0)
    model.eval()
    predict = model(inp_data)
    predict_class = simpsons_class_names[torch.max(predict.data, 1)[1].item()]
    predict_proba = round(torch.sigmoid(torch.max(predict.data, 1)[0]).item()*100, 4)
    return predict_class, predict_proba
    # plt.imshow(image)
    # plt.title(simpsons_class_names[torch.max(out.data, 1)[1].item()])
    # plt.grid(False)


if __name__ == '__main__':
    models = torch.load("./dense.pt", map_location=torch.device('cpu')), \
             torch.load('./simpsons_model.pkl')
    MY_PATH = './static/test_imgs'
    imgs = [join(MY_PATH, f) for f in listdir(MY_PATH) if isfile(join(MY_PATH, f))]
    for img in imgs:
        print(img)
        classes = classify(img, models[0]), classify(img, models[1])
        out = f'{classes[0]:>30} {classes[1]:>30}'
        if classes[0] != classes[1]:
            out = out + '-->DIFF'
        print(out)

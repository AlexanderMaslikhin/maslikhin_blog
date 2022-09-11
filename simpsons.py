import torch
from torchvision import transforms, datasets, models
from PIL import Image
from matplotlib import colors, pyplot as plt


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
    out = model(inp_data)
    print(simpsons_class_names[torch.max(out.data, 1)[1].item()])
    # plt.imshow(image)
    # plt.title(simpsons_class_names[torch.max(out.data, 1)[1].item()])
    # plt.grid(False)


if __name__ == '__main__':
    model = torch.load("./simpsons_model.pkl", map_location=torch.device('cpu'))
    img = './test_imgs/apu.jpg'
    classify(img, model)
